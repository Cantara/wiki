# Jenkins Installation Guide - Docker

###### Install and configure Docker 

See [sysadm:Nexus Installation Guide - Docker](../sysadm/Nexus<sub>~Installation</sub>~Guide-Docker.md)

###### Config steps 

```
# Create file location outside docker container
sudo mkdir /var/jenkins
copy [^Dockerfile] to present directory on server
docker build -t stig/jenkins .
docker run -d -p 8080:8080 -e "JENKINS_OPTS=--prefix=/jenkins" --name jenkins -u root -v /var/jenkins:/var/jenkins_home stig/jenkins

Hvis plugins ikke vises: Plugins -> Advanced -> Check now
alt:
http://stackoverflow.com/questions/16213982/unable-to-find-plugins-in-list-of-available-plugins-in-jenkins

```

#### Create your own Certificate:
sudo openssl req -new -x509 -nodes -out synaptic.no.crt -keyout synaptic.no.key
Note that the expiry may be as little as 1 month!

Build code:
https://github.com/SynapticTechnologies/Synaptic-Provisioning

#### References
- https://registry.hub.docker.com/_/jenkins/
- http://serialized.net/2013/04/simply<sub>~generating</sub><sub>self</sub><sub>signed</sub><sub>ssl</sub><sub>certs</sub>~with-ansible/
