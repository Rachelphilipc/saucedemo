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
                    
                    // Execute SQL query using jdbcStep
                    def sqlQuery = "INSERT INTO test_results (passed, failed, skipped) VALUES (${passed}, ${failed}, ${skipped})"
                    def sql = jdbcStatement(
                        credentialsId: 'your-db-credentials-id',  // Use Jenkins credentials plugin to store DB credentials
                        driver: 'com.mysql.jdbc.Driver',  // Specify your JDBC driver
                        url: env.DB_URL,
                        username: env.DB_USER,
                        password: env.DB_PASS,
                        sql: sqlQuery
                    )
                    
                    // Check for SQL execution status
                    if (sql.rowsAffected == 1) {
                        echo "Data inserted successfully into database."
                    } else {
                        error "Failed to insert data into database."
                    }
                    }
            }
        }
  }
}
