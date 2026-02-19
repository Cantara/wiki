# Maven Deploy and Release FAQ

## Table of Contents

---

#### How to ensure all sub-modules use the same version in a multi-module reactor? 

Set the autoVersionSubmodules to true. 
```
<plugin>
    <artifactId>maven-release-plugin</artifactId>
    <version>2.3.2</version>
    <configuration>
        <autoVersionSubmodules>true</autoVersionSubmodules>
    </configuration>
</plugin>
```

Docs: http://maven.apache.org/plugins/maven-release-plugin/prepare-mojo.html#autoVersionSubmodules

#### How to cut a release?
See official documentation; [Release guide](http://maven.apache.org/guides/mini/guide-releasing.html) and [plugin documentation](http://maven.apache.org/plugins/maven-release-plugin/)
1. Make sure no dependencies or plugins use SNAPSHOT versions.
1. Set up distributionManagement
```
<build>
    <extensions>
      <extension>
        <groupId>org.apache.maven.wagon</groupId>
        <artifactId>wagon-webdav</artifactId>
        <version>1.0-beta-2</version>
      </extension>
    </extensions>
    <!--necessary due to http://jira.codehaus.org/browse/MRELEASE-271 -->
    <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-release-plugin</artifactId>
          <configuration>
            <preparationGoals>clean install</preparationGoals>
          </configuration>
        </plugin>
      </plugins>
  </build>

  <distributionManagement>
    <repository>
      <id>libs-releases</id>
      <name>Objectware Internal Release Repository</name>
      <url>dav:${releaseRepoUrl}</url>
    </repository>
    <snapshotRepository>
      <id>libs-snapshots</id>
      <name>Objectware Internal Snapshot Repository</name>
      <url>dav:${snapshotRepoUrl}</url>
    </snapshotRepository>
  </distributionManagement>

  <properties>
    <repoUrl>http://repo.objectware.no/artifactory</repoUrl>
    <releaseRepoUrl>${repoUrl}/libs-releases</releaseRepoUrl>
    <snapshotRepoUrl>${repoUrl}/libs-snapshots</snapshotRepoUrl>
  </properties>
```
1. Check out a copy of the source code with the protocol used in the scm element and run _mvn clean install_ to make sure you have all dependencies in the local .m2 repository.
1. Do a dry run, to check that everything seems ok:
```
mvn release:prepare -DdryRun=true
mvn release:clean
```
1. Do the actual release ( (!) Your [Subversion commandline client](What-do-I-need-to-do-to-get-mvn-release-to-work-on-Windows.md) version must be 1.6.5 or greater because of [this bug](http://subversion.tigris.org/issues/show_bug.cgi?id=3119).)
```
mvn release:prepare
mvn release:perform
```

#### What to do when a release fails? 

1. Try reverting changes automatically with _mvn release:rollback_. 

2. If 1 doesn't work, manual cleanup is needed. Run _mvn release:clean_ first to delete files created by the release-plugin. Next, check the version control system and the maven repo for changes and revert them if necessary.  

#### What do I need to do to get mvn release to work on Windows?

- Install commandline client 
    - [svn-win32-1.6.6.zip](http://subversion.tigris.org/files/documents/15/46880/svn-win32-1.6.6.zip) or similar (see [CollabNet Subversion Downloads](http://www.collab.net/downloads/subversion/), [Slik SVN](http://www.sliksvn.com/en/download/)) 

- Set up ssh keys if site-deploy use scp (and is not disabled) 
    - [Subversion / TortoiseSVN SSH HowTo](http://tortoisesvn.net/ssh_howto), see section _SSH key generation and connection check (client)_. 

#### How to cut a release when a dependency has not been released yet? 

See http://www.sonatype.com/people/2009/01/best-practices-for-releasing-with-3rd-party-snapshot-dependencies/ for aa thorough description of the different alternatives. This is the same solution, but we have added example commands to illustrate the process. 

1. Change the _version_ (not artifactId or groupId) to something that clearly explains that this is a workaround to be able to perform a release with a dependency on a snapshot. The [versions-maven-plugin](http://mojo.codehaus.org/versions-maven-plugin) is useful: 

`mvn versions:set -DnewVersion=4.0-companyName-r<scmRevisionNumber>`

2. Add authentication information to settings.xml. The id _plugins-releases_ must be added to the servers section with username and password.  

3. Deploy to _altDeploymentRepository_: 
```
mvn deploy -DupdateReleaseInfo=true -DaltDeploymentRepository=plugins-releases::default::http://repo.objectware.no/artifactory/plugins-releases/
```

#### How to deploy 3rd party artifacts to a DAV repository? 

wagon-webdav extension is required to deploy to a DAV repository. It is therefore necessary to create a temporary pom.xml to able to perform _deploy-file_. 

**Temporary pom.xml**: 
```
<project>
   <modelVersion>4.0.0</modelVersion>
   <groupId>com.example</groupId>
   <artifactId>webdav-deploy</artifactId>
   <packaging>pom</packaging>
   <version>1</version>
   <name>Webdav Deployment POM</name>
   
   <build>
      <extensions>
         <extension>
            <groupId>org.apache.maven.wagon</groupId>
            <artifactId>wagon-webdav</artifactId>
            <version>1.0-beta-2</version>
         </extension>
      </extensions>
   </build>
</project>
```

**Command**:
```
mvn deploy:deploy-file -Dfile=myproject-1.0.jar -DrepositoryId=myrepo
-Durl=dav:https://server/dav/url
-DgroupId=no.objectware -DartifactId=myproject -Dversion=1.0 -Dpackaging=jar
```

#### How to use deploy (and site-deploy) on Windows? 

See [Maven, Windows and Deploying to a Remote Location](http://ekawas.blogspot.com/2007/02/maven-windows-and-deploying-to-remote.html) 

#### How do I skip tests when preparing a release?

You need to pass the test argument as a system variable when Maven forks the thread to perform the tests like this:

```
mvn release:perform -Darguments=-Dmaven.test.skip=true
```

#### How can I skip site-deploy (or a exclude a certain plugin) when I do a release?
This is workaround that allows cutting a release even though reporting-plugins fail (e.g. clirr). 

```
mvn release:perform -Dgoals=deploy 
```

#### Which distribution mechanisms are common for site-deploy? 

File, scp and scpexe are common ways to distribute the site. 

```
<distributionManagement>
    <site>
      <id>site</id>
      <url>${siteUrl}</url>
    </site>
</distributionManagement>
```

**[File](http://maven.apache.org/wagon/wagon-providers/wagon-file/index.html)**: Works almost always, but will only "deploy" the site locally.  
    - Example url: <siteUrl>file:///var/www/html/sites</siteUrl>

**[scp](http://maven.apache.org/wagon/wagon-providers/wagon-ssh/index.html)**: Java implementation of scp based on [JSCh](http://www.jcraft.com/jsch/). 
    - Example url: <siteUrl>scp://m2sites.company.com/var/www/html/sites</siteUrl>

**[scpexe](http://maven.apache.org/wagon/wagon-providers/wagon-ssh-external/)**: Use external implementation of SSH. This can be more troublesome to set up on Windows, but works in general better than scp (at least on Unix systems :P). 

See [Wagon Providers](http://maven.apache.org/wagon/wagon-providers/) for other distribution providers. 

> 📝 If file protocol is set in site distributionManagement, the site for the release is lost unless the release is run from the server which hosts the sites. This problem should (IMHO) be possible to remedy by overriding the property commandline, but this doesn't seem to be supported yet according to [MSITE-295](http://jira.codehaus.org/browse/MSITE-295). 

#### How to authenticate when using site-deploy? 

See the official docs for the [<servers> element](http://maven.apache.org/settings.html#Servers) for more information. Some examples follow below. Note that username/password and privatekey/passphrase schemes are mutually exclusive. 

###### Username and password in settings.xml 

```
  <servers>
    <server>
      <id>site</id>
      <username>user</username>
      <password>pass</password>      
      <filePermissions>664</filePermissions>
      <directoryPermissions>775</directoryPermissions>
      <configuration></configuration>
    </server>
  </servers>
```

###### Use SSH-keys 
```
  <servers>
    <server>
      <id>site</id>
      <username>user</username>      
      <privateKey>${user.home}/.ssh/id_dsa</privateKey>
      <passphrase>passphrase</passphrase>
      <filePermissions>664</filePermissions>
      <directoryPermissions>775</directoryPermissions>
      <configuration></configuration>
    </server>
  </servers>
```

Linux: [OpenSSH Public Key Authentication](http://sial.org/howto/openssh/publickey-auth/) 

Windows with Putty: [Public Key Authentication With PuTTY](http://www.ualberta.ca/CNS/RESEARCH/LinuxClusters/pka-putty.html)
Windows with Tortoise: **TODO** 

**TODO**: Verify that these recipes are complete and work properly. 

#### How to "release" to Maven artifact repository using Maven Ant Tasks

Sometimes you need to deploy artifacts from non-Maven projects to a Maven repository. This is how to do it with Ant.

###### Installing Maven Ant Task
1. Download Maven Ant Task jar-file, and place it in your Ant lib-folder.
1. Add namespace to project element in build-file: 
```
<project ... xmlns:artifact="antlib:org.apache.maven.artifact.ant">
```

See http://maven.apache.org/ant-tasks/installation.html

###### Deploy file with classified attachments

```
<?xml version="1.0" encoding="UTF-8"?>
<project name="AntTest" basedir="." xmlns:artifact="antlib:org.apache.maven.artifact.ant">

  ...

  <target name="deploy-app">
    <artifact:install-provider artifactId="wagon-webdav" version="1.0-beta-2"/>
    <artifact:pom id="my-pom" file="${basedir}/pom.xml"/>

    <artifact:deploy file="${basedir}/src/myApplication.jar">        
      <attach file="${basedir}/src/myApplication-sources.jar" type="jar" classifier="src"/>
      <attach file="${basedir}/src/myApplication-docs.jar" type="jar" classifier="docs"/>
      <remoteRepository url="http://nexus.mysite.com/nexus/content/repositories/releases/"/>
      <pom refid="my-pom"/>
    </artifact:deploy>
  </target>
</project>
```

```title
<?xml version="1.0" encoding="UTF-8"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd" 
  xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.colorline.accounting</groupId>
  <artifactId>myApplication</artifactId>
  <version>0.0.1</version>
  <packaging>jar</packaging>
</project>
```
