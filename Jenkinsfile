pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --alluredir=reports/'
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh 'allure generate reports/ --clean -o allure-report'
            }
        }
    }
}