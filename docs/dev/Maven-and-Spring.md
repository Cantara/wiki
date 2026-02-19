# Maven and Spring

#### How to share configuration between Spring and Maven 

See [Deploy to different environments - run<sub>~time](Deploy</sub><sub>to</sub><sub>different</sub><sub>environments</sub><sub>run</sub><sub>time.md) and [configuration</sub><sub>management</sub><sub>with</sub><sub>spring](http://blog.arendsen.net/index.php/2005/03/12/configuration</sub><sub>management</sub><sub>with</sub>~spring/) for examples on what's possible. 

###### Filtering in Maven 
Use filtering to easily set a different set of properties according to environment. 

(+) Provides the same functionality for pom.xml as PropertyOverrideConfigurer and PropertyPlaceholderConfigurer does for the application context. 
(-) "MavenMagic"

###### Maven Profiles 
Use system properties or profile name to activate and disable profiles. One profile per environment can be used to easily switch between environments. 

(+) Flexible 
(-) Too flexible, so often misused with high complexity as a result 
(-) "MavenMagic"

###### How to avoid duplication between Maven projects and Maven modules

See [Organizing Maven projects](Organizing<sub>~Maven</sub>~projects.md)

###### How to use different web.xml files in different environments

See 
[webxml in war<sub>~plugin](../ttp/maven</sub><sub>apache</sub><sub>org</sub><sub>plugins</sub><sub>maven</sub><sub>war</sub><sub>plugin</sub><sub>exploded</sub><sub>mojo</sub>~html-webXml.md)
[BluePrints: maven profiles](http://altuure.blogspot.com/2006/11/maven-profiles.html)
