# Basic configuration tactics

## Arguments, variables, options and properties

The traditional approach to make an application is to extract relevant properties and put them in external property files. Setting environmental variables or command-line arguments are two other approaches. The following table gives an overview. 

| Type | Get | Set |  |
| --- | --- | --- | --- |
| [Command-Line Arguments | http://java.sun.com/docs/books/tutorial/essential/environment/cmdLineArgs.html] | just fetch from args in the main method: public static void main (String[] args) | java Sort **friends.txt**, where Sort is the application and friends.txt is a command-line argument. |  |
| [java options - standard options | http://java.sun.com/j2se/1.5.0/docs/tooldocs/solaris/java.html] | ManagementFactory.getRuntimeMXBean().getInputArguments() | java **-Xms1024m  -Xmx1024m** Sort |  |
| [java options - system property value | http://java.sun.com/j2se/1.5.0/docs/tooldocs/solaris/java.html] | System.getProperty(key) | java **-Dproperty=value** Sort |  |
| [System Properties | http://java.sun.com/docs/books/tutorial/essential/environment/sysprop.html] | System.getProperty("path.separator"); | System.setProperties(new Properties(System.getProperties())); |  |
| [Environment Variables | http://java.sun.com/docs/books/tutorial/essential/environment/env.html] | System.getEnv | export $ENV=environmentA (linux), set ENV=environmentA (windows) |  |

## File-based approaches

#### Load properties from a .properties file 

- Get from classpath
[Smartly load your properties - Classpath resources](http://www.javaworld.com/javaworld/javaqa/2003-08/01-qa-0808-property.html?page=2)

- Get from a jar file:
```
Properties properties = new Properties();
InputStream in = FileLoader.class.getClassLoader().getResourceAsStream("filename.properties");
if (in != null) {
    properties.load(in);
}
```

- Get from filesystem: 
```
Properties properties = new Properties().load(new FileInputStream("filename.properties"));
```

\\
- Set: properties.store(new FileOutputStream("filename.properties"), null);

#### Read and write files 

Use [Apache Commons-IO](http://commons.apache.org/io/description.html) 

## Configuration in Spring 

[Advanced Spring configuration](Advanced-Spring-configuration.md) 
[Chapter 4: Resources](http://static.springframework.org/spring/docs/2.5.x/reference/resources.html)
[PropertyConfigurers](http://static.springframework.org/spring/docs/2.5.x/reference/beans.html#beans-factory-extension-factory-postprocessors) 

**TODO** 
Many use Spring to load property-files during application context initialization. Can this be achieved by extending [PropertyOverrideConfigurer](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/beans/factory/config/PropertyOverrideConfigurer.html) and [PropertyPlaceholderConfigurer](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/beans/factory/config/PropertyPlaceholderConfigurer.html)? 

If beans that need properties from external property-files are set to _lazy-init_, it is possible to load properties manually after application context initialization, but before the properties are actually used in the relevant beans. 

## Apache Commons Configuration 

[Apache Commons Configuration](http://commons.apache.org/configuration)
[SpringModules Commons support](https://springmodules.dev.java.net/docs/reference/0.7/html/commons.html)
[Using Spring and Commons Configuration - an example](http://forum.springframework.org/showthread.php?t=57246)

## Load configuration from multiple sources with a priority

Properties can come from multiple sources, and it is necessary to prioritize the different sources. 

Initial suggestion: 

1a. Properties loaded from a path given as part of the command-line 
1b. Properties loaded from default path
2. From ConfigService 
3. From deployed jar file 

Choosing the correct property files is easy when properties are loaded during the applications life-cycle. 

## Load properties directly from a database 

Don't?
