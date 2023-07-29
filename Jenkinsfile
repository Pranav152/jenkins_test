pipeline {
    agent any

    stages {
        stage('Linting') {
            steps {
                script {
                    // Run pylint and capture the output
                    sh 'pylint --exit-zero ${PWD} > pylint-report.txt'
                    def pylintOutput = readFile('pylint-report.txt')
                    echo "Pylint Output: ${pylintOutput}"
                    def scoreLine = pylintOutput.readLines().find { it.startsWith('Your code has been rated at') }
                    echo "Pylint Score Original: ${scoreLine}"
                    // Extract the actual score from the output
                    def score = scoreLine ? scoreLine.split()[6].split('/')[0] as float : 0
                    echo "Pylint Score: ${score}"

                    // Check for warnings and score greater than 4
                    if (score > 4.0) {
                        echo "Pylint passed with a score above 4 and warnings."
                    } else {
                        echo "Pylint failed or returned a score of 4 or below, or no warnings were found."
                        error("Pylint score is not above 4 or no warnings were found. Pipeline failed.")
                    }
                }
            }
        }

        stage('Unit Tests') {
            steps {
                // Install Python dependencies (if needed)
                // sh 'pip install -r requirements.txt'

                // Run unit tests using the system's Python
                sh 'python3 -m unittest discover'
            }
        }

        stage('Code Coverage') {
            steps {
                // Install code coverage tool
                // Run unit tests with code coverage
                sh 'coverage run -m unittest discover tests'
                // Generate code coverage report
                sh 'coverage report'
            }
        }
    }

    post {
        always {
            // Collect static code analysis results with Warnings Next Generation plugin
            recordIssues enabledForFailure: true, tools: [
                pyLint(pattern: 'pylint-report.txt')
            ]
        }
    }
}
