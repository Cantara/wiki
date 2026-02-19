# Organizing Maven projects

#### Guidelines  

There are many [types of Maven project relationships](http://www.sonatype.com/books/maven-book/reference/pom-relationships-sect-project-relationships.html) and many ways or organizing Maven projects. The purpose of this page is to explain some guidelines and setups that we have come to value. The main guidelines can be summarized as follows: 

- _Lifecycle_: Projects/modules with different release cycles should not share reactor (or trunk). 

- "_ One primary output per project_", from [BBwM](http://www.exist.com/better-build-maven), chap.1.2.1, page 27, and likewise "One project per deployment unit" ([Maven FAQ](Organize-Maven-projects-and-modules-FAQ.md))

- _Common code_: Place code shared by multiple projects in a separate project. 

- When in doubt, separate! 

#### Detailed descriptions and examples 

- [Project Inheritance](Project-Inheritance.md) aka. _Parent_ _POM_.
- Multi-module projects aka. _Aggregator projects_
    - [Builder project](Builder-project.md) (no inheritance) 
    - [Multi-module project with inheritance](Multi-module-project-with-inheritance.md)
    - [Multi-module project with shared release cycle only](Multi-module-project-with-shared-release-cycle-only.md)
- [Project Structure for Persistence Logic](Project-Structure-for-Persistence-Logic.md) 

- [Maven Project Terminology](Maven-Project-Terminology.md)
- [Recommended directory structure using Subversion and Maven](Recommended-directory-structure-using-Subversion-and-Maven.md)
- [Maven Artifact Naming](Maven-Artifact-Naming.md)
- Example of a [Release Profile](Release-Profile.md)
