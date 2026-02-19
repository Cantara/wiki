# Nexus Installation Guide - Amazon EC2

#### Amazon EC2 setup 

Instance type: [t1.micro](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts_micro_instances.html)
64-bit Amazon Linux AMi.
Separate EBS volume for storage, http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs<sub>~using</sub>~volumes.html

- Security group which allow incoming port 22, 80 and 443. 

###### Yum packages 

```
rpm -qa | grep openjdk
sudo yum remove  java-1.6.0-openjdk-1.6.0.0-66.1.13.1.62.amzn1.x86_64
sudo yum install java-1.7.0-openjdk.x86_64

sudo yum install nginx.x86_64
```

#### Download and install 

- http://nexus.sonatype.org/using/download.html
- http://books.sonatype.com/nexus-book/reference/install.html

```
sudo adduser nexus
wget www.sonatype.org/downloads/nexus-2.11.2-03-bundle.tar.gz
tar xvzf nexus-2.11.2-03-bundle.tar.gz
sudo mv nexus-2.11.2-03 /opt/
sudo ln -s nexus-2.11.2-03/ nexus 
sudo mv sonatype-work /data/
sudo chown nexus:nexus nexus-2.11.2-03 -R 
sudo chown nexus:nexus /data -R 
cd /opt 
sudo ln -s /data/sonatype-work sonatype-work
```

- Set up as service 
```
sudo cp nexus/bin/nexus /etc/init.d/nexus
sudo update-rc.d nexus defaults
sudo service nexus start
tail -200f /data/sonatype-work/nexus/logs/nexus.log 
```

#### Configure 

- Follow http://www.giorgiozamparelli.com/private<sub>~maven</sub><sub>repository</sub><sub>install</sub><sub>nexus</sub><sub>on</sub><sub>aws</sub><sub>ec2</sub>~amazon-linux/

- sonatype-work dir should reside on /data (the second EBS volume) 

Set up backup for this directory. 

Tip: Override default location for proxy repositories to avoid taking backup of these. 

#### Configure Apache or NginX as reverse proxy 

- [http://books.sonatype.com/nexus<sub>~book/reference/install</sub><sub>sect</sub><sub>service.html](http://books.sonatype.com/nexus</sub><sub>book/reference/install</sub><sub>sect</sub>~service.html) 

###### Apache2 

Baseurl: http://tools.company.no/nexus/

```
<VirtualHost *:80>
       ServerName tools.company.no
       Redirect / https://tools.company.no/
</VirtualHost>

<VirtualHost *:443>
        ServerName tools.company.no
        RequestHeader set X-Forwarded-Proto "https"

        SSLEngine On
        SSLCertificateFile /etc/apache2/ssl/tools.crt
        SSLCertificateKeyFile /etc/apache2/ssl/tools_ssl.key
        SSLCACertificateFile /etc/apache2/ssl/startssl_sub.class1.server.ca.pem

        SSLProtocol All -SSLv2 -SSLv3
        #Even higher security https://www.digicert.com/ssl-support/ssl-enabling-perfect-forward-secrecy.htm
        SSLHonorCipherOrder on
        #No RC4
        SSLCipherSuite "EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384 EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256 EECDH+aRSA+RC4 EECDH EDH+aRSA RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS !RC4"

        #books.sonatype.com/nexus-book/reference/install-sect-proxy.html
        ProxyPass /nexus http://localhost:8081/nexus
        ProxyPassReverse /nexus http://localhost:8081/nexus
        ProxyPassReverseCookiePath / /nexus
</VirtualHost>
```

###### Configure NginX as reverse proxy (nginx.conf)

nexus<sub>~webapp</sub>~context-path=/

```
server {
                listen              80 default_server;
                server_name         mvnrepo.cantara.no;
                access_log  /var/log/nginx/nexus_access.log;
                error_log   /var/log/nginx/nexus_error.log;
                location / {
                        proxy_pass http://localhost:8081;
                        proxy_set_header Host $host;
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header X-Forwarded-for $remote_addr;
                        #port_in_redirect off;
                        #proxy_redirect http://mvnrepo.cantara.no:8081/nexus /;
                        proxy_connect_timeout 300;
                }
        }
```

###### Make it secure 
[Post<sub>~install checklist](http://www.sonatype.com/books/nexus</sub><sub>book/reference/install</sub><sub>sect</sub><sub>repoman</sub><sub>post</sub>~install.html)

#### User and role management 

 

#### Resources 

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html

http://www.giorgiozamparelli.com/private<sub>~maven</sub><sub>repository</sub><sub>install</sub><sub>nexus</sub><sub>on</sub><sub>aws</sub><sub>ec2</sub>~amazon-linux/

https://gist.github.com/cedricwalter/1636020
