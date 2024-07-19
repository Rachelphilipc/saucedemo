pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    sh 'python -m unittest discover -s tests -p "saucedemo.py" --junitxml=test-results.xml'
                }
            }
        }
    }

    post {
        always {
            // Here you can perform cleanup or additional actions
            echo 'Always executed'
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
