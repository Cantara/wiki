# Organize Maven projects and modules FAQ

## Table of Contents

---

#### What is and where can I find the Maven SuperPOM? 

All Maven projects implicitly inherit from the Maven super pom. Read more on the subject in [Introduction to the pom, Super_POM](http://maven.apache.org/guides/introduction/introduction-to-the-pom.html#Super_POM). See subversion for the [Maven 2.0.9 Super POM](http://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.9/maven-project/src/main/resources/org/apache/maven/project/pom-4.0.0.xml). 

#### How are projects and modules different? Are artifacts created from projects, modules or both?

In Maven there are single\- or multi-module projects. When _mvn install_ is run, each module is packaged and copied into the local Maven repository (defaults to \~/.m2/repository). The file produced is called an **artifact** and can be of type **jar**, **war**, **ejb**, etc.

#### How to decide whether some code should be a separate module in a multi-module project, or a separate project?

**One project per deployment unit**
It comes with experience, but the general rule it to have one project for each **{_}deployment unit{_}**. E.g., if you are creating a swing client that communicates with a server, these can be defined as two different deployment units and should be two different Maven projects. Modules can be used within each of these projects to split functionality into logical "chunks" of code. Modules should have high [cohesion](http://en.wikipedia.org/wiki/Cohesion_%28computer_science%29) and the considerations when creating modules are much the same as when creating Java packages.

**Libraries as separate projects**
If two products depend on some common code, this code should be placed in a separate Maven project. The domain model is a popular candidate for such a library project. Utility classes are other popular candidates. Note that these libraries are not necessarily products, but they might be, if the libraries are delivered/used by themselves or by other products.

#### When I deploy my multi-module project it is still possible for another project to depend only the artifact generated for one of the modules. Isn't this the best of both worlds?

It is possible to add a dependency directly to a module of another project. However, then you also add a dependency to the _parent_ of the module and any other modules in this project that the module depends on. You also require that the whole multi-module project must be deployed/released if you need a new version of the module. 
In other words, **this is a bad thing (TM)**! 

#### When is a _single_ Maven project appropriate? 

When the project 

- is a standalone library 
- produces a single deployment unit and no code needs to be shared with other projects. I.e., do not move a module into a separate project just for the purpose of creating an external dependency. 

#### I really, really want to have a single project for everything. Why is that a bad idea? 

The only real advantage of the "Everything in one project" strategy is that it may be  easier to understand for inexperienced developers. Below follows a list of disadvantages with using this approach: 

- If Maven's principles are not followed, the benefits of using Maven are forsaken as well. E.g., if two deployment units are put into the same Maven project multiple plugins (e.g. release, assembly, webstart) no longer work as expected.  

- Release everything or release nothing. 

- All developers must build all modules, always. This might be appropriate for small projects, but for enterprise projects the build quickly becomes annoyingly slow. 

- Two small projects are easier to get to know than one large project. This means that ramp-up-time for a new developer is reduced if a module can be refactored into a separate project. 

- When the number of modules grow too large, the volume of code, tests and dependencies grows accordingly. This increases the risk of creating circular dependencies and makes it harder to maintain low coupling and high cohesion. 

- the longer you build your silo, the more difficult it is to break out of the silo

- it works on my machine syndrome...

- cross-cutting commits break builds and reduce productivity

#### Moving a module to a separate Maven project means that I now must build _two_ projects instead of one. This is bothersome and increases my round-trip time. How can this be a good thing? 

- First, only the developer making the change to the (now) external project needs to build this project. The CI server should deploy the new version of the external project and deploy it to a [Build Artifact Repository Manager](http://maven.apache.org/repository-management.html). Enterprise projects needs [Enterprise Maven Infrastructure](Enterprise-Maven-Infrastructure.md)!

- Second, if small changes require modifications to multiple projects, this should be viewed as an indication that perhaps some refactoring is in order. (This is a common _"code smell"_.) 

#### How to modularize a Maven project? 

In progress

In an ideal world refactorizing a Maven project should not break any tests and could be committed to VCS as a single transaction. To my experience this is extremely hard to do, at least with Subversion. It is thus vital that you ensure that your work does not hinder other developers from working. E.g. do the refactorization in a branch, because it +**is**+ necessary to commit multiple times (again assuming Subversion). 

1. Create a VCS tag 
1. Stop CI 
1. Create a new empty module 
1. Move all existing code into this new module 
1. Create a parent pom and set up **two-way** relationship to the module 
1. Run all tests and commit to VCS 
1. Create the rest of the modules 
1. Move code from the original module to the others. 
1. Ensure that all tests run successfully 
1. Commit
1. Start CI (and cross your fingers for luck) 

#### What is the recommended way to set module versions? 

IMHO, Maven is more flexible than necessary in this regard. I prefer to have all modules use the same version as the parent when the modules also **inherit from the parent**. 

This is done by 

- lock down module versions with dependencyManagement in the parent 
```
<modules>
  <module>project-module1</module>
  <module>project-module2</module>
</modules>

<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>${pom.groupId}</groupId>
      <artifactId>project-module1</artifactId>
      <version>${pom.version}</version>
    </dependency>
    <dependency>
      <groupId>${pom.groupId}</groupId>
      <artifactId>project-module2</artifactId>
      <version>${pom.version}</version>
    </dependency>    
  </dependencies>
</dependencyManagement>
```

- Inherit from parent in all modules 

- do not specify version in any of the modules 

When one module needs code from another module, just add a dependency to that module, but omit the version here as well. 

Dependencies common to all modules is a candidate for extracting to the parent pom. 

#### [How to structure EAR projects?](How-to-structure-EAR-projects.md)

See [How to structure EAR projects?](How-to-structure-EAR-projects.md).
