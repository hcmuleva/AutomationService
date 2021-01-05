pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Script related to Build modules will get called here'
                   bat 'python  ./Build/build.py'
            }
        }

        stage('Deployment') {
            steps {
                echo 'Script related to Deployment modules will get called here'
            }

        }

         stage('Unit Test') {

            steps {

                echo 'Unit Test Case module'

            }

        }

         stage('Regression') {
            steps {
                echo 'Regression Module'
            }
        }

    }

}