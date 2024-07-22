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

    stage('Store Results in Database') {
            steps {
                script {
                    // Parse test results from Jenkins console output
                    def counts = sh(returnStdout: true, script: 'grep "passed\\|failed\\|skipped" $JENKINS_HOME/jobs/$JOB_NAME/builds/$BUILD_NUMBER/log | tail -n1')
                    
                    def passed = counts.take(1)
                    def failed = counts.take(2)
                    def skipped = counts.take(3)

                    // Insert results into MySQL database
                    sql = Sql.newInstance(env.DB_URL, env.DB_USER, env.DB_PASS, 'com.mysql.jdbc.Driver')
                    sql.execute("INSERT INTO test_results (passed, failed, skipped) VALUES (${passed}, ${failed}, ${skipped})")
                }
            }
        }
  }
}
