# Maven Dependencies and Build Stability FAQ

## Table of Contents

---

#### How to handle libraries that cannot be found in any public Maven repository?

- Download the artifact to local storage. (e.g. /tmp/)
- Add the dependency to pom.xml and run _mvn clean install_. If the dependency cannot be found, the output will display which command to run to install the artifact.
- Change the "-Dfile=path-to-your-artifact-jar" option to point to the downloaded artifact (e.g. /tmp/someArtifact.jar)

This will solve the problem for one user, one a single computer. A better solution is to deploy the artifact to, e.g., the company repository. 
See [how to use a build artifact repository manager](http://wiki.community.objectware.no/display/smidigtonull/Maven+FAQ#MavenFAQ-Howtouseabuildartifactrepositorymanager%3F) for an example on how to use a company Maven repository. 

#### How to debug problems related to different versions of a dependency?

###### Alternative 1: Use the [maven-dependency-plugin](http://maven.apache.org/plugins/maven-dependency-plugin)

Display a the dependency tree directly in the console (requires the [apache-snapshot-repo](http://wiki.objectware.no/display/java/Maven+FAQ#MavenFAQ-Howtobesttakeadvantageofapacheandcodehaussnapshotrepos%3F)):
```
mvn dependency:tree
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

###### Alternative 1: Use profiles

Add the company Maven repository to a profile in settings.xml and activate this profile the _first time_ you build a project that depends on the parent pom. See the [how to use a build artifact repository manager](http://wiki.community.objectware.no/display/smidigtonull/Maven+FAQ#MavenFAQ-Howtouseabuildartifactrepositorymanager%3F) section for an example. 

###### Alternative 2: Use svn externals

1. Set a svn externals property below the project that reference the external parent pom.
1. svn up
1. Add a relativePath in the project that points to the external

```
    <groupId>no.objectware.commons</groupId>
    <artifactId>objectware-parent</artifactId>
    <version>3</version>
    <relativePath>../../externals/objectware-parent</relativePath>
  </parent>
```
See [http://svn.objectware.no/repos/objectware-public/examples/agile2/trunk/](http://svn.objectware.no/repos/objectware-public/examples/agile2/trunk/) for an example implementation.

A good guide on externals can be found in [Howto: Subversion externals basics](http://jeremyknope.com/articles/2006/06/23/howto-subversion-externals-basics). See also [chapter 7: Externals Definitions](http://svnbook.red-bean.com/en/1.1/ch07s04.html) in _Version Control with Subversion_ for a more thorough description of how externals work.

###### Alternative 3: Manual installation

Check the source code and install it manually. 

#### My build builds fails because a core Maven plugin has been released. How can I ensure a stable build?

Always lock down all plugin versions\!

Use the enforcer-plugin to check it.

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

#### How to share resources across projects in Maven

Two methods of sharing resources distinguishes themselves as better than other. These are using the _maven-remote-resources-plugin_ and a combination of the _maven-assembly-plugin_ and _maven-dependency-plugin_.

To help you choose, here are some qualities of the methods

| maven-remote-resources-plugin | maven-assembly-plugin and maven-dependency-plugin |
| --- | --- |
|(+) Easy configuration
 (+) Supports velocity templates|(+) More flexible
 (-) Requires more configuration|

> 📝 Need more qualities of the two methods to help with the selection of one method for a project.

##### maven-remote-resources-plugin
Create a project that contains the resources to be shared. A minimal pom follows:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>no.objectware.examples</groupId>
	<artifactId>shared-resources</artifactId>
	<packaging>jar</packaging>
	<version>1.0-SNAPSHOT</version>

	<build>
		<plugins>
			<plugin>
				<artifactId>maven-remote-resources-plugin</artifactId>
				<executions>
					<execution>
						<goals>
							<goal>bundle</goal>
						</goals>
						<configuration>
							<includes>
								<include>**/*.properties</include>
							</includes>
						</configuration>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>
</project>
```

The plugin creates a _shared-resources.xml_ inside the _META-INF_ directory of the resulting jar. This file is used by the consumer and lists the resources that are shared and consequently extracted from the jar. 

The configuration element includes specifies which files are listed in _shared-resources.xml_. By default, only _.txt_ and _.vm_ files are included. The default base directory for these patterns is the _resource_ directory.

Using shared resources in a project requires the following minimum pom:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>no.objectware.examples</groupId>
	<artifactId>shared-resources-consumer</artifactId>
	<packaging>jar</packaging>
	<version>1.0-SNAPSHOT</version>

	<build>
		<plugins>
			<plugin>
				<artifactId>maven-remote-resources-plugin</artifactId>
				<executions>
					<execution>
						<goals>
							<goal>process</goal>
						</goals>
						<configuration>
							<resourceBundles>
								<resourceBundle>no.objectware.commons:shared-resources:1.0-SNAPSHOT</resourceBundle>
							</resourceBundles>
						</configuration>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>
</project>
```

The shared resources will now be unpacked and included in the project. They are unpacked to _$\/maven-shared-archive-resources_ and this directory is added to the list of resources but not filtered. 

Any resource ending with _.vm_ is treated as a velocity template, stripped of the .vm ending and processed. Properties to Velocity can be passed via the configuration tag of the plugin. 

Any project defining the consumer as a parent will also have the resources unpacked.

For more information see the [plugin site](http://maven.apache.org/plugins/maven-remote-resources-plugin/).

##### maven-assembly-plugin and maven-dependency-plugin

Create a project that contains the resources to be shared. A minimal pom follows:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>no.objectware.examples</groupId>
	<artifactId>shared-resources</artifactId>
	<packaging>pom</packaging>
	<version>1.0-SNAPSHOT</version>

	<build>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-assembly-plugin</artifactId>
				<version>2.2-beta-2</version>
				<executions>
					<execution>
						<id>make shared resources</id>
						<goals>
							<goal>single</goal>
						</goals>
						<phase>package</phase>
						<configuration>
							<descriptors>
								<descriptor>src/main/assembly/resources.xml</descriptor>
							</descriptors>
						</configuration>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>
</project>
```

Note here that the project may be packaged as _pom_. This is because the shared resources are packaged as described in the assembly descriptor with the assembly id as classifier. This assembly descriptor needs to be referred to in the pom as can be seen in the configuration section of the plugin. An example of a descriptor:

```xml
<assembly>
	<id>resources</id>
	<formats>
		<format>zip</format>
	</formats>
	<includeBaseDirectory>false</includeBaseDirectory>
	<fileSets>
		<fileSet>
			<directory>src/main/resources</directory>
			<outputDirectory/>
		</fileSet>
	</fileSets>
</assembly>
```

Using this, all files in the resources directory will be packaged in a zip file with the id, _resources_, as the classifier.

For more information see the [plugin site](http://maven.apache.org/plugins/maven-assembly-plugin/).

Using shared resources in a project requires the following minimum pom:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>no.objectware.examples</groupId>
	<artifactId>shared-resources-comsumer</artifactId>
	<packaging>jar</packaging>
	<version>1.0-SNAPSHOT</version>

	<dependencies>
		<dependency>
			<groupId>no.objectware.examples</groupId>
			<artifactId>shared-resources</artifactId>
			<version>1.0-SNAPSHOT</version>
			<classifier>resources</classifier>
			<type>zip</type>
			<scope>provided</scope>
		</dependency>
	</dependencies>

	<build>
		<resources>
			<resource>
				<directory>${basedir}/src/main/resources</directory>
				<filtering>true</filtering>
			</resource>
			<resource>
				<directory>${project.build.directory}/shared-resources</directory>
				<filtering>true</filtering>
			</resource>
		</resources>

		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-dependency-plugin</artifactId>
				<version>2.0</version>
				<executions>
					<execution>
						<id>unpack-shared-resources</id>
						<goals>
							<goal>unpack-dependencies</goal>
						</goals>
						<phase>generate-resources</phase>
						<configuration>
							<outputDirectory>${project.build.directory}/shared-resources</outputDirectory>
							<includeArtifacIds>shared-resources</includeArtifacIds>
							<includeGroupIds>no.objectware.examples</includeGroupIds>
							<excludeTransitive>true</excludeTransitive>
						</configuration>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>

</project>
```

The shared resources will now be unpacked and included in the project. They are unpacked to _target/shared-resources_ and this directory is added manually to the list of resources in the build section of the pom.

Since this is the dependency plugin performing operations on a dependency, it is critical that the artifact containing the shared resources is listed amongst the dependencies of the consumer project.

Any project defining the consumer as a parent will also have the resources unpacked.

For more information see the [plugin site](http://maven.apache.org/plugins/maven-dependency-plugin/).

For a more detailed explanation of this method see [Brian's Enterprise Blog](http://blogs.sonatype.com/brian/2008/04/17/1208485500000.html).
