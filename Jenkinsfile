pipeline {
     agent any 
     stages {
       stage('Checkout') {
	  steps {
             git branch: 'main', url: 'https://github.com/prakruti2729/model-train.git'
        }
       }
       stage('Install Dependencies') {
         steps {
            sh 'pip install -r requirements.txt'
        }
      }
       stage('Train Model') {
         steps   {
            sh 'python3 train.py'
           }
       }
       stage('Test Model') {
        steps {
            sh 'python3 test.py'

          }
       }
       stage('Archive Model') {
        steps {
         archiveArtifacts artifacts: 'model.pkl', fingerprint: true
          }
        }
     }
}
