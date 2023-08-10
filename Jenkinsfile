pipeline {
    agent none
    stages {
        stage('Checkout code Build Docker Image') {
            agent {
                label 'master'
            }
            steps {
                git 'https://github.com/ZK2207/jenkins.git'
                script {
                    sh "docker image prune -af"
                    def dockerImage = 'zoe2512/simple-web'
                    // Build Docker image
                    docker.image('python:3.8-slim').inside {
                        sh "docker build -t ${dockerImage} ."}
                }
            }
        }
        stage('Testing in Local') {
            agent {
                    label 'Local_Pool'
                }
            steps {
                script {
                    def dockerImage = 'zoe2512/simple-web'
                    def containerName = 'simple-web'
                    
                    // Remove existing container (if any)
                    sh "docker rm -f ${containerName}"
                    
                    // Pull and run Docker container
                    sh "docker run -d --name simple-web -p 80:5000 ${dockerImage}"
                }
            }
        }
        stage('Push Docker Image') {
            agent {
                label 'master'
                }
            steps {
                script {
                    def dockerImage = 'zoe2512/simple-web'
                    sh "docker login -u zoe2512 -p qwerty123"
                    sh "docker tag ${dockerImage} ${dockerImage}:latest"
                    sh "docker push ${dockerImage}"
                }
            }
        }
        
        stage('Deploy to Docker') {
            agent {
                label 'Server_Pool'
            }
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
        stage('Email Notification') {
            agent {
                label 'master'
            }
            steps {
                echo "Job Done"
            }
            post{
                always{
                    mail to: "nghihuynh7022@gmail.com",
                    subject: "CI/CD Notification",
                    body: "Deployment of Flask app was ${currentBuild.result}"
                }
            }
        }
    }
    
    post {
        success {
            echo "Deployment Successful"
        }
        failure {
            echo "Deployment Failed"
        }
    }
}
