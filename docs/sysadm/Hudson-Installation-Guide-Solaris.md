# Hudson Installation Guide - Solaris

This guide explains how to install Hudson on Solaris 10 and integrate with SMF. This setup is based on [Paul Oswald's article](http://pauloswald.com/blog/article/29/hudson-solaris-smf-manifest) and use the built-in [Winstone servlet container](http://winstone.sourceforge.net/). 

#### Install 
- Create a [new zone](New-zone-procedure.md)
- Add user 
```
export username=hudson
useradd -d /export/home/$username -s /usr/bin/bash -m $username
```

- Download 
```
mkdir -p /local/app/hudson
cd /local/app/hudson
wget --no-check-certificate http://hudson.gotdns.com/latest/hudson.war
chown -R hudson:other /local/app/hudson
```

- Set up SMF 
Example manifest: [hudson-smf.xml](hudson-smf-xml.md)
```
vim /var/svc/manifest/application/hudson-smf.xml
svccfg -v validate /var/svc/manifest/application/hudson-smf.xml
svccfg -v import /var/svc/manifest/application/hudson-smf.xml
```

- Check that everything is OK and online
```
svcadm enable hudson
svcs -l hudson
prstat (hudson process is listed) 
point a browser to http://hudson.company.com:8080/hudson/
```

#### Operation 

```
svcadm enable hudson
svcadm disable hudson
svcadm restart hudson
```

See [Solaris Service Management Facility](http://www.sun.com/bigadmin/content/selfheal/smf-quickstart.jsp#Stopping_starting_and_restarting_services) for more information on scvadm. 

#### Docs 

[hudson.dev.java.net](https://hudson.dev.java.net/)
[Hudson Solaris SMF Manifest](http://pauloswald.com/blog/article/29/hudson-solaris-smf-manifest)
