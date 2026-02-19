# Confluence 3.5 - Amazon EC2

#### Amazon EC2 setup 

- AMI: Ubuntu Server 14.04 LTS (HVM), SSD Volume Type - ami-234ecc54
- Instance type: [t2.medium](http://aws.amazon.com/ec2/instance-types/), 2cpus, 4GiB memory
- Protect against accidental termination
- Separate 20GiB EBS volume for storage, http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

- Security group which allow incoming port 22, 80 and 443. 

###### Install java and postgresql

Atlassion recommends Oracle JDK 6. See https://confluence.atlassian.com/display/CONF35/Supported+Platforms and https://confluence.atlassian.com/display/CONFKB/Dashboard+is+not+rendering+properly. 

```
sudo locale-gen nb_NO.UTF-8 en_US.UTF-8
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java6-installer

sudo aptitude install postgresql-9.3
```

###### Database 

- [cantaraadm:Setup Postgres database for Confluence](../cantaraadm/Setup-Postgres-database-for-Confluence.md)

###### Install confluence 

3.5.17 is the last version before Atlassian removed the markup support. See [Why We Removed the Wiki Markup Editor in Confluence 4.0](http://blogs.atlassian.com/2011/11/why-we-removed-wiki-markup-editor-in-confluence-4/). 

https://www.atlassian.com/software/confluence/download-archives

```
sudo apt-get install libice-dev libsm-dev libx11-dev libxext-dev libxp-dev libxt-dev libxtst-dev
sudo useradd --create-home -c "Confluence role account" confluence
cd /opt
sudo wget https://www.atlassian.com/software/confluence/downloads/binary/confluence-3.5.17-std.tar.gz
sudo tar -xvvzf confluence-3.5.17-std.tar.gz
sudo ln -s confluence-3.5.17-std confluence
sudo chown confluence:confluence confluence -R

sudo vim confluence/confluence/WEB-INF/classes/confluence-init.properties 
wget https://jdbc.postgresql.org/download/postgresql-9.3-1103.jdbc4.jar 
sudo wget https://jdbc.postgresql.org/download/postgresql-9.3-1103.jdbc4.jar 
sudo cp postgresql-9.3-1103.jdbc4.jar confluence/confluence/WEB-INF/lib/
```

###### Move data 

```
sudo su - postgres 
/usr/postgres/8.3/bin/pg_dump confluence > /tmp/dump.sql
sudo su - postgres 
psql -U postgres confluence < dump.sql
```

- move confluence-data 

###### Read more 

- http://ubuntuhandbook.org/index.php/2015/01/install-openjdk-8-ubuntu-14-04-12-04-lts/
- https://confluence.atlassian.com/display/DOC/Start+Confluence+Automatically+on+Linux
- https://confluence.atlassian.com/display/CONF34/Installing+Confluence+Standalone+on+UNIX+or+Linux
- https://confluence.atlassian.com/display/CONF35/Supported+Platforms
    - https://confluence.atlassian.com/display/CONFKB/Dashboard+is+not+rendering+properly
