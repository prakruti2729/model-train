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
                    // Define the path for your virtual environment
                    def venvDir = "venv" // This will create a 'venv' directory in your workspace

                    // 1. Create the virtual environment if it doesn't exist
                    sh "python3 -m venv ${venvDir}"

                    // 2. Activate the virtual environment and install dependencies
                    //    The 'source' command needs to be executed in the same shell as the pip command.
                    //    Therefore, we chain the commands using '&&'.
                    sh "source ${venvDir}/bin/activate && pip install -r requirements.txt"
                    // Optionally, if you still face the "externally-managed-environment" error here
                    // (which is unlikely inside a venv but good to be aware of),
                    // you can add --break-system-packages (NOT RECOMMENDED inside venv unless truly stuck)
                    // sh "source ${venvDir}/bin/activate && pip install -r requirements.txt --break-system-packages"
                }
            }
            stage('Train Model') {
                steps {
                    script {
                        def venvDir = "venv"
                        // Activate the virtual environment and then run your script
                        sh "source ${venvDir}/bin/activate && python train.py"
                    }
                }
            }
            stage('Test Model') {
                steps {
                    script {
                        def venvDir = "venv"
                        // Activate the virtual environment and then run your script
                        sh "source ${venvDir}/bin/activate && python test.py"
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
}
