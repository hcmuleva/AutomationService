import json

import click
import logging
import requests
from time import sleep
from random import randint

from pyspark.sql.functions import udf, explode
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark import SparkConf
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s')
logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)


def run_testcases(TESTCASE):
    # Step1. Get IP and Configuration
    device_config = requests.get('http://localhost:5000/getIP')
    device_config_json = device_config.json()

    # Step2. Call to test execution
    ### this is the place actual python code will be executed
    print("TestCase Executing ")
    print(f'TestCase: {TESTCASE} DeviceInfoIP: {device_config_json}')
    sleep(randint(3, 10))  # Fake Sleep function to test functionality
    test_status = {'status':"Passed", "deviceInfo":device_config_json}
    # Step3. Put Ip back to ip pool
    submit_config_to_pool={"ip":device_config_json['ip'],"config":device_config_json["config"]}
    print('submit_config_to_pool==>',submit_config_to_pool)
    response = requests.post('http://localhost:5000/addDeviceToPool', json=submit_config_to_pool)

    return json.dumps(test_status)  # res['status']


udfrun_testcases = udf(run_testcases, StringType())

@click.command()
@click.option("--suite_name", help="suite name", required=True)
@click.option("--input_path", help="Input file name", required=True)
@click.option("--output_format", help="output file format", default='csv')
@click.option("--output_file_name", help="output file name", required=True)
@click.option("--num_parallel_test", help="Number of parallel test", required=True)
def run(suite_name, input_path, output_format, output_file_name, num_parallel_test):
    conf = SparkConf().setAll([('spark.executor.instances',num_parallel_test), ('spark.executor.memory', '1g'), ('spark.executor.cores', 1), ('spark.cores.max', 1),('spark.driver.memory','3g')])
    conf.setMaster(f'local[{num_parallel_test}]').setAppName("MyApp")
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    print(f'Spark config {spark.sparkContext.getConf().getAll()}')
    logging.warning(f"spark version {spark.version}")
    df = load_file(spark, input_path)
    df = df.filter(df.suite == suite_name)
    df = df.select(explode(df.TC).alias("TESTCASES"))
    df.show()

    print('partition count before', df.rdd.getNumPartitions())
    print('Total Input row count:', df.count())
    df = df.repartition(df.count())
    print('partition count after repartition', df.rdd.getNumPartitions())
    df = df.withColumn('status', udfrun_testcases('TESTCASES'))
    df.cache().count()
    df.show()
    df.coalesce(1).write.format(output_format).mode('overwrite').save(f'./data/output/{output_file_name}.{output_format}')
    spark.stop()


def load_file(spark, input_path):
    return (
        spark.read.format("json")
        .load(input_path)
    )


if __name__ == "__main__":
    run()