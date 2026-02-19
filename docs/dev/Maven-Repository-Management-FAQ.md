# Maven Repository Management FAQ

## Table of Contents

---

#### How to use a build artifact repository manager? 

See [Repository Management](http://maven.apache.org/repository-management.html) for a description of the concept. See also [repository manager](http://www.sonatype.com/book/reference/repository-manager.html#) (Nexus centric). 

The maven repository can **replace** your existing repositories or it can be used in **addition to other repositories**. The first approach is recommended. 
 
#### One repo to rule them all

It is recommended to mirror the global central repositories. Please see http://maven.apache.org/guides/mini/guide-mirror-settings.html for details. This can be achieved with mirrors in settings.xml or by overriding central in the pom and only username and password in settings.xml. 
[Sonatype recommends the mirrorOf approach](http://www.sonatype.com/people/2009/02/why-putting-repositories-in-your-poms-is-a-bad-idea/), but there are situations where putting the repos in the pom is better. It is a trade-off, pick your poison ;)  

###### mirrorOf in settings.xml

```xml
<settings>
  <servers>
    <server>
      <id>company</id>
      <username>user</username>
      <password>pass</password>
    </server>
  </servers>
  <mirrors>
    <mirror>
      <id>company</id>
      <name>Objectware Maven Repository Manager</name>
      <url>http://artifactory.company.com/artifactory/repo</url>
      <mirrorOf>*</mirrorOf>
    </mirror>
  </mirrors>
</settings>
```

###### Example of profile-activated company repo settings

Insert the following into your pom.xml file:

```
    <properties>        
        <m2repoUrl>http://m2repo.company.no/repo</m2repoUrl>
    </properties>
    <repositories>
        <repository>
            <id>central</id>
            <url>${m2repoUrl}</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
        </repository>
    </repositories>
    <pluginRepositories>
        <pluginRepository>
            <id>central</id>
            <url>${m2repoUrl}</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
        </pluginRepository>
    </pluginRepositories>
```

and the following into **~/.m2/settings.xml**: 

```
<settings>
  <servers>
    <!-- Override central  -->
    <server>
       <id>central</id>
       <username>username</username>
       <password>password</password>
    </server>
    <!-- To use the profile -->     
    <server>
       <id>company</id>
       <username>username</username>
       <password>password</password>
    </server>
    <!-- See distributionManagement -->
    <server>
       <id>libs-releases</id>
       <username>username</username>
       <password>password</password>
    </server>
    <!-- See distributionManagement --> 
    <server>
       <id>libs-snapshots</id>
       <username>username</username>
       <password>password</password>
    </server>    
  </servers>
  <profiles>
    <profile>
      <id>company</id>
      <activation>
        <activeByDefault>false</activeByDefault>
     </activation>
      <repositories>
        <repository>
          <id>company<</id>
          <name>Company< M2 repo</name>
          <url>http://m2repo.company<.no/repo</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>ow</id>
          <name>Company< M2 repo</name>
          <url>http://m2repo.company.no/repo</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>
  </profiles>
</settings>
```

#### In **addition** to other repos
If you don't want to modify the pom.xml file, the repo can be used from a profile (defined in the previous section). You will then get access to artifacts that are not available from the repositories defined in the POM, but not take advantage of the proxy functionality. 

To use this profile: 

` mvn clean install -U -P company<` 

Set activeByDefault to _true_ use the profile permanently. 

#### How to allow Artifactory to proxy a https repository with self-signed SSL certificate? 
NOT FINISHED

1. Obtain certificate
    1. See [Obtaining remote SSL certificate](http://wiki.community.objectware.no/display/smidigtonull/Java+SSL+-+Keystores#JavaSSL-Keystores-ObtainingaremoteSSLcertificate) or just download [Maven Repository Management FAQ^maven-repository.dev.java.net.crt](Maven-Repository-Management-FAQ-maven-repository-dev-java-net-crt.md)
1. Install it in the JVM used by Artifactory
    1. Check if cacerts is present: ls -l $JAVA_HOME/jre/lib/security
    1. Add certificate
```
keytool -import -file /root/maven-repository.dev.java.net.crt -alias maven-repository.dev.java.net -keystore $JAVA_HOME/jre/lib/security/jssecacerts -storepass changeit
```
    1. Check that it was added
```
keytool -list -keystore $JAVA_HOME/jre/lib/security/jssecacerts -storepass changeit
```
 
1. Restart Artifactory
