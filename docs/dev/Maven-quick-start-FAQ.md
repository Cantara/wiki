# Maven quick-start FAQ

## Table of Contents

---

#### What does "Maven" mean? 

 _A maven (also mavin or mayvin) is a trusted expert in a particular field, who seeks to pass his or her knowledge on to others._ (From: [Wikipedia](http://en.wikipedia.org/wiki/Maven)) 

#### How to learn Maven? 

RTFM: 

- [Maven documentation](http://maven.apache.org/guides/index.html)
- [Maven: The Definitive Guide](http://www.sonatype.com/book/index.html) (free online book)
- [Better Builds with Maven](http://www.devzuz.com/web/guest/products/resources#BBWM) (free online book, but registration is needed)
- [Maven's wiki](http://docs.codehaus.org/display/MAVEN)

#### How does Maven compare to Ant?

Maven is a lot more than a pure build tool like Ant. **Convention over configuration** is one central concept, which (among other things) means that if you follow Maven's directory structure you can use most basic goals without any configuration. Comparisons can be found in [Maven vs Ant](http://www-128.ibm.com/developerworks/java/library/j-maven/#N1006A) or [Apache Maven Simplifies the Java Build Process---Even More Than Ant](http://www.devx.com/Java/Article/17204).

#### How to convert an Ant project to Maven?

1. Create a tag in the version control system (to be able to roll back) 
1. Create new directory structure 
    1. Create a new empty Maven project with [Standard Directory Layout](http://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
(Tip: the [archetype plugin](http://maven.apache.org/plugins/maven-archetype-plugin/) can be used to set up template projects quickly.)
    1. Copy sources and resources from old project to the new standard Maven directory structure. 
1. Add dependencies. [Introduction to the Dependency Mechanism](http://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html) explains how dependencies work in Maven. [Sonatype's Nexus instance](http://repository.sonatype.org) or [http://mvnrepository.org](http://mvnrepository.org) can be used to search for available dependencies. 
1. Bugfix until the [default build lifecycle](http://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html) works properly (It basically works when _mvn clean install_ builds successfully.) 
1. Add additional plugins 
    1. Use the [release plugin](http://maven.apache.org/guides/mini/guide-releasing.html) 
    1. Use [assemblies](http://maven.apache.org/guides/mini/guide-assemblies.html) to create the proper delivery packages 
    1. Add additional plugin definitions as needed. The [Mojo project](http://mojo.codehaus.org/) at Codehaus is a good place to start looking for plugins.
    1. Ant tasks that you are unable to find a proper replacement for can be run by the [Antrun plugin](http://maven.apache.org/plugins/maven-antrun-plugin/). However, this option should only be used as a last resort or as a means to minimize the impact of switching to Maven.

**Resources:**
- http://www.sonatype.com/people/2010/08/how-to-migrate-from-ant-to-maven-project-structure/
