pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code repository
                checkout scm
            }
        }
        stage('Test') {
            steps {
                script {
                    // Set up virtual display if running headless
                    // For example: Xvfb :99 &
                    sh 'pip install -r requirements.txt'  // Install dependencies
                    sh 'python -m unittest discover -s tests -p "saucedemo.py" --junitxml=test-results.xml'  // Run tests and generate JUnit XML
                }
            }
        }
        stage('Publish HTML Reports') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'tests/reports',
                    reportFiles: 'index.html',
                    reportName: 'Test Results'
                ])
            }
        }
    }

    post {
        always {
            // Clean up steps if needed
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
