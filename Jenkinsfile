pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // git branch: 'main', url: 'https://github.com/your-repo.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building project...'
                // Add build commands here, e.g., mvn package, npm install, etc.
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running tests...'
                // Add test commands here, e.g., mvn test, npm test, etc.
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deploying application...'
                // Add deployment commands here
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
