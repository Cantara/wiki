# Maven Other FAQ

#### How to compile C++ code with Maven? 

Alternative 1: Use [exec-maven-plugin](http://mojo.codehaus.org/exec-maven-plugin/) to call a make script. 

Alternative 2: Use [native-maven-plugin](http://mojo.codehaus.org/maven-native/native-maven-plugin/) to call the compiler directly. 

**TODO** Paste pom examples 

#### How to package C++ code as rpm? 

1. Compile the code for the appropriate architecture(s). (See above) 
1. Deploy the artifact to a repository manager. (currently not working, todo add ref to jira) 
1. Use unix-maven-plugin to create the rpm. **TODO**: pom example 

#### How to make the output of a shell command available to Maven?

If you cannot use any of the predefined properties mentioned in [Java System Properties](http://www.sonatype.com/books/maven-book/reference/resource-filtering-sect-system-properties.html) or [Codehaus Maven Properties Guide](http://docs.codehaus.org/display/MAVENUSER/MavenPropertiesGuide), you might need to extract the information yourself. The following example shows how to fetch the version number of a linux distribution from /etc/issue: 

- Example: [How to make the output of a shell command available to Maven?](How-to-make-the-output-of-a-shell-command-available-to-Maven.md)

**TODO**: This should probably be supported in a plugin. Which? Should update with reference to jira issue. 

#### Running Jetty
Early versions of the Maven Jetty plugin was named _maven-jetty-plugin_, and would run as expected, e.g.
**>mvn jetty:run**
its pom.xml:
```xml
<plugin>
    <groupId>org.mortbay.jetty</groupId>
    <artifactId>maven-jetty-plugin</artifactId>
    <version>6.0.2</version>
</plugin>
```

Later versions (from 7) changed the plugin's name to conform to Maven convention, into _jetty-maven-plugin_,  but now the expected  'mvn jetty:run' will not run!
The [documentation](http://docs.codehaus.org/display/JETTY/Maven+Jetty+Plugin) explains the use of <pluginGroups>, in effect similar to prefixing the _run_ with the groupid and complete plugin name:
**>mvn org.mortbay.jetty:jetty-maven-plugin:run**
Its pom.xml
```xml
<plugin>
    <groupId>org.mortbay.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <version>7.0.0.pre5</version>
</plugin>
```
