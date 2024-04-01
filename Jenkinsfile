pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from your Git repository
                git 'https://github.com/PreshitS/assessment4_1.git'
            }
        }
        
        stage('Install dependencies') {
            steps {
                // Install Python dependencies using pip
                sh 'pip install Flask'
            }
        }
        
        stage('Run Flask application') {
            steps {
                // Start the Flask application
                sh 'python pyapp.py &'
                
                // Wait for the application to start (adjust sleep time as needed)
                sleep 10
            }
        }
        
        stage('Run tests') {
            steps {
                // Run any tests you have for your Flask application
                sh 'pytest'
            }
        }
    }
    
    post {
        always {
            // Stop the Flask application after the pipeline finishes
            sh 'pkill -f "python pyapp.py"'
        }
    }
}
