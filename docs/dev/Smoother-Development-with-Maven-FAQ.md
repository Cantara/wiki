# Smoother Development with Maven FAQ

## Table of Contents

- [Table of Contents](#SmootherDevelopmentwithMavenFAQ-TableofContents)

- [How to find which jar a class belongs to](#SmootherDevelopmentwithMavenFAQ-Howtofindwhichjaraclassbelongsto)
- [How to find a pom snippet for a given jar](#SmootherDevelopmentwithMavenFAQ-Howtofindapomsnippetforagivenjar)
- [How to use a socks proxy](#SmootherDevelopmentwithMavenFAQ-Howtouseasocksproxy)
- [How to use a HTTP proxy](#SmootherDevelopmentwithMavenFAQ-HowtouseaHTTPproxy)
- [How to get code completion in an IDE](#SmootherDevelopmentwithMavenFAQ-HowtogetcodecompletioninanIDE)
- [How to make javadoc and sources available to your IDE](#SmootherDevelopmentwithMavenFAQ-HowtomakejavadocandsourcesavailabletoyourIDE)
- [How to set how much memory Maven can use?](#SmootherDevelopmentwithMavenFAQ-HowtosethowmuchmemoryMavencanuse%3F)
- [How to run a single test with Maven?](#SmootherDevelopmentwithMavenFAQ-HowtorunasingletestwithMaven%3F)
- [How to start a an application by running *public static void main* with Maven?](#SmootherDevelopmentwithMavenFAQ-HowtostartaanapplicationbyrunningpublicstaticvoidmainwithMaven%3F)
- [How to use apache and codehaus snapshot repos?](#SmootherDevelopmentwithMavenFAQ-Howtouseapacheandcodehaussnapshotrepos%3F)

---

#### How to find which jar a class belongs to

[jarFinder](http://www.jarfinder.com/) or [javacio.us/jarhoo](http://javacio.us/jarhoo)

#### How to find a pom snippet for a given jar

Places to start:

- [MVNBrowser](http://www.mvnbrowser.com/)
- [Sonatype Nexus](http://repository.sonatype.org/index.html)
- [Javacio.us/poms](http://javacio.us/poms)

#### How to use a socks proxy

Set up a SSH tunnel to a server somewhere:

and use 6655 as socks port.

**Linux (bash)**:

**Windows**:

#### How to use a HTTP proxy

[Maven: Configuring a proxy](http://maven.apache.org/guides/mini/guide-proxies.html)

#### How to get code completion in an IDE

Add the following to *settings.xml*.

#### How to make javadoc and sources available to your IDE

**Eclipse**:

**IntelliJ IDEA**:or   
If you use pom.xml to open your IDEA project, then javadoc and sources under ~/.m2/repository are automatically available. To download sources to ~/.m2/repository click *Download artifacts* in IDEA's Maven panel.

#### How to set how much memory Maven can use?

**Linux (bash)**:

**Windows**:

#### How to run a single test with Maven?

Use the [Surefire plugin](http://maven.apache.org/plugins/maven-surefire-plugin) for running a single test class.

#### How to start a an application by running *public static void main* with Maven?

Use the [exec plugin](http://mojo.codehaus.org/exec-maven-plugin) to start applications with a main method.

#### How to use apache and codehaus snapshot repos?

1. Inherit from [objectware-parent](http://svn.objectware.no/repos/objectware-public/objectware-commons/objectware-parent/pom.xml)
2. Add them to a profile in settings.xml and use with *-Papache* or *-Pcodehaus*

It is **not** recommended to put these repositories directly in pom.xml, because they cannot be used in a final release. (And we do not want to support habits that adds yetAnotherThingToRemember before a release.)
