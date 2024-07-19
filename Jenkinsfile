pipeline {
    agent any
    
    stages {
        stage('Install dependencies') {
            steps {
                script {
                    // Install required Python packages
                    sh 'pip install selenium webdriver-manager'
                }
            }
        }
        
        stage('Run Selenium tests') {
            steps {
                script {
                    // Run your Python script
                    sh 'python3 saucedemo.py'
                }
            }
        }
    }
    
    post {
        always {
            // Clean up steps if needed
        }
    }
}
