pipeline {
    environment {
        dockerImage = 'zoe2512/simple-web'
        containerName = 'simple-web'
    }
    agent none
    stages {

        stage('Git Checkout') {
            agent {
                label 'master'
            }
            steps {
                git 'https://github.com/ZK2207/jenkins.git'
            }
        }

        stage('Build Docker Image') {
            agent {
                label 'master'
            }
            steps {
                git 'https://github.com/ZK2207/jenkins.git'
                script {
                    echo "### Remove unsed images"
                    sh "docker image prune -af"

                    echo "### Display Dockerlile"
                    sh "cat Dockerfile"

                    echo "### Build Docker image"
                    sh "docker build -t ${dockerImage} ."
                    sh "docker image ls"
                }
            }
        }
        stage('Deloy Simple Web in Local') {
            agent {
                    label 'Local_Pool' // Docker_Local_01
                }
            steps {
                script {
                    echo "### Remove existing container"
                    sh "docker rm -f ${containerName}"

                    echo "### Pull and run Docker container"
                    sh "docker run -d --name simple-web -p 80:5000 ${dockerImage}"
                    sh "docker ps -a"
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            agent {
                label 'master'
                }
            steps {
                script {
                    sh "docker login -u zoe2512 -p qwerty123"
                    sh "docker tag ${dockerImage} ${dockerImage}:latest"
                    sh "docker push ${dockerImage}"
                    sh "docker image prune -af"
                }
            }
        }
        
        stage('Deploy Simple Web in Server') {
            agent {
                label 'Server_Pool' // Docker_Server_01
            }
            steps {
                script {
                    echo "### Remove existing container"
                    sh "docker rm -f ${containerName}"

                    echo "### Pull and run Docker container"
                    sh "docker pull ${dockerImage}"
                    sh "docker run -d --name simple-web -p 80:5000 ${dockerImage}"
                    sh "docker ps -a"
                }
            }
        }
        stage('Email Notification!!') {
            agent {
                label 'master'
            }
            steps {
                echo "### Sending Email..."
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
