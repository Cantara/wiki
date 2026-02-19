# Webapp deployment from RPM

#### Requirements to war archive 
- Must be released with maven and deployed to a repository.
- No jetty specific configuration in the war (i.e no WEB<sub>~INF/jetty</sub>~web.xml file).

#### Jetty configuration 

xml-file examples
[{}](jetty-xml.md) - The main configuration file where the jetty server properties are set.
[{}](jetty<sub>~logging</sub>~xml.md) - Configure the logging.
[{}](myWebapp-xml.md) - Individual configuration for each application deployed on the server. Is only read when using the ContextDeployer.

contexts 
- To be able to specify individual configuration parameters for the different webapps deployed on the server use the {}.
- The {} configuration in {} specifies where to look for application context configurations (defaults to {} folder)
- By default the ContextPath of a deployed WAR equals the name of the war file. This is not desirable since the war file can (and will) change its name and we do not want to change the contextpath of the application. 
- To statically set the context path create a configuration file in the contexts folder and set the desired path. See the example file ([myWebapp.xml](myWebApp-xml.md)).

logging 

set different default port for each application 
Port is specified in jetty.xml `<Set name="port">`

Security? 
Using SSL? http://docs.codehaus.org/display/JETTY/How+to+configure+SSL

#### RPM setup 

pom.xml example 

appConfig
