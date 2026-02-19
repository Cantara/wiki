# Organizing Maven projects

#### Guidelines  

There are many [types of Maven project relationships](http://www.sonatype.com/books/maven<sub>~book/reference/pom</sub><sub>relationships</sub><sub>sect</sub>~project-relationships.html) and many ways or organizing Maven projects. The purpose of this page is to explain some guidelines and setups that we have come to value. The main guidelines can be summarized as follows: 

- _Lifecycle_: Projects/modules with different release cycles should not share reactor (or trunk). 

- "_ One primary output per project_", from [BBwM](http://www.exist.com/better<sub>~build</sub><sub>maven), chap.1.2.1, page 27, and likewise "One project per deployment unit" ([Maven FAQ](Organize</sub><sub>Maven</sub><sub>projects</sub><sub>and</sub>~modules-FAQ.md))

- _Common code_: Place code shared by multiple projects in a separate project. 

- When in doubt, separate! 

#### Detailed descriptions and examples 

- [Project Inheritance](Project-Inheritance.md) aka. _Parent_ _POM_.
- Multi-module projects aka. _Aggregator projects_
    - [Builder project](Builder-project.md) (no inheritance) 
    - [Multi<sub>~module project with inheritance](Multi</sub><sub>module</sub><sub>project</sub>~with-inheritance.md)
    - [Multi<sub>~module project with shared release cycle only](Multi</sub><sub>module</sub><sub>project</sub><sub>with</sub><sub>shared</sub><sub>release</sub><sub>cycle</sub>~only.md)
- [Project Structure for Persistence Logic](Project<sub>~Structure</sub><sub>for</sub><sub>Persistence</sub>~Logic.md) 

- [Maven Project Terminology](Maven<sub>~Project</sub>~Terminology.md)
- [Recommended directory structure using Subversion and Maven](Recommended<sub>~directory</sub><sub>structure</sub><sub>using</sub><sub>Subversion</sub><sub>and</sub>~Maven.md)
- [Maven Artifact Naming](Maven<sub>~Artifact</sub>~Naming.md)
- Example of a [Release Profile](Release-Profile.md)
