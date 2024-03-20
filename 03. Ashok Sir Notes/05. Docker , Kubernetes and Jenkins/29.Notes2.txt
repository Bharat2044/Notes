=================
What is Jenkins?
=================

=> Jenkins is an open source automation tool for CI and CD

=> Jenkins tool developed using Java

=> Jenkins is part of Hudson Project

=> Intially it is called as Hudson then later it renamed to Jenkins

=================
About CI CD
=================

=> CI and CD are two most frequently used terms in modern development practises and DevOps practises.

=> CI stands for Continuous Integration. It is fundamental DevOps best practise where developers frequently merge code changes to central repository where automated builds and tests runs.

=> CD means Continuous Delivery or Continous Deployment.

=> Jenkins is a self-contained, open-source automation server which can be used to automate all sorts of tasks related to building, testing, and delivering or deploying software.

==================================
Build & Deployment Process
==================================

1) Take latest source code from repository

2) Compile source code 

3) Execute Unit tests (Junits)

4) Perform Code Review

5) Package code as war file

6) Deploy the war file into server

Note: All the above build and deployment tasks can be automated using Jenkins tool.


==========================
Jenkins Installation:
===========================

1) Create an EC2 instance with Ubuntu AMI (t2.micro instance)

2) Connect to your EC2 instance using MobaXterm
 
3) Install Java In Ubuntu VM with below commands

$ sudo apt-get update

$ sudo apt-get install default-jre

4) Install Jenkins in Ubuntu VM with below commands

$ curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

$ echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

$ sudo apt-get update

$ sudo apt-get install jenkins

$ sudo systemctl status jenkins
 
5) Access Jenkins Server in browser using below URL

		URL : http://ec2-public-ip:8080/

	Note: Enable 8080 port in security group
 
6) Get the initial administrative password 

	$ sudo cat /var/lib/jenkins/secrets/initialAdminPassword

	pwd : 5fe6ddcc9db244cab6aca5ccf2d6a83a

-> Provide pwd which we have copied to unlock jenkins

-> Select "Install Suggested Plugins" card (it will install those plugins)

-> Create Admin account

===============================
Creating First Job in Jenkins 
===============================

1) Goto Jenkins Dashboard

2) Click on New Item

		-> Enter Item Name (Job Name)
		-> Select Free Style Project & Click OK
		-> Enter some description
		-> Click on 'Build' tab
		-> Click on 'Add Build Step' and select 'Execute Shell'

3) Enter below shellscript

echo "Hello Guys,"
touch ashokit.txt
echo "Hello Guys, Welcome to Jenkins Classes" >> ashokit.txt
echo "Done..!!"

4) Apply and Save

Note: With above steps we have created JENKINS Job

5) Click on 'Build Now' to start Job execution

6) Click on 'Build Number' and then click on 'Console Ouput' to see job execution details.


=> Jenkins Home Directory in EC2 : /var/lib/jenkins/workspace/

		$ cd /var/lib/jenkins/workspace/

7) Go to Jenkins home directory and check for the job name --> check the file created inside the job


