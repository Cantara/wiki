# MActor Downloads

We are trying to improve the distribution mechanism for MActor. Currently we are working on building RPMs using [unix-maven-plugin](http://mojo.codehaus.org/unix/unix-maven-plugin/) and [appassembler-maven-plugin](http://mojo.codehaus.org/appassembler/appassembler-maven-plugin). 

An early snapshot can be found here: [^mactor-rpm-2.1-1-SNAPSHOT.rpm](393507-mactor-rpm-2.1-1-SNAPSHOT.rpm). Note that licenses may not be correct! 

To test it: 

```
sudo su - 
wget http://wiki.cantara.no/download/attachments/393507/mactor-rpm-2.1-1-SNAPSHOT.rpm?version=1
rpm -ivh target/mactor-rpm-2.1-1-SNAPSHOT.rpm

/usr/local/mactor/bin/MActorGui

or 

/usr/local/mactor/bin/MActorCmd

```
