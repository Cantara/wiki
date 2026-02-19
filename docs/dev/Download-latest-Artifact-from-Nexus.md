# Download latest Artifact from Nexus

### Actual code to run
```
@Echo Off
rem Unclear to test on my repo which is empty. set BASE_URL=http://127.0.0.1/nexus/service/local/artifact/maven/redirect? 
set BASE_URL=http://repository.sonatype.org/service/local/artifact/maven/redirect?
set RELEASE_REPO=central-proxy
set SNAPSHOT_REPO=
set GROUP=log4j
set ARTIFACT=log4j
set VERSION=LATEST

set URL="%BASE_URL%r=%RELEASE_REPO%&g=%GROUP%&a=%ARTIFACT%&v=%VERSION%"
echo Url to be called: %URL%
call wget.exe --no-check-certificate  %URL%
if %errorlevel%==0 (
echo Downloaded ok from repo
) else (
echo Download failed
)

echo Done
```

### Bash example to fetch.
```
$version = xxxx
url="http://x.x.x.x:8081/nexus/service/local/artifact/maven/redirect?r=nnn&g=com.nnn.nn&a=nnnn&v=$version&e=zip"
  echo "#"
  echo "# Try to fetch from Snapshot repo for version: " $version " from " $url
  echo "#"
  WGET=`/usr/local/bin/wget $url --output-document=$releasefile`
  EXITCODE=$?
```

### Win code example
```
net stop UserAdministration
bin\wget -O UserAdministration-1.0-SNAPSHOT.jar "http://nexus:8080/nexus/service/local/artifact/maven/redirect?r=snapshots&g=net.whydah.iam&a=UserAdministration&v=1.0-SNAPSHOT&p=jar"
net start UserAdministration
```

| net stop | if runing as a service wrapper service |
| bin\wget | Using wget.exe to fetch |
| net start | if runing as a service wrapper service |
