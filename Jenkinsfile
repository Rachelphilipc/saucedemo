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

        script {
          // Read the output file (optional, can be removed if not needed)
          // def testOutput = readFile('output.txt').trim()
          // echo "Test output: ${testOutput}"

          // Parse the test results (assuming your test script provides parsable output)
          def (passed, failed, skipped) = parseTestResults( /* parse logic based on your test output */ )  // Replace with your parsing logic

          // Get additional information
          def user = env.USER
          def buildName = env.BUILD_NUMBER
          def startTime = sh(returnStdout: true, script: 'date +"%Y-%m-%d %H:%M:%S"').trim()
          def endTime = sh(returnStdout: true, script: 'date +"%Y-%m-%d %H:%M:%S"').trim()
          def timeTaken = "${endTime} - ${startTime}"  // Calculate time difference

          // Update database with test results
          updateDatabase(user, buildName, startTime, endTime, timeTaken, 
                         // Assuming totalTests is available from your test script (or adjust calculation)
                         passed + failed + skipped, passed, failed, skipped, 
                         failed > 0 ? 'FAILED' : 'PASSED')
        }
      }
    }
  }
}

// Define functions for parsing test results (replace with your actual logic)
def parseTestResults(testOutput) {
  // Implement your parsing logic here to extract passed, failed, and skipped counts from the test output
  // This example assumes a simple format, modify it based on your actual output
  def passed = testOutput =~ /passed (\d+)/ ? Integer.parseInt(testOutput[0][1]) : 0
  def failed = testOutput =~ /failed (\d+)/ ? Integer.parseInt(testOutput[0][1]) : 0
  def skipped = testOutput =~ /skipped (\d+)/ ? Integer.parseInt(testOutput[0][1]) : 0
  return [passed, failed, skipped]
}

// Define function to update database (replace with your actual implementation)
def updateDatabase(user, buildName, startTime, endTime, timeTaken, totalTests, passed, failed, skipped, runStatus) {
  // Implement your database connection logic here
  // This example is a placeholder, replace it with your actual database connection and update query
  echo "User: ${user}, Build Name: ${buildName}, Start Time: ${startTime}, End Time: ${endTime}, Time Taken: ${timeTaken}, Total Tests: ${totalTests}, Passed: ${passed}, Failed: ${failed}, Skipped: ${skipped}, Run Status: ${runStatus}"
}
