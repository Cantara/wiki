# Organizing Maven projects

#### Guidelines

There are many [types of Maven project relationships](http://www.sonatype.com/books/maven-book/reference/pom-relationships-sect-project-relationships.html)  and many ways or organizing Maven projects. The purpose of this page is to explain some guidelines and setups that we have come to value. The main guidelines can be summarized as follows:

- *Lifecycle*: Projects/modules with different release cycles should not share reactor (or trunk).

- "\_ One primary output per project\_", from [BBwM](http://www.exist.com/better-build-maven) , chap.1.2.1, page 27, and likewise "One project per deployment unit" ([Maven FAQ](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Organize+Maven+projects+and+modules+FAQ "Organize Maven projects and modules FAQ") )

- *Common code*: Place code shared by multiple projects in a separate project.

- When in doubt, separate!

#### Detailed descriptions and examples

- [Project Inheritance](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Project+Inheritance "Project Inheritance") aka. *Parent* *POM*.
- Multi-module projects aka. *Aggregator projects*
  - [Builder project](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Builder+project "Builder project") (no inheritance)
  - [Multi-module project with inheritance](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Multi-module+project+with+inheritance "Multi-module project with inheritance")
  - [Multi-module project with shared release cycle only](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Multi-module+project+with+shared+release+cycle+only "Multi-module project with shared release cycle only")
- [Project Structure for Persistence Logic](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Project+Structure+for+Persistence+Logic "Project Structure for Persistence Logic")

- [Maven Project Terminology](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Maven+Project+Terminology "Maven Project Terminology")
- [Recommended directory structure using Subversion and Maven](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Recommended+directory+structure+using+Subversion+and+Maven "Recommended directory structure using Subversion and Maven")
- [Maven Artifact Naming](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Maven+Artifact+Naming "Maven Artifact Naming")
- Example of a [Release Profile](/web/20100615233055/http://wiki.cantara.no/display/smidigtonull/Release+Profile "Release Profile")
