pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Git checkout code
                checkout scm
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    def dockerImage = 'your-dockerhub-username/flask-app'
                    
                    // Build Docker image
                    docker.image('python:3.8-slim').inside {
                        sh 'pip install -r requirements.txt'
                        sh 'docker build -t ${dockerImage} .'
                    }
                    
                    // Login to DockerHub and push image
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        sh "docker login -u your-dockerhub-username -p ${DOCKERHUB_PASSWORD}"
                        sh "docker push ${dockerImage}"
                    }
                }
            }
        }
        
        stage('Deploy to Docker') {
            steps {
                script {
                    def dockerImage = 'your-dockerhub-username/flask-app'
                    
                    // Stop and remove existing container (if any)
                    sh 'docker stop flask-app || true'
                    sh 'docker rm flask-app || true'
                    
                    // Pull and run Docker container
                    sh "docker pull ${dockerImage}"
                    sh "docker run -d --name flask-app -p 80:5000 ${dockerImage}"
                }
            }
        }
    }
    
    post {
        success {
            echo 'Deployment successful'
        }
        failure {
            echo 'Deployment failed'
        }
    }
}
