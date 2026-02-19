# Nexus Installation Guide - Linux

#### Download and install 

- http://nexus.sonatype.org/using/download.html
- http://books.sonatype.com/nexus-book/reference/install.html

#### Configure 

###### Set work-dir 
NEXUS_HOME = /opt/nexus 
vim $\/conf/plexus.properties to change work-dir from default. 

Set up backup for this directory. 

Tip: Override default location for proxy repositories to avoid taking backup of these. 

###### Add vhost to apache: 
```
#m2repo, for reference in pom.xml
<VirtualHost *>
        ServerName m2repo.abakus.no
        ProxyPreserveHost ON
        ProxyPass / http://localhost:8081/nexus/
        ProxyPassReverse / http://localhost:8081/nexus/
</VirtualHost>
#for access to the webapp
<VirtualHost *>
        ServerName nexus.abakus.no
        ProxyPreserveHost ON
        ProxyPass /nexus/ http://localhost:8081/nexus/
        ProxyPassReverse /nexus/ http://localhost:8081/nexus/
</VirtualHost>
```

###### Make it secure 
[Post<sub>~install checklist](http://www.sonatype.com/books/nexus</sub><sub>book/reference/install</sub><sub>sect</sub><sub>repoman</sub><sub>post</sub>~install.html)
