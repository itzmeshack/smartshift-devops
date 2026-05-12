pipeline {

    // Run pipeline on any available Jenkins agent
    agent any

    stages {

        // Install Python dependencies
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        // Execute automated unit tests
        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        // Build Docker container image
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t smartshift-app .'
            }
        }
    }
}