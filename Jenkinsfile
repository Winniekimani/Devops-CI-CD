pipeline {
    agent any
        stage('Build') {
            steps {
                script {
                    sh """
                    cd ${WORKING_DIRECTORY}
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    """
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh """
                    cd ${WORKING_DIRECTORY}
                    source venv/bin/activate
                    python3 -m pytest
                    """
                }
            }
        }
    }

