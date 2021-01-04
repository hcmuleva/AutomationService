pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Script related to Build modules will get called here'
                   sh "chmod +x -R ${env.WORKSPACE}"
                   sh './Build/build.sh'
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