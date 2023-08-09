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
                    // def dockerImage = 'your-dockerhub-username/flask-app'
                    def dockerImage = 'zoe2512/simple-web'
                    
                    // Build Docker image
                    docker.image('python:3.8-slim').inside {
                        sh 'pip install -r requirements.txt'
                        sh 'docker build -t ${dockerImage} .'
                    }
                    
                    // Login to DockerHub and push image
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        // sh "docker login -u your-dockerhub-username -p ${DOCKERHUB_PASSWORD}"
                        // sh "docker push ${dockerImage}"
                        sh "docker login -u zoe2512 -p ${DOCKERHUB_PASSWORD}"
                        sh "docker push ${dockerImage}"
                    }
                }
            }
        }
        
        stage('Deploy to Docker') {
            agent docker_node_01
            steps {
                script {
                    def dockerImage = 'zoe2512/simple-web'
                    def containerName = 'simple-web'
                    
                    // Stop and remove existing container (if any)
                    sh "docker stop ${containerName} || true"
                    sh "docker rm ${containerName} || true"
                    
                    // Pull and run Docker container
                    sh "docker pull ${dockerImage}"
                    sh "docker run -d --name simple-web -p 80:5000 ${dockerImage}"
                }
            }
        }
    }
    
    post {
        success {
            def mess = 'successful'
            echo "${mess}"
        }
        failure {
            def mess = 'failed'
            echo "${mess}"
        }
        stage('Email Notification') {
            steps {
                emailext (
                    to: 'nghihuynh7022@gmail.com',
                    subject: 'CI/CD Notification',
                    body: "Deployment of Flask app was ${mess}.",
                    mimeType: 'text/html',
                    attachLog: true,
                    recipientProviders: [[$class: 'CulpritsRecipientProvider']]
                )
            }
        }
    }
}
