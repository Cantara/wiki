# Artifactory 2.0.x Installation Guide - Solaris

#### Install

- Create a [new zone ]
- Add user
- Download and unzip

- Fix start script (see [RTFACT-1601](http://issues.jfrog.org/jira/browse/RTFACT-1601) )

  Copy content from [artifactoryctl](/web/20161004191043/https://wiki.cantara.no/display/sysadm/artifactoryctl "artifactoryctl") into the *artifactoryctl* file

- Set SMF

  Copy content from [artifactory-smf.xml](/web/20161004191043/https://wiki.cantara.no/display/sysadm/artifactory-smf.xml "artifactory-smf.xml") into the *artifactory-smf.xm* file

- Check that everything is OK and online

  ```
  svcadm enable svc:/application/artifactory:artifactory
  svcs -x (no artifactory here)
  svcs -a | grep artifactory (online) 
  prstat (artifactory process is listed) 
  point a browser to http://artifactory-205.company.com:8081/artifactory
  ```

#### Operation

See [Solaris Service Management Facility](http://www.sun.com/bigadmin/content/selfheal/smf-quickstart.jsp#Stopping_starting_and_restarting_services)

#### Docs

[Installing Artifactory as Linux Service](http://wiki.jfrog.org/confluence/display/RTF/Installing+on+Un*x)   
[Upgrading Artifactory](http://wiki.jfrog.org/confluence/display/RTF/Upgrading+Artifactory)
