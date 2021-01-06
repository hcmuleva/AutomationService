import threading

from flask import Flask, request, jsonify
from flask_api import status

sem = threading.Semaphore()
app = Flask(__name__)
config_pool = {}


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/addDeviceToPool", methods=["POST"])
def add_device_to_pool():
    print("Start request", request, " request info")
    if request and request.json:
        data = request.json
        if validate_request_param(data):
            config_pool[data["ip"]] = data["config"]
            return jsonify(
                {"msg": "Device successfully added", "status": status.HTTP_201_CREATED}
            )
        else:
            return jsonify(
                {
                    "msg": "Device info can not be empty or null",
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                }
            )
    return jsonify(
        {
            "msg": "Device info can not be empty or null",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
        }
    )


@app.route("/getIP", methods=["GET"])
def getIP():
    ip = None
    sem.acquire()
    if len(config_pool.keys()) > 0:
        ip, selected_device_info = config_pool.popitem()
    sem.release()
    if ip:
        return jsonify(
            {
                "msg": "Successfully received IP",
                "ip": ip,
                "config": selected_device_info,
                "status": status.HTTP_200_OK,
            }
        )
    else:
        return jsonify(
            {
                "msg": "No Device in pool",
                "status": status.HTTP_404_NOT_FOUND,
            }
        )


def validate_request_param(data):
    try:
        if data["ip"] and data["config"]:
            return True
        else:
            return False
    except Exception as e:
        return False


if __name__ == "__main__":
    app.run(debug=True)
