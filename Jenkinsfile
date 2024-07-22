pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository
                git 'https://github.com/Rachelphilipc/saucedemo.git'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run your Python script
                sh 'testcases.py'
            }
        }
    }
    
    post {
        always {
            // Clean up or post-processing steps if needed
        }
    }
}
