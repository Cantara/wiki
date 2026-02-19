# Project Inheritance

#### Introduction 

Project inheritance is about sharing POM configuration between projects. See [9.5.3. Project Inheritance](http://www.sonatype.com/books/maven-book/reference/pom-relationships-sect-project-inheritance.html) for a description of the concept. 

There will always be a trade-off between the [DRY principle](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself) and level of complexity. In other words; while Maven supports the perfect inheritance tree, many levels of inheritance may make the setup too complex.

We will now explain one rather sophisticated setup that evolved in a Norwegian company with more than 50 Maven projects.   

**[Diagram: project_inheritance](../Diagram/project_inheritance.md)** 

#### POM descriptions 

Example on the [Generic Parent POM Example](Generic-Parent-POM-Example.md) - used by almost all projects in an organization (possibly indirectly).

- Two-level structure (inherits Generic)
    - [Java Parent POM Example](Java-Parent-POM-Example.md) - used by all _Java_ projects in an organization
    - [JSW Daemon Parent POM Example](JSW-Daemon-Parent-POM-Example.md) - used by all projects deployed as Java Service Wrapper Daemons
    - [JSW Daemon Webapp Parent POM Example](JSW-Daemon-Webapp-Parent-POM-Example.md) - used by all projects deployed as Java Service Wrapper Daemons with Jetty

If you only have Java projects the [generic parent pom](Generic-Parent-POM-Example.md) can be combined with the [java parent pom](Java-Parent-POM-Example.md) to remove one level of inheritance: 

- Single parent pom for only java projects
    - [Company parent pom example for only Java projects](Company-parent-pom-example-for-only-Java-projects.md)
