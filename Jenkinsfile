pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('build') {
            steps {
                   withEnv(["HOME=${env.WORKSPACE}"]) {
                        sh "pip install -r requirements.txt --user"
                    }
                }
        }
        stage('test') {
            steps {
                    sh 'python3 -m flask --version'
                    sh 'python3 test.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }
    }
}