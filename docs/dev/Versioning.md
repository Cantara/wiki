# Versioning

- **Source code** can easily be version controlled with a [Version Control System](http://en.wikipedia.org/wiki/List_of_revision_control_software) .

- We can control the version of **artifacts** using Maven and the [maven-release-plugin](http://maven.apache.org/plugins/maven-release-plugin). See [Organizing Maven projects](/web/20210226164142/https://wiki.cantara.no/display/dev/Organizing+Maven+projects "Organizing Maven projects") for details on how to structure your Maven projects to achieve releasable artifacts.

- All applications needs some sort of **configuration**.
  - In a non-distributed system the configuration can probably be version controlled much like the source code, since all configuration can be found in one place.
  - In a *distributed system*, however, the configuration is needed in multiple locations. If we want to control and track changes to the configuration of the *system as a whole* we must have a way to tag the configuration of all the nodes with a shared version.

- The **base system** is the final piece of the puzzle. I presume there exists some sort of software to ensure complete control of operating system, installed software and their configuration. An alternative approach is to create the means to easily get back to a known state. In this context this means fully automating the installation of the base system. This can be achieved by scripting the installation or by cloning images ("ghosting").

[Major, minor, micro](http://apr.apache.org/versioning.html)   
[Semantic Versioning 2.0.0](http://semver.org/)

[Maven Project Versions](http://books.sonatype.com/mvnref-book/reference/pom-relationships-sect-pom-syntax.html#pom-reationships-sect-versions)

[Maven Version ranges](http://books.sonatype.com/mvnref-book/reference/pom-relationships-sect-project-dependencies.html#pom-relationships-sect-version-ranges)   
[Maven Version ranges - enforcer](http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html)

[Software\_version (wikipedia)](http://en.wikipedia.org/wiki/Software_version)
