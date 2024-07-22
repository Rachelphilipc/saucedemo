pipeline {
  agent any
  
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
        sh 'python3 testcases.py' > output.txt
      }
    }
    stage('Store it in a db') {
      steps {
        // Example: Build and execute your Python script
        sh 'python3 parsemydata.py'
      }
    }
  }
  post {
        always {
            archiveArtifacts artifacts: 'output.txt'
        }
    }
}
