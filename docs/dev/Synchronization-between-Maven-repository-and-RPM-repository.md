# Synchronization between Maven repository and RPM repository

We assume that the rpm repository can be set up on the same host as the Maven repository. If this is not the case, use _rsync_ instead of _cp_ in the script below and use ssh to execute the _createrepo_ command on the remote host. 

#### Export files 
    - From JCR-based repositories (Artifactory)
        - Choose how often to synchronize and set up _backup_ from Artifactory to disk from the GUI. 
    - File system based repositories (Archiva, Nexus)
        - wget 

#### Add a script to cron which do the following 
```
#!/bin/bash

src=/path/to/artifactoryBackup
rpmRepo=/path/to/rpms

mkdir -p $rpmRepo

# Copy rpm files to the rpm repo folder 
find $src -name *.rpm | while read filename; do cp -u "${filename}" $rpmRepo; done

# Update rpm repo metadata
createrepo --update --checkts --pretty $rpmRepo
```

- Note! Files will be overwritten, if timestamps in src change between synchronizations. 

#### Set up a webserver to server the repo

A webserver needs to be running with the repo path as a part of the document root, for instance /var/www/html/repo.

**TODO**: Example apache config here

#### Add repo to yum clients

The yum repository needs to be added on the yum clients. On RH/CentOS 5 this is done by adding nameOfRepo.repo file under /etc/yum.repos.d/ containing something like
```
[nameOfRepo]
name=Name of Repo
baseurl=http://nameOfRepo.realurl.here/repo
```

You can then verify it by running `yum check-update` and `yum list recent` on the client
