pipeline {
    agent any

    stages {

        stage('Build Image') {
            steps {
                bat "docker build -t leeon182/docker -f ./Dockerfile ."
            }
        }
		
        stage('Push Image') {
            steps {
				withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'pass', usernameVariable: 'user')]) {
					bat "docker login --username=${user} --password=${pass}"
					bat "docker push leeon182/docker:latest"
				}
            }
        }

        stage('a') {
            steps {
                bat "docker-compose build"
            }
        }

        stage('b') {
            steps {
                bat "docker-compose up"
            }
        }
		
    }
}