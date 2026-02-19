# Webapp deployment from RPM - scratch area

#### Strategy 1: add war archive to a pre-installed webserver 

Typically multiple webapps in one instance of WebSphere, Weblogic, Tomcat (or Jetty). 
cargo-maven-plugin? 
was-m-p? 
etc. 

Distribution as war or ear. 
Requires a preconfigured webserver. 
Probably not easy to automate, since you cannot know upfront which webapps will be running there. 
Possible to use JNDI and share resources etc. 

It should be possible to use the dependency functionality of RPM together with yum to let [jetty rpm](http://docs.codehaus.org/display/JETTY/Using+the+Jetty+RPMs) be a transitive dependency of the webapp. This seems like a good idea, since we can then let Mortbay maintain the jetty rpms while still get full automation. 

#### Strategy 2: Bundle a lightweight servlet container with the distribution 

Reduce complexity, since each webapp can be configured and deployed in isolation from the rest. Easiest to fully automate. 

###### Wanted status 

Automated installation/deployment of servlet container 
Automated configuration of servlet container 
Automated deployment of war file 
Automated upgrade of servlet container 
Automated upgrade of app 
Automated removal of servlet container and app

#### Proposed solution 
Bundle jetty + jettyConfig + appConfig + war file in a rpm. 

Example: [archiva](http://svn.apache.org/viewvc/archiva/trunk/archiva-jetty/pom.xml?revision=746186&view=markup) 

- Install jetty as a standalone servlet container
    - it's not installed, just laid out in a directory with jsw and ready to go 
    - minimal jetty is _start.jar_ and _jetty.jar_
- Add/change configuration if needed 
    - Separate jetty config from webapp config. 
- Dump the war file into jettys hotfolder 
- Add symlinks to start scripts or the actual scripts to /etc/init.d to make the webapp start at boot.

#### Questions 

When is each strategy appropriate? 

Advantages and disadvantages of each?
