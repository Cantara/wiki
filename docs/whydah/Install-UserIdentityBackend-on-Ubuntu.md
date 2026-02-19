# Install UserIdentityBackend on Ubuntu

This is how to install UserIdentityBackend on Ubuntu

### Prerequisites 
1. Set up an ubuntu server, tested on Ubuntu 13.10.
1. Firewall rules - To harden the server, source limitations of UIB access to only where the ssologinservice, securitytokenservice and useradministration is being hosted.
1. JDK 7 (OpenJDK)
```
sudo apt-get install openjdk-7-jre
```
1. Apache or NginX as webproxy 
1. [ApacheDS](http://directory.apache.org/apacheds/download/download-linux-deb.html)
    1. http://opendesignarch.blogspot.no/2012/12/download-and-install-ldap-on-ubuntu.html 
1. PostgreSQL
    1. [How To Install and Use PostgreSQL on Ubuntu 12.04](https://www.digitalocean.com/community/articles/how-to-install-and-use-postgresql-on-ubuntu-12-04)
    1. [cantaraadm:Setup Postgres database for Confluence](../cantaraadm/Setup-Postgres-database-for-Confluence.md)

### Configuration 

### Install UIB 
```
sudo adduser UserIdentityBackend

# As the correct user
sudo su - UserIdentityBackend

# Download and update configuration file
wget https://raw.github.com/altran/Whydah-UserIdentityBackend/master/src/main/resources/useridentitybackend.PROD.properties
nano useridentitybackend.PROD.properties

# Download startup-script for the service
wget https://raw.github.com/altran/Whydah-UserIdentityBackend/master/start-service.sh
chmod 550 start-service.sh

# Start the service
./start-service.sh

```

### Security 

UIB, webproxy 
postgres, apacheds 

All services run as separate, non-root users. 

Suggest require SSH tunnel to access database and LDAP. Only allow direct connection from localhost.
