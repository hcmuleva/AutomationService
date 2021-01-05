pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Script related to Build modules will get called here'
                   bat 'python  ./CICD/Build/build.py'
            }
        }

        stage('Deployment') {
            steps {
                echo 'Script related to Deployment modules will get called here'
                bat 'python  ./CICD/Deployment/Deployment.py'
            }

        }
        stage('StaticAnalysis') {
            steps {
                echo 'Script related to StaticAnalysis modules will get called here'
                bat 'python  ./CICD/StaticAnalysis/StaticAnalysis.py'
            }

        }
         stage('Unit Test') {

            steps {

                echo 'Unit Test Case module'
                bat 'python  ./CICD/UnitTest/UnitTest.py'

            }

        }
     stage('BVT') {
            steps {
                echo 'BVT Test Case module'
                bat 'python  ./CICD/BVT/BVT.py'
            }
        }
        stage('Regression') {
            steps {
                echo 'Regression Module'
                 bat 'python  ./CICD/Regression/Regression.py'
            }
        }
      stage('Performance') {
            steps {
                echo 'Performance Module'
                bat 'python  ./CICD/Performance/Performance.py'
            }
        }
         stage('Security') {
            steps {
                echo 'Security Module'
                bat 'python  ./CICD/Security/Security.py'
            }
        }

    }

}