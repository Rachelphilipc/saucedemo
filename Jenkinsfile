pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Rachelphilipc/saucedemo.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 testcases.py > output1.txt'
            }
        }

        stage('Store') {
            steps {
                sh 'python3 parsemydata.py'
                archiveArtifacts artifacts: 'output1.txt'
            }
        }
    }
}
