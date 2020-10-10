pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python3 -m venv env'
                    sh 'source ./env/bin/activate'
                    sh 'python3 -m pip install Flask --user'
                }
            }
        }
        stage('test') {
            steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                        sh 'python3 -m flask --version'
                        sh 'python3 test.py'
                    }
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }
    }
}