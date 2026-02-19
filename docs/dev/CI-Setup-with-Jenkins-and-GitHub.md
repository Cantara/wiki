# CI Setup with Jenkins and GitHub

# Setup with Jenkins and GitHub
_Tested on Ubuntu 13.04 on a virual machine in azure_

## Requirements
- Git
- JDK and JRE 7
- Maven
- GitHub repository

## Installing Jenkins
https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins+on+Ubuntu

**Be sure to apply the package manager update or you'll end upp with an old Jenkins version**
	
	wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
	sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
	sudo apt-get update
	sudo apt-get install jenkins

	**If you get the error**:
	
	dpkg: error processing /var/cache/apt/archives/jenkins_1.523_all.deb (--unpack):
		trying to overwrite '/usr/share/jenkins/jenkins.war', which is also in package jenkins-common 1.480.3+dfsg-1~exp2 
 
	You need to force an overwrite*
	`sudo dpkg -i --force-overwrite /var/cache/apt/archives/jenkins_1.523_all.deb`
	
_If you wish to expose Jenkins on port 80, follow the steps explaining how to install apache proxy and forward 80->8080 (or use nginx proxy if you so prefer)._
\\
\\
## Configure Jenkins
**Setup Standard Security**

https://wiki.jenkins-ci.org/display/JENKINS/Standard+Security+Setup

**Verify configuration**
Go to Manage Jenkins -> Configure System
Verify that JDK, Maven and Git-installations are correct. 
_If any of them are missing, either install the missing tool or point Jenkins to the correct installation path._

**Install plugins**
Manage Jenkins -> Manage Plugins

- Install Maven Integration plugin
  This will enable the option of creating a new task that builds from the POM-file

- Install GitHub plugin
  This will enable you to pull the code from GitHub directly
\\

##### Generate ssh-key
If you have plans on using multiple GitHub repositories you will need to add one key for each project.
A general key for all repos won't work.
See the explanation here: http://blog.firmhouse.com/configuring-multiple-private-ssh-deploy-keys-in-jenkins-for-github-com
(if you've already added github.com as a known_host in ~/.ssh/known_hosts you need to remove that entry for this to work)

Log on as the jenkins-user on your system:
`sudo -i -u jenkins`

Generate a new ssh key-pair
`ssh-keygen -f ~/.ssh/id_rsa.projectname -t rsa -C "Project Name"`

Add it to ~/.ssh/config since you only wish to use it for github authorization:
```bash
Host github-projectname
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_rsa.projectname
        IdentitiesOnly yes
#The next repo you add might look like this:
#Host github-projectname22
#        HostName github.com
#        User git
#        IdentityFile ~/.ssh/id_rsa.projectname22
#        IdentitiesOnly yes

```
\\

##### Deploy Key on GitHub 
Use the public part of the key as a Deploy Key on GitHub. (id_rsa.git.pub)
1. Browse to the Github project 
1. Choose "Settings" (on the right hand side menu in your project)
1. Select "Deploy Keys" on the left hand menu
1. Add the public part of the key you just created - "title" can be anything ("Jenkins build" for example)
1. Save
\\

##### Verify ssh authentication 
Go back to the shell on your jenkins server and sudo in as the jenkins-user.
`sudo -i -u jenkins`
Verify that the keys are set up correct by typing
`git ls-remote -h ssh://git@github-projectname/user/project.git HEAD`
This will also add GitHub to known hosts.
\\

##### Add the new Job

**Create the job**
1. Log in to the web interface of your jenkins server.
1. Select New Job.
1. Select "Build a maven2/3 project".

**Configure the job**
1. Under "GitHub project", enter https://github.com/name/project/
1. Under "Source Code Management" select Git and enter Repository URL: **ssh://git@github-projectname/name/project.git**

Save the configuration, a new build should be started.
\\

## GitHub trigger
You can set up Jenkins to poll the GitHub repository for changes on a given interval - which is nice.
What is even better is the ability to add a post-push hook in GitHub that will automagically trigger a build in Jenkins whenever the repo has received changes.

**Configure Jenkins**
Go to **Build Triggers** under your project's configuration in Jenkins.
1. Enable polling by checking the box "Poll SCM" in the configuration of your Jenkins project.
 Enter "H * * * *" to poll once every hour, or change to another schedule, the important thing is that polling is enabled for this to work.
1. Enable "Build when a change is pushed to GitHub"

Try out the hook by simulating an update to the repo:
http://my-jenkins.company.com/git/notifyCommit?url=https://github.com/name/project
The page must display the message "Scheduled polling of Projectname"

**Enable the hook on GitHub**
1. Go to the Settings page on your repository.
1. Select Service Hooks -> Jenkins (Git plugin) - _(not the (GitHub plugin) see step 4)_
1. In the URL-field you simply need to specify the server name (and root directory if your context directory isn't at root level): http://my-jenkins.company.com/
1. **NB!** If you are using multiple deploy keys and have specified the github repo on the form ssh://git@github-project/name/project.git you need to use the Jenkins (GitHub plugin) and specify the complete URL to the hook on the form http://ci.company.com/git/notifyCommit?url=ssh://git@github-project/name/project
\\

## References

https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins+on+Ubuntu \\
https://wiki.jenkins-ci.org/display/JENKINS/Standard+Security+Setup \\
http://www.karan.org/blog/index.php/2009/08/25/multiple-ssh-private-keys \\ 
https://wiki.jenkins-ci.org/display/JENKINS/Git+plugin \\
http://kohsuke.org/2011/12/01/polling-must-die-triggering-jenkins-builds-from-a-git-hook/ \\
http://blog.firmhouse.com/configuring-multiple-private-ssh-deploy-keys-in-jenkins-for-github-com
