pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Git checkout code
                git 'https://github.com/ZK2207/jenkins.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // def dockerImage = 'your-dockerhub-username/flask-app'
                    sh "docker image prune -af"
                    def dockerImage = 'zoe2512/simple-web'
                    // Build Docker image
                    docker.image('python:3.8-slim').inside {
                        sh "docker build -t ${dockerImage} ."
                    }
                    /*def image = 'zoe2512/simple-web'
                    dockerImage = docker.build("${image}")*/
                }
            }
        }
        stage('Testing - Running in Docker Local') {
            /*agent {
                 label 'Docker_Local_Pool'
                }*/
            steps {
                script {
                    def dockerImage = 'zoe2512/simple-web'
                    def containerName = 'simple-web'
                    
                    // Stop and remove existing container (if any)
                    sh "docker stop ${containerName} || true"
                    sh "docker rm ${containerName} || true"
                    
                    // Pull and run Docker container
                    sh "docker run -d --name simple-web -p 80:5000 ${dockerImage}"
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    def dockerImage = 'zoe2512/simple-web'
                    // Login to DockerHub and push image
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                    // sh "docker login -u your-dockerhub-username -p ${DOCKERHUB_PASSWORD}"
                    // sh "docker push ${dockerImage}"
                    sh "docker login -u zoe2512 -p qwerty123"
                    sh "docker tag ${dockerImage} ${dockerImage}:latest"
                    sh "docker push ${dockerImage}"
                    }
                }
            }
        }
        
        /*stage('Deploy to Docker') {
            steps {
                agent {
                    label 'Docker_Sever_Pool'
                }
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
        stage('Email Notification') {
            steps {
                emailext (
                    to: 'nghihuynh7022@gmail.com',
                    subject: 'CI/CD Notification',
                    body: "Deployment of Flask app was ${currentBuild.result}.",
                    mimeType: 'text/html',
                    attachLog: true,
                    recipientProviders: [[$class: 'CulpritsRecipientProvider']]
                )
            }
        }
    }
    
    post {
        success {
            echo "Deployment successful"
        }
        failure {
            echo "Deployment failed"
        }*/
    }
}
