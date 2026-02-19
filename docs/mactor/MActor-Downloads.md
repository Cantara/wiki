# MActor Downloads

We are trying to improve the distribution mechanism for MActor. Currently we are working on building RPMs using [unix<sub>~maven</sub><sub>plugin](http://mojo.codehaus.org/unix/unix</sub><sub>maven</sub><sub>plugin/) and [appassembler</sub><sub>maven</sub><sub>plugin](http://mojo.codehaus.org/appassembler/appassembler</sub><sub>maven</sub>~plugin). 

An early snapshot can be found here: [^mactor<sub>~rpm</sub><sub>2.1</sub><sub>1</sub><sub>SNAPSHOT.rpm](mactor</sub><sub>rpm</sub><sub>2</sub><sub>1</sub><sub>1</sub><sub>SNAPSHOT</sub>~rpm.md). Note that licenses may not be correct! 

To test it: 

```
sudo su - 
wget http://wiki.cantara.no/download/attachments/393507/mactor-rpm-2.1-1-SNAPSHOT.rpm?version=1
rpm -ivh target/mactor-rpm-2.1-1-SNAPSHOT.rpm

/usr/local/mactor/bin/MActorGui

or 

/usr/local/mactor/bin/MActorCmd

```
