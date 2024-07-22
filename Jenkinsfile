pipeline {
    agent any

    environment {
        DB_URL = 'jdbc:mysql://localhost:3306/test_results_db'
        DB_USER = credentials('root')  // Use Jenkins credentials plugin for secure credential handling
        DB_PASS = credentials('Test@1234')  // Replace 'root' and 'Test@1234' with your credential IDs
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository using the configured Git installation
                git branch: 'main', url: 'https://github.com/Rachelphilipc/saucedemo.git'
            }
        }
        
        stage('Build and Test') {
            steps {
                // Example: Build and execute your Python script
                sh 'python3 testcases.py > output.txt'  // Redirect output to a file
                
                // Read the output file
                def testOutput = readFile('output.txt').trim()
                echo "Test output: ${testOutput}"
                
                // Parse the test results
                def (passed, failed, skipped) = parseTestResults(testOutput)
                
                // Update database based on test results
                updateDatabase(passed, failed, skipped)
            }
        }
    }
}

def parseTestResults(testOutput) {
    def passed = testOutput =~ /passed (\d+)/ ? Integer.parseInt(testOutput[0][1]) : 0
    def failed = testOutput =~ /failed (\d+)/ ? Integer.parseInt(testOutput[0][1]) : 0
    def skipped = testOutput =~ /skipped (\d+)/ ? Integer.parseInt(testOutput[0][1]) : 0
    
    return [passed, failed, skipped]
}

def updateDatabase(passed, failed, skipped) {
    def dbParams = [
        url: 'jdbc:mysql://localhost:3306/test_results_db',
        user: root,
        password: Test@1234,
        driver: 'com.mysql.jdbc.Driver'
    ]
    
    def sql = Sql.newInstance(dbParams.url, dbParams.user, dbParams.password, dbParams.driver)
    
    try {
        // Insert test results into the database
        sql.execute("INSERT INTO test_results (passed_count, failed_count, skipped_count, build_number, build_timestamp) " +
                    "VALUES (${passed}, ${failed}, ${skipped}, '${env.BUILD_NUMBER}', NOW())")
    } catch (Exception e) {
        echo "Error executing SQL query: ${e.message}"
    } finally {
        // Close connection
        sql.close()
    }
}
