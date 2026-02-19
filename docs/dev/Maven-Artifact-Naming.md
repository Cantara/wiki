# Maven Artifact Naming

###### artifactId
The name of a libProject/product used in VCS should be reflected in the _artifactId_ of the project. Additionally, it is common to prefix all modules (including the parent) in a multimodule project. E.g. commons-parent, commons-log, commons-file. 

###### groupId
Choosing a _groupId_ is a bit trickier: 
- groupId + some variant of the artifactId should be equal to the java package
- The directory structure of the project must match the Java package structure
- The groupId should thus follow [SUN's Naming Conventions](http://java.sun.com/docs/codeconv/html/CodeConventions.doc8.html). (So do not use camelCase!)

#### Some well-named artifacts

```
<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-plugin-parent</artifactId>

<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-antrun-plugin</artifactId>

<groupId>com.telenor.cinclus</groupId>
<artifactId>cinclus-parent</artifactId>

<groupId>com.telenor.cinclus.store.sql</groupId>
<artifactId>cinclus-sql-helper</artifactId>

<groupId>com.telenor.cinclus.transport.jms</groupId>
<artifactId>cinclus-jms-helper</artifactId>
```
