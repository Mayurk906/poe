pipeline {
    agent any
    environment {
        PY = 'D:\\poe\\venv\\Scripts\\python.exe'
    }
    stages {
        stage('Run App') {
            steps { bat '"%PY%" hello.py' }
        }
        stage('Test') {
            steps { bat '"%PY%" -m pytest -v --junitxml=report.xml' }
        }
        stage('Drift Check') {
            steps { bat '"%PY%" drift.py' }
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'report.xml'
            archiveArtifacts artifacts: 'drift_report.html', allowEmptyArchive: true
        }
    }
}
