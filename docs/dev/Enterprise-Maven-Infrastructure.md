# Enterprise Maven Infrastructure

#### Introduction 

A prerequisite for efficient development is to choose good tools and use these tools to their full potential. The Java community has a comprehensive suite of tools to choose from; IDE, VCS, build tools, CI server and Build Artifact Repository Manager. It is common (perhaps even _best practice_?) to standardize on **VCS** and **build tool** on Enterprise Java projects. While it might be appropriate to standardize on IDE in a small (not Enterprise) project, this is seldom a good idea (reasoning: three competing IDEs, "works-here-syndrome", etc.). As of time of writing Maven2 is the leading build tool on the market and [Subversion](http://subversion.tigris.org/) is the most popular VCS. 

For repository management, the choice is not that obvious as there are at least three adequate products available; Archiva, Artifactory and Nexus. [Archiva](http://archiva.apache.org/) has no support for virtual repositories, so [Artifactory](http://www.jfrog.org/sites/artifactory/latest/) seems a better choice for most big companies. [Nexus](http://nexus.sonatype.org/) claims to have both virtual repository support and use file system storage (not a Java space like Artifactory) and surfs up as an enticing alternative to the two others. The recommendations given is based on experiences from using Artifactory, but most should apply to both Nexus and Archiva. 

There are plenty of good Continuous Integration servers available, both commercial and Open Source. An overview of some of the most popular ones can be found in [sysadm:Continuous Integration Server Overview](../sysadm/Continuous-Integration-Server-Overview.md). Choose anyone you want. We prefer Continuum for two reasons: 
1. It has excellent support for Maven projects and utilize a lot of information from the POM. 
1. Projects can be released from the GUI, which makes it easier for system architects, project managers and other non-developers to cut a release.

The rest of this article will explain how to work efficiently on Maven-based projects in an Enterprise context, with focus on the infrastructure required. **Effective communication** is a key component in any well-functional team. This topic is outside the scope of this article, but a **wiki**, an **issue tracker**, **email lists** and an **agile mindset** are highly recommended. 

###### Example setup

1. **IDE - +any+**
2. VCS - **[Subversion](http://subversion.tigris.org/)**
3. Build tool - **[Maven2](http://maven.apache.org)**
4. Build Artifact Repository Manager - **[Artifactory](http://www.jfrog.org/sites/artifactory/latest/)**
5. Continuous Integration Server - **[Continuum](http://continuum.apache.org/)**

#### Component overview 

There are basicly three main processes we want Enterprise Maven Infrastructure to support (in addition to regular Continuous Integration) 
1. use CI server to deploy snapshots to the build artifact repository manager
2. release (initiated from CI server or directly with maven)
3. deploy the technical site so the documentation (for the snapshot or the release is easily accessable)

Step 3. is optional, but deploying the site at least **nightly** AND **for every release** adds a lot of value.

#### 1. Deploy snapshots
**Diagram: Enterprise**

#### 2. Release
**Diagram: Enterprise**

#### Implementation recommendations 

- [Organizing Maven projects](Organizing-Maven-projects.md)
- [Repository Management](Repository-Management.md)
- [CI recommendations](CI-recommendations.md)
- [sysadm:Version Control System tips and tricks](../sysadm/Version-Control-System-tips-and-tricks.md)
- [Technical site and reporting](Technical-site-and-reporting.md)
- [Automatic code review](Automatic-code-review.md)
- [Agile Project Communication](Agile-Project-Communication.md)

###### Administration

- It is important that the system administrators feel ownership and take responsibility for the infrastructure. 

- Always use service names for all services to make it possible to switch implementations easily. E.g., avoid http://192.168.1.1:8080/artifactory in company parent-pom. 

#### Resources

- [Integrated Development Environment (IDE)](http://en.wikipedia.org/wiki/Integrated_Development_Environment) ([IntelliJ IDEA](http://www.jetbrains.com/idea/), [Eclipse](http://www.eclipse.org/), [Netbeans](http://www.netbeans.org/))
- [Version Control Management System (VCS) aka. Source Control Management (SCM)](http://en.wikipedia.org/wiki/Revision_control)
- Build tools: [Maven2](http://maven.apache.org), [Maven1](http://maven.apache.org/maven-1.x/), [Ant](http://ant.apache.org/), [make](http://www.gnu.org/software/make/), [gradle](http://www.gradle.org) 
- [Build Artifact Repository Manager](http://maven.apache.org/repository-management.html) 

#### External articles about Maven infrastructure

- [Summary of Maven How-Tos, by Brian Fox](http://www.sonatype.com/people/2009/04/summary-of-maven-how-tos/)
- [Maven in our development process. Part 2 - Maven infrastructure.](http://blogs.atlassian.com/developer/2008/02/maven_in_our_development_proce_2.html)
- [Maven: The Definitive Guide - 3.5.4. Maven Repositories](http://www.sonatype.com/book/reference/simple-project.html#section-simple-repo)
- [Automation for the people: Pushbutton documentation](http://www.ibm.com/developerworks/java/library/j-ap06108/index.html?ca=drs-)
