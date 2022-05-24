pipeline {
    agent {
         docker { image 'inogo/docker-compose:1.21.2' }
    }

    stages {
        stage('Build') {
            steps {
                sh 'apk add --no-cache make git'
                sh 'make build'
            }
        }

        stage('Lint') {
            steps {
                sh 'docker run atera-api bash -c "black atera_client --check -l 120"'
            }
        }

        stage('Deploy to PyPi') {
            when {
                branch 'master'
            }

            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'roelvdboomPypi', usernameVariable: 'TWINE_USERNAME', passwordVariable: 'TWINE_PASSWORD']]) {
                    sh 'make publish'
                }
            }
        }
    }
}