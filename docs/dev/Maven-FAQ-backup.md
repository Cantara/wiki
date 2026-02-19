# Maven FAQ - backup

## Howtos

#### How to convert an Ant project to Maven?

1. Change your build file to work with a file structure that adheres to the [Standard Directory Layout](http://maven.apache.org/guides/introduction/introduction<sub>~to</sub><sub>the</sub><sub>standard</sub>~directory-layout.html).
1. Ensure that your Ant tasks follows the [Build lifecycle](http://maven.apache.org/guides/introduction/introduction<sub>~to</sub>~the-lifecycle.html). The purpose of this process is identify  which tasks (if any) that are not covered by Maven's [Core plugins](http://maven.apache.org/plugins/index.html).
1. If you have build tasks not covered by the core plugins, search for plugins that can replace the Ant task. The [Mojo project](http://mojo.codehaus.org/) at Codehaus is a good place to start looking.
1. Ant tasks that you are unable to find a proper replacement for can be run by the [Antrun plugin](http://maven.apache.org/plugins/maven<sub>~antrun</sub>~plugin/). However, this option should only be used as a last resort or as a means to minimize the impact of switching to Maven.
1. Do the actual conversion
    1. Tag and branch in the version control system
    1. Create a new Maven project (the [archetype plugin](http://maven.apache.org/plugins/maven<sub>~archetype</sub>~plugin/) can be used to set up template projects quickly.
    1. Add dependencies
    1. Add code
    1. Add the necessary plugins
    1. Bugfix until it works properly

#### How to handle libraries that cannot be found in any public Maven repository?

- Download the artifact to local storage. (e.g. /tmp/)
- Add the dependency to pom.xml and run _mvn clean install_. If the dependency cannot be found, the output will display which command to run to install the artifact.
- Change the "<sub>~Dfile=path</sub><sub>to</sub><sub>your</sub>~artifact-jar" option to point to the downloaded artifact (e.g. /tmp/someArtifact.jar)

This will solve the problem for one user, on a single computer. A better solution is to deploy the artifact to, e.g., the company repository. See [Repository Management](http://maven.apache.org/repository-management.html) for details.

#### How to debug problems related to different versions of a dependency?

###### Alternative 1: Use the [maven<sub>~dependency</sub><sub>plugin](http://maven.apache.org/plugins/maven</sub><sub>dependency</sub>~plugin)

Display a the dependency tree directly in the console (requires the [apache<sub>~snapshot</sub>~repo](http://wiki.objectware.no/display/java/Maven+FAQ#MavenFAQ-Howtobesttakeadvantageofapacheandcodehaussnapshotrepos%3F)):
```
mvn org.apache.maven.plugins:maven-dependency-plugin:2.0:tree
```

###### Alternative 2: Generate the dependency report:

```
mvn project-info-reports:dependencies
firefox target/site/dependencies.html
```

###### Alternative 3: Look at the POM that is actually executed:

```
mvn help:effective-pom
```

#### How to see more information about a plugin (e.g. which version is actually used)?

```
mvn help:describe -Dplugin=dependency
```

#### My parent pom is only available in a company Maven repository and this parent defines the repositories. How to fix?

###### Alternative 1: Use a profile

Add the company Maven repository to a profile in settings.xml and activate this profile the _first time_ you build a project that depends on the parent pom.

Content in **\~/.m2/settings.xml**, install with profile with _mvn install \-P company_
```
<settings>
  <servers>
    <server>
       <id>company</id>
       <username>username</username>
       <password>pw</password>
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
          <id>company</id>
          <name>company M2 repo</name>
          <url>http://m2repo.company.no/repo</url>
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
          <id>company</id>
          <name>company M2 repo</name>
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

###### Alternative 2: Use svn externals

1. Set a svn externals property below the project that reference the external parent pom.
1. svn up
1. Add a relativePath in the project that points to the external

**Example:**
```
<groupId>no.company.commons</groupId>
    <artifactId>company-parent</artifactId>
    <version>3</version>
    <relativePath>../../externals/company-parent</relativePath>
  </parent>
```
A good guide on externals can be found in [Howto: Subversion externals basics](http://jeremyknope.com/2006/06/23/howto<sub>~subversion</sub><sub>externals</sub><sub>basics/). See also [chapter 7: Externals Definitions](http://svnbook.red</sub>~bean.com/en/1.1/ch07s04.html) in _Version Control with Subversion_ for a more thorough description of how externals work.

###### Alternative 3: Manual installation

Check out the source code and install it manually.

#### How to cut a release?

See official documentation; [Release guide](http://maven.apache.org/guides/mini/guide<sub>~releasing.html) and [plugin documentation](http://maven.apache.org/plugins/maven</sub>~release-plugin/)
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
      <name>Company Internal Release Repository</name>
      <url>dav:${releaseRepoUrl}</url>
    </repository>
    <snapshotRepository>
      <id>libs-snapshots</id>
      <name>Company Internal Snapshot Repository</name>
      <url>dav:${snapshotRepoUrl}</url>
    </snapshotRepository>
  </distributionManagement>

  <properties>
    <repoUrl>http://repo.company.no/artifactory</repoUrl>
    <releaseRepoUrl>${repoUrl}/libs-releases</releaseRepoUrl>
    <snapshotRepoUrl>${repoUrl}/libs-snapshots</snapshotRepoUrl>
  </properties>
```
1. Check out a copy of the source code with the _protocol used in the scm element_ and run _mvn clean install_ to make sure you have all dependencies in the local Maven repository.
1. Do a dry run, to check that everything seems ok:
```
mvn release:prepare -DdryRun=true
mvn release:clean
```
1. Do the actual release
```
mvn release:prepare
mvn release:perform
```

#### My build builds fails because a new version of a Maven plugin has been released. How can I ensure a stable build?

This problem is reduced if Maven version 2.0.9 is used, because the versions of the plugins used in the default lifecycle is locked down here. However, all other plugins still need to be locked down.

**{+}Always lock down all plugin versions\!+**

And use the enforcer-plugin to check that it is so (and stays so).

Will check that a version is specified for all plugins (not reporting ones), but will currently ignore if they are SNAPSHOTS (see comment below).
```
<build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-enforcer-plugin</artifactId>
        <version>1.0-SNAPSHOT</version>
        <configuration>
          <rules>
            <requirePluginVersions>
              <message>Best Practice is to always define plugin versions!</message>
              <banSnapshots>false</banSnapshots> <!-- This rule doesn't work in alpha-1, alpha-2 or alpha-3-->
            </requirePluginVersions>
          </rules>
        </configuration>
        <executions>
          <execution>
            <id>enforce-plugin-versions</id>
            <phase>validate</phase>
            <goals>
              <goal>enforce</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
```

#### Which versions of Surefire and TestNG work well together? 

We recommend Surefire 2.4 and TestNG 5.7. This combination has proven to work well. 

```
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>2.4</version>
      <configuration>
        <suiteXmlFiles>
          <suiteXmlFile>src/test/resources/testng.xml</suiteXmlFile>
        </suiteXmlFiles>
      </configuration>
    </plugin>
  </plugins>
</build>
<dependencies>
  <dependency>
    <groupId>org.testng</groupId>
    <artifactId>testng</artifactId>
    <version>5.7</version>
    <scope>test</scope>
    <classifier>jdk15</classifier>
  </dependency>
</dependencies>  
```

See [TestNG](TestNG.md)

#### How to handle different groups of tests separately with TestNG?

TestNG use a configuration file, which can be changed run-time, to decide which tests to run. As of time of writing, this is the best known approach to handle multiple groups of tests. 

- Use annotations to sort your tests into groups. 
- Write one configuration for each environment you want to support (e.g. all unit tests and unit tests + integration tests) 
- Use profiles to select which configuration to run

Example setup follows. 

###### pom.xml 

Add dependency to testng and a configuration to surefire: [recommended combination of surefire and testng](http://wiki.objectware.no/display/java/Maven+FAQ#MavenFAQ-WhichversionsofSurefireandTestNGworkwelltogether%3F)

###### A test method 

```
@Test(groups = { "database"})
public void testSomeThingThatUseADatabase() {
  //some assertions

}
```

###### testng.xml
```
<!DOCTYPE suite SYSTEM "http://beust.com/testng/testng-1.0.dtd">
<suite name="ArtifactName Non-environment dependent test suite">

  <test name="Non-environment dependent tests" verbose="3">
    <groups>
      <run>
        <exclude name="database" />
        <exclude name="jms" />
      </run>
    </groups>

    <packages>
      <package name="no.company.projectName.packageA.*" />
    </packages>
  </test>
</suite>
```

###### testng<sub>~jms</sub>~database.xml
```
<!DOCTYPE suite SYSTEM "http://beust.com/testng/testng-1.0.dtd">
<suite name="ArtifactName test suite">

  <test name="All tests" verbose="10">
    <packages>
      <package name="no.company.projectName.packageA.*" />
    </packages>
  </test>
</suite>
```

**NOTE!** 
The general group concept is scalable, but many profiles quickly become chaotic. It is thus recommended to use a Continuous Integration server to handle all but two-three profiles. 

#### How to handle different groups of tests separately _without_ TestNG?

Without TestNG there are two approaches to run tests that are not run when executing _mvn test_. Note that this approach can only handle _two_ dimensions. This is why the most common separation is unit tests and integration tests. 

- Put all integration tests in a separate folder (e.g. itest).
    - See \[example \](../[http/svn<sub>~objectware</sub><sub>no</sub><sub>repos</sub><sub>objectware</sub><sub>public</sub><sub>examples</sub><sub>maven</sub><sub>itest</sub><sub>examples</sub>~itest-directory.md)

- Use a naming convention so separate from regular/unit tests (e.g. all integration tests a postfixed with IntTest
    - See \[example \](../[http/svn<sub>~objectware</sub><sub>no</sub><sub>repos</sub><sub>objectware</sub><sub>public</sub><sub>examples</sub><sub>maven</sub><sub>itest</sub><sub>examples</sub>~itest-directory.md)

#### How to cut a release when a dependency has not been released yet?

| This is a **{+}workaround{+}** to allow a snapshot dependency to be used when using maven<sub>~release</sub>~plugin. |
1. Change the version to something that clearly explains that this is a workaround to be able to perform a release with a dependency on a snapshot.
2. Add wagon webdav to the build section of the pom
```
<extensions>
  <extension>
    <groupId>org.apache.maven.wagon</groupId>
    <artifactId>wagon-webdav</artifactId>
    <version>1.0-beta-2</version>
  </extension>
</extensions>
```
3. Add authentication information to settings.xml.

4. Deploy to _altDeploymentRepository_:
```
mvn deploy -Dmaven.test.skip=true -DaltDeploymentRepository=plugins-releases::default::dav:http://repo.company.no/artifactory/plugins-releases/
```

#### How to deploy 3rd party artifacts to a DAV repository?

wagon<sub>~webdav extension is required to deploy to a DAV repository. It is therefore necessary to create a temporary pom.xml to able to perform _deploy</sub>~file_.

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

See [Maven, Windows and Deploying to a Remote Location](http://ekawas.blogspot.com/2007/02/maven<sub>~windows</sub><sub>and</sub><sub>deploying</sub>~to-remote.html)

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

#### How to assemble an application

Read the official documentation: [maven<sub>~assembly</sub><sub>plugin](http://maven.apache.org/plugins/maven</sub><sub>assembly</sub>~plugin/). If applicable, prefer to use the predefined descriptors.

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

#### How to verify that JSPs compile?

To precompile JSPs the [jspc<sub>~maven</sub><sub>plugin](http://mojo.codehaus.org/jspc</sub><sub>maven</sub>~plugin/) can be used.

Example:
```
<build>
  <plugins>
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>jspc-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>jspc</id>
          <goals>
            <goal>compile</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

#### [How to use Java WebStart with Maven](Maven<sub>~Webstart</sub>~static-website.md)

See [Maven Webstart - static website](Maven<sub>~Webstart</sub>~static-website.md).

## Concepts and general theory

#### How does Maven compare to Ant?

Maven is a lot more than a pure build tool like Ant. **Convention over configuration** is one central concept, which (among other things) means that if you follow Maven's directory structure you can use most basic goals without any configuration. Comparisons can be found in [Maven vs Ant](http://www<sub>~128.ibm.com/developerworks/java/library/j</sub>~maven/#N1006A) or [Apache Maven Simplifies the Java Build Process---Even More Than Ant](http://www.devx.com/Java/Article/17204).

#### How are projects and modules different? Are artifacts created from projects, modules or both?

In Maven there are single\- or multi-module projects. When _mvn install_ is run, each module is packaged and copied into the local Maven repository (defaults to \~/.m2/repository). The file produced is called an **artifact** and can be of type **jar**, **war**, **ejb**, etc.

#### How to decide whether some code should be a separate module in a multi-module project, or a separate project?

**One project per deployment unit**
It comes with experience, but the general rule it to have one project for each **{_}deployment unit{_}**. E.g., if you are creating a swing client that communicates with a server, these can be defined as two different deployment units and should be two different Maven projects. Modules can be used within each of these projects to split functionality into logical "chunks" of code. Modules should have high [cohesion](http://en.wikipedia.org/wiki/Cohesion_%28computer_science%29) and the considerations when creating modules are much the same as when creating Java packages.

**Libraries as separate projects**
If two products depend on some common code, this code should be placed in a separate Maven project. The domain model is a popular candidate for such a library project. Utility classes are other popular candidates. Note that these libraries are not necessarily products, but they might be, if the libraries are delivered/used by themselves or by other products.

#### [How to share resources across projects in Maven](http://blogs.sonatype.com/brian/2008/04/17/1208485500000.html)

[How to share resources across projects in Maven](http://blogs.sonatype.com/brian/2008/04/17/1208485500000.html)

#### Where can I find the "superPom" that +all+ Maven projects inherit from?

[http://svn.apache.org/repos/asf/maven/components/trunk/maven<sub>~project/src/main/resources/org/apache/maven/project/pom</sub><sub>4.0.0.xml](http://svn.apache.org/repos/asf/maven/components/trunk/maven</sub><sub>project/src/main/resources/org/apache/maven/project/pom</sub>~4.0.0.xml)

## Tips to make development with Maven a bit smoother

#### How to get code completion in an IDE

Add the following to _settings.xml_.
```
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
```

#### How to make javadoc and sources available to your IDE

```
mvn idea:idea -DdownloadSources=true -DdownloadJavadocs=true
mvn eclipse:eclipse -DdownloadSources=true -DdownloadJavadocs=true
```

#### How to best take advantage of apache and codehaus snapshot repos?

1. Proxy them with a [Build Artifact Repository Manager](http://maven.apache.org/repository-management.html). 
1. Add them to a profile in settings.xml and use with _\<sub>~Papache_ or _\</sub>~Pcodehaus_

```
<profiles>
     <profile>
      <id>apache</id>
      <repositories>
        <repository>
          <id>apache.org</id>
          <name>Maven Snapshots</name>
          <url>http://people.apache.org/repo/m2-snapshot-repository</url>
          <releases>
            <enabled>false</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>apache.org</id>
          <name>Maven Plugin Snapshots</name>
          <url>http://people.apache.org/repo/m2-snapshot-repository</url>
          <releases>
            <enabled>false</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>

    <profile>
      <id>codehaus</id>
      <repositories>
        <repository>
          <id>codehaus.org</id>
          <name>CodeHaus Snapshots</name>
          <url>http://snapshots.repository.codehaus.org</url>
          <releases>
            <enabled>false</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>codehaus.org</id>
          <name>CodeHaus Plugin Snapshots</name>
          <url>http://snapshots.repository.codehaus.org</url>
          <releases>
            <enabled>false</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>
  </profiles>
```
It is **not** recommended to put these repositories directly in pom.xml, because they cannot be used in a final release. (And we do not want to support habits that adds yetAnotherThingToRemember before a release.)

#### How to set how much memory Maven can use? 
###### Linux (bash) 
```
Export MAVEN_OPTS="-Xms256m -Xmx1024m -XX:MaxPermSize=512m"
```

###### Windows
```
set MAVEN_OPTS="-Xms256m -Xmx1024m -XX:MaxPermSize=512m"
```
