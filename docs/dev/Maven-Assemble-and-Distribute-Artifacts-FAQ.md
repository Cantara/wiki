# Maven Assemble and Distribute Artifacts FAQ

## Table of Contents

---

#### How to assemble an application

The official docs should be sufficient, see the [maven-assembly-plugin](http://maven.apache.org/plugins/maven-assembly-plugin/). If applicable, prefer to use the predefined descriptors.

###### Example: How to create an executable jar with all run-time dependencies included

See the [jar-with-dependencies](http://maven.apache.org/plugins/maven-assembly-plugin/descriptor-refs.html#jar-with-dependencies) descriptor. 
For your convenience a working configuration is shown below: 

```
<properties>
  <packageName>no.objectware.projectName</packageName>
  <mainClass>${packageName}.MainClassName</mainClass>
</properties>
<build>
  <plugins>
     <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-assembly-plugin</artifactId>
        <version>2.2-beta-1</version>
        <configuration>
          <finalName>${pom.artifactId}</finalName>
          <descriptorRefs>
            <descriptorRef>jar-with-dependencies</descriptorRef>
          </descriptorRefs>
          <archive>
            <manifest>
              <mainClass>${mainClass}</mainClass>
              <packageName>${packageName}</packageName>
              <addClasspath>true</addClasspath>
            </manifest>
            <manifestEntries>
              <mode>development</mode>
            </manifestEntries>
          </archive>
        </configuration>
        <executions>
          <execution>
            <id>packageWithDependencies</id>
            <phase>package</phase>
            <goals>
              <goal>assembly</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
  </plugins>
</build>
```

###### Example: How to create an assembly with custom descriptor

1. Add a reference to an assembly descriptor.
```
<build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-assembly-plugin</artifactId>
        <version>2.2-beta-1</version>
        <configuration>
          <descriptor>src/main/assembly/assemblydescriptor.xml</descriptor>
        </configuration>
        <executions>
          <execution>
            <id>createBinaryArchive</id>
            <phase>package</phase>
            <goals>
              <goal>assembly</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
```

1. Create an assembly descriptor
    - See [descriptor-refs](http://maven.apache.org/plugins/maven-assembly-plugin/descriptor-refs.html)
    - See [advanced-descriptor-topics](http://maven.apache.org/plugins/maven-assembly-plugin/advanced-descriptor-topics.html)

#### [How to use a zip file to share resources between projects](How-to-use-a-zip-file-to-share-resources-between-projects.md)? 

See [How to use a zip file to share resources between projects](How-to-use-a-zip-file-to-share-resources-between-projects.md)

#### How to deploy to an application container?

Do not confuse deploy to an application container with Maven's deploy phase. _Maven deploy_ means installing an artifact in a non-local Maven repository (e.g. the company repository). The typical use case for this kind of setup is if you want to deploy the application in a testing environment to allow others to test the newest development version of the application.
1. Copy the application manually or use the [maven-antrun-plugin](http://maven.apache.org/plugins/maven-antrun-plugin/) with the copy task.
1. Use [Cargo](http://cargo.codehaus.org/Maven2+plugin)
    - If on tomcat; [tomcat-maven-plugin](http://mojo.codehaus.org/tomcat-maven-plugin/deployment.html) can be used as well.
1. Make the maven-war-plugin output the final war file to a folder that e.g. tomcat listens to.
```
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-war-plugin</artifactId>
  <configuration>
    <outputDirectory>/var/www/tomcatHome/app</outputDirectory>
  </configuration>
</plugin>
```
1. Run with custom scripts with [exec-maven-plugin](http://mojo.codehaus.org/exec-maven-plugin). See [Deploying to GlassFish using Maven2](http://technology.amis.nl/blog/?p=2495) for an example. 

#### [How to use Java WebStart](Maven-Webstart-static-website.md)

See [Maven Webstart - static website](Maven-Webstart-static-website.md)
