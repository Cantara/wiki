# rpm-maven-plugin with multiple modules

To build RPM package from your java project (using Maven), the following maven plugin should be added to your POM file:
```xml
 <plugin>
   <groupId>org.codehaus.mojo</groupId>
   <artifactId>rpm-maven-plugin</artifactId>
   <version>2.0-beta-1</version>
 </plugin>
```

### Using RPM plugin with several modules
If your Maven project has several modules and your RPM packaging is done into the parent POM (root POM file), Maven RPM plugin will be called by all Maven modules. To avoid this, a specific module could be defined. This module would be used to defined the packaging (assembly plugin, rpm plugin, etc.) of the whole project. It will contain dependencies on required modules and define the needed RPM packaging. This configuration will avoid RPM plugin to be called by all Maven modules because its configuration is not anymore defined into the project parent POM, but only in a specifc module (application packaging module).
If, for some reasons (legacy), you need to define your RPM packaging into your parent POM, the following configuration should be done to avoid rpm-maven-plugin to be called by each module:

```xml
 <plugin>
   <groupId>org.codehaus.mojo</groupId>
   <artifactId>rpm-maven-plugin</artifactId>
   <version>2.0-beta-1</version>
 </plugin>
 <inherited>false</inherited>
 <executions>
   <execution>
     <inherited>false</inherited>
     <phase>install</phase>
     <goals>
       <goal>rpm</goal>
     </goals>
   </execution>
 </executions>
```

You should now launch your RPM packaging using _mvn install_ phase which is mapped to RPM plugin (_execution_ tag). This will run RPM plugin without executing it on each module (_inherited_ = false). Both _inherited_ configuration tag are needed to avoid RPM plugin execution on each Maven modules. If RPM packaging is run using _mvn rpm:rpm_ goal, rpm-maven-plugin will be executed on all modules (_inherited_ configuration will not be used).
