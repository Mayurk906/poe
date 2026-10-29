pipeline {
    agent any
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Run App')  { steps { bat 'python hello.py' } }
        stage('Test')     { steps { bat 'python -m pip install pytest && python -m pytest -v -s' } }
    }
}