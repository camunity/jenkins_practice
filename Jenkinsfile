pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('build){
            steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                        sh 'python3 -m venv env'
                        sh 'source ./env/bin/activate'
                        sh 'python -m pip install Flask --user'
                    }
                }
        }
        stage('test') {
            steps {
                    sh 'python3 test.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }
    }
}