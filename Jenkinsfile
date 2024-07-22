pipeline {
  agent any

  environment {
    // Consider using Jenkins Credentials Plugin for secure credential handling
    DB_URL = 'jdbc:mysql://localhost:3306/test_results_db'
    DB_USER = 'root'
    DB_PASS = 'Test@1234'
  }

  stages {
    stage('Checkout') {
      steps {
        // Checkout your repository using the configured Git installation
        git branch: 'main', url: 'https://github.com/Rachelphilipc/saucedemo.git'
      }
    }

    stage('Test') {
      steps {
        // Example: Build and execute your Python script
        sh 'python3 testcases.py'
      }
    }
  }
}
