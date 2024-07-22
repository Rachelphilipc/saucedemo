pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository using the configured Git installation
                git branch: 'main ', url: 'https://github.com/Rachelphilipc/saucedemo.git'
            }
        }
        
        // Additional stages for running tests, deployment, etc.
    }
}
