pipeline
{
	agent {
		label 'aws-slave-label'
	}

	stages{
		stage('fetch the code'){
            steps{
                git branch: 'main', url: 'https://github.com/sravanre/python_Webservers.git'
            }
        }
		
		// stage('check the existing port is free '){
		// 	steps{
		// 		sh ''' netstat -tulpn | grep 5000
		// 		'''
		// 	}
		// }
		
		stage('build the image from the code'){
			steps{
				sh '''sudo docker ps
					  sudo docker images					  
					  sudo docker build -t new_pythonflaskapp_sravan .
					  sudo docker images
					  sudo docker run -d --name myflaskapp -p 5000:5000 new_pythonflaskapp_sravan
					'''
				}
			}
			
		stage('IP of the machine'){
			steps{
				sh '''
					curl http://checkip.amazonaws.com
					'''
				}
			}
	}
}