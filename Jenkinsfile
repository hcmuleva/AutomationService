pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Script related to Build modules will get called here'
                   bat 'C:\Users\Harish_Muleva\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\python  ./Build/build.py'
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