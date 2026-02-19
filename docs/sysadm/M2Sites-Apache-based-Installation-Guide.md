# M2Sites - Apache-based Installation Guide

Apache 2 as installed by default in Solaris. This guide will be based on Solaris. It should be trivial to follow for other platforms. 

###### Create default configuration 

```
cd /etc/apache2/
mkdir sites-enabled
mkdir sites-available
cp httpd.conf-example httpd.conf
echo "include /etc/apache2/sites-enabled" >> httpd.conf
```

Modify {} with the following changes:

- Run as {}

User webservd
Group webservd

###### Set up vhosts
Create and edit `/etc/apache2/sites-available/m2sites.company.com`. 

Suggested content 
```
<VirtualHost *:80>
    ServerAdmin admin@company.com
    DocumentRoot /m2sites/
    ServerName m2sites.company.com
    ErrorLog /var/apache2/logs/m2sites.company.com-error_log
    CustomLog /var/apache2/logs/m2sites.company.com-access_log common
    <Directory /m2sites/>
        Options Indexes FollowSymLinks
    </Directory>
</VirtualHost>
```

Symlink in enabled sites:
```
cd /etc/apache2/sites-enabled/
ln -s ../sites-available/m2sites.company.com
```

Prepare folder for sites
```
mkdir -p /data/local/export/m2sites
chown -R webservd /data/local/export/m2sites
ln -s /data/local/export/m2sites m2sites
```

We use a symlink to easily switch file system path for the sites without affecting the DocumentRoot in the vhost or the clients which copy files to the server using scp. 

###### Start script

Enable the service
```
svcadm enable apache2
```
