pipeline {
    //agent { label "dev-server" }
    //agent { label "demo-agent"}
    agent any
    stages{
        stage("code clone") {
            steps{
                echo "code cloning"
                git url: "https://github.com/deepak-dj/Ashish-APi.git", branch: "master"
            }
        }
        stage("code build") {
            steps{
                echo "code building"
                sh "docker build -t ashish-app ."
            }
        }
        stage("code push") {
            steps{
                echo "code pushing"
                withCredentials([usernamePassword(credentialsId: 'docker-id', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    sh "docker login -u ${env.user} -p ${env.pass}"
                    echo "Docker login successful"
                    sh "docker tag ashish-app:latest ${env.user}/ashish-app:latest"
                    sh "docker push ${env.user}/ashish-app:latest"
                }
                
            }
        }
        stage("code deploy") {
            steps{
                echo "code depolying"
                sh "docker compose down && docker compose up -d"
            }
        }
    }
}
