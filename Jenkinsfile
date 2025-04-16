pipeline {
    agent {
        docker {
            image 'python:3.10'
            
        }
    }

    stages {
        stage('Clone code') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install -r requirements.txt || true' // Bỏ qua nếu không có file
            }
        }

        stage('Run Python script') {
            steps {
                echo 'Running main.py...'
                sh 'python main.py'
            }
        }
    }
}
