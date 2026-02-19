# Continuum 1.3.2 Installation Guide - Solaris

This guide explains how to install Continuum 1.3.2 on Solaris 10 and integrate with SMF. 
The are a lot of gotchas (see [CONTINUUM-2182](http://jira.codehaus.org/browse/CONTINUUM-2182), hopefully these will be fixed eventually. 

#### Install 
- Create a [new zone](New-zone-procedure.md)
- Add user 
```
export username=continuum
useradd -d /export/home/$username -s /usr/bin/bash -m $username
```
- Download and unzip 
```
mkdir -p /local/app/continuum
cd /local/app/continuum
wget http://mirrorservice.nomedia.no/apache.org/continuum/binaries/apache-continuum-1.3.2-bin.zip
unzip apache-continuum-1.3.2-bin.zip
ln -s apache-continuum-1.3.2-bin current 
```

- Fix start script 
    - fix parameters to tr according to [CONTINUUM-2181](http://jira.codehaus.org/browse/CONTINUUM-2181)
    - In **bin/continuum**
```
> RUNDIR=`dirname $0`

< WRAPPER_CMD="./wrapper"
> WRAPPER_CMD="$RUNDIR/wrapper"
< PIDDIR="."
> PIDDIR="$RUNDIR"
```
    - In **/conf/wrapper.conf** (fix "Address is already in use" error) 
below wrapper.java.mainclass=org.tanukisoftware.wrapper.WrapperSimpleApp 
```
> wrapper.port=1777
```

- Set up SMF 
Example manifest: [continuum-smf.xml](continuum-smf-xml.md)
```
vim /var/svc/manifest/application/continuum-smf.xml
svccfg -v validate /var/svc/manifest/application/continuum-smf.xml
svccfg -v import /var/svc/manifest/application/continuum-smf.xml
```

- Check that everything is OK and online
```
svcadm enable continuum
svcs -l continuum
prstat (continuum process is listed) 
point a browser to http://continuum-132.company.com:8080/continuum
```

#### Operation 

```
svcadm enable continuum
svcadm disable continuum
svcadm restart continuum
```

See [Solaris Service Management Facility](http://www.sun.com/bigadmin/content/selfheal/smf-quickstart.jsp#Stopping_starting_and_restarting_services)

#### Docs 

[Installing Continuum Standalone](http://continuum.apache.org/docs/1.3.2/installation/standalone.html) 
[LDAP Configuration](http://continuum.apache.org/docs/1.3.2/administrator_guides/security/ldap.html)
