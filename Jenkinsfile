pipeline {
    agent any // Or a specific label if you have one

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/prakruti2729/ml-hello-world', branch: 'main' // Or your actual repo
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                   
                    def venvDir = "venv" // This will create a 'venv' directory in your workspace

                    
                    sh "python3 -m venv ${venvDir}"

                    
                    sh "bash -c'source ${venvDir}/bin/activate && pip install -r requirements.txt'"
               
                }
            }
        }
        stage('Train Model') {
                steps {
                    script {
                        def venvDir = "venv"
                        
                        sh ""bash -c 'source ${venvDir}/bin/activate && python train.py'"
                    }
                }
            }
        stage('Test Model') {
                steps {
                    script {
                        def venvDir = "venv"
                        // Activate the virtual environment and then run your script
                        sh ""bash -c 'source ${venvDir}/bin/activate && python test.py'"
                    }
                }
            }
            // ... other stages
		stage('Archive Model') {
        	steps {
         		archiveArtifacts artifacts: 'model.pkl', fingerprint: true
          }
        }
		
        
    }
}
