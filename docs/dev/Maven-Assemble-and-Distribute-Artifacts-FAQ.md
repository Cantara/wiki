# Maven Assemble and Distribute Artifacts FAQ

## Table of Contents

---

#### How to assemble an application

The official docs should be sufficient, see the [maven<sub>~assembly</sub><sub>plugin](http://maven.apache.org/plugins/maven</sub><sub>assembly</sub>~plugin/). If applicable, prefer to use the predefined descriptors.

###### Example: How to create an executable jar with all run-time dependencies included

See the [jar<sub>~with</sub><sub>dependencies](http://maven.apache.org/plugins/maven</sub><sub>assembly</sub><sub>plugin/descriptor</sub><sub>refs.html#jar</sub>~with-dependencies) descriptor. 
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
    - See [descriptor<sub>~refs](http://maven.apache.org/plugins/maven</sub><sub>assembly</sub><sub>plugin/descriptor</sub>~refs.html)
    - See [advanced<sub>~descriptor</sub><sub>topics](http://maven.apache.org/plugins/maven</sub><sub>assembly</sub><sub>plugin/advanced</sub><sub>descriptor</sub>~topics.html)

#### [How to use a zip file to share resources between projects](How<sub>~to</sub><sub>use</sub><sub>a</sub><sub>zip</sub><sub>file</sub><sub>to</sub><sub>share</sub><sub>resources</sub><sub>between</sub>~projects.md)? 

See [How to use a zip file to share resources between projects](How<sub>~to</sub><sub>use</sub><sub>a</sub><sub>zip</sub><sub>file</sub><sub>to</sub><sub>share</sub><sub>resources</sub><sub>between</sub>~projects.md)

#### How to deploy to an application container?

Do not confuse deploy to an application container with Maven's deploy phase. _Maven deploy_ means installing an artifact in a non-local Maven repository (e.g. the company repository). The typical use case for this kind of setup is if you want to deploy the application in a testing environment to allow others to test the newest development version of the application.
1. Copy the application manually or use the [maven<sub>~antrun</sub><sub>plugin](http://maven.apache.org/plugins/maven</sub><sub>antrun</sub>~plugin/) with the copy task.
1. Use [Cargo](http://cargo.codehaus.org/Maven2+plugin)
    - If on tomcat; [tomcat<sub>~maven</sub><sub>plugin](http://mojo.codehaus.org/tomcat</sub><sub>maven</sub>~plugin/deployment.html) can be used as well.
1. Make the maven<sub>~war</sub>~plugin output the final war file to a folder that e.g. tomcat listens to.
```
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-war-plugin</artifactId>
  <configuration>
    <outputDirectory>/var/www/tomcatHome/app</outputDirectory>
  </configuration>
</plugin>
```
1. Run with custom scripts with [exec<sub>~maven</sub><sub>plugin](http://mojo.codehaus.org/exec</sub><sub>maven</sub>~plugin). See [Deploying to GlassFish using Maven2](http://technology.amis.nl/blog/?p=2495) for an example. 

#### [How to use Java WebStart](Maven<sub>~Webstart</sub>~static-website.md)

See [Maven Webstart - static website](Maven<sub>~Webstart</sub>~static-website.md)
