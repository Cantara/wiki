# Nexus Installation Guide - Docker

###### Install and configure Docker 

Install _lxc-docker_ according to [docs](https://docs.docker.com/installation/ubuntulinux/). 

- Suggest using _sudo_ instead of adding yourself to the docker group as suggested here: [dial unix /var/run/docker.sock: permission denied_ issue](https://github.com/docker/docker/issues/5314). 

###### Steps 

Use a _data volume container_ for persistence. 

```
sudo docker pull sonatype/nexus
sudo docker run -d --name nexus-data sonatype/nexus echo "data-only container for Nexus"
sudo docker run -d -p 8081:8081 --name nexus --volumes-from nexus-data --restart=on-failure:10 sonatype/nexus
```

- **TODO** Evaluate how to restart nexus at boot. 
    - [https://docs.docker.com/articles/host_integration/](https://docs.docker.com/articles/host_integration/)

- Follow the [Post<sub>~Install Checklist](http://books.sonatype.com/nexus</sub><sub>book/reference/install</sub><sub>sect</sub><sub>repoman</sub><sub>post</sub>~install.html)

###### Explore 

Check that you now have two containers. nexus-data container do not have to be running. 
```
sudo docker ps -a
```

```
curl http://localhost:8081/service/local/status
```

http://stackoverflow.com/questions/23405689/accessing<sub>~a</sub><sub>docker</sub><sub>containers</sub><sub>file</sub><sub>system</sub>~through-terminal

```
sudo docker exec -t -i nexus /bin/bash
```

###### Read more 
- https://registry.hub.docker.com/u/sonatype/nexus/
- [Persistent volumes with Docker - Data<sub>~only container pattern](http://www.tech</sub><sub>d.net/2013/12/16/persistent</sub><sub>volumes</sub><sub>with</sub><sub>docker</sub><sub>container</sub><sub>as</sub>~volume-pattern/)

#### Apache reverse proxy 

```
sudo a2enmod headers
```

```
<VirtualHost *:80>
       ServerName someIpHere
       Redirect / https://someIpHere/
</VirtualHost>

<VirtualHost *:443>
        ServerName someIpHere
        RequestHeader set X-Forwarded-Proto "https"

        SSLEngine On
        SSLCertificateFile /etc/apache2/ssl/some.no.crt
        SSLCertificateKeyFile /etc/apache2/ssl/some.no.key

        ProxyPass /jenkins http://localhost:8080/jenkins nocanon
        ProxyPassReverse /jenkins http://localhost:8080/jenkins
        ProxyRequests     Off
        AllowEncodedSlashes NoDecode
        #Doc: https://wiki.jenkins-ci.org/display/JENKINS/Running+Jenkins+behind+Apache

        #books.sonatype.com/nexus-book/reference/install-sect-proxy.html
        ProxyPass /nexus/ http://localhost:8081/
        ProxyPassReverse /nexus/ http://localhost:8081/
        ProxyPassReverseCookiePath / /nexus
</VirtualHost>
```
