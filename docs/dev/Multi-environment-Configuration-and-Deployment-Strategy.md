# Multi-environment Configuration and Deployment Strategy

WORK IN PROGRESS! 

#### Erik's notes: 

Document strategy for managing multiple environments. 

- Use JNLP for deployment in test environments to reduce deployment time to virtually nothing. 
    - [Deploy application with Java Network Launching Protocol (JNLP)](Deploy-application-with-Java-Network-Launching-Protocol-JNLP.md) 

- Use [ConfigService](ConfigService.md) to make it possible to manage all configurations from one user interface. 
    - ConfigService should provide diff functionality to make it possible to answer questions like: `What are the differences between test environmentA and production?` 

- Remember traceability and integration to Jira and/or HP Quality Center.  

- [sysadm:Virtualization](../sysadm/Virtualization.md) is crucial to keep the costs down. 

- [sysadm:Dynamic addressing with service names](../sysadm/Dynamic-addressing-with-service-names.md) is also required. 

---

## Deployment 

#### Requirements, drivers and goals 

- Automation 

- Support for running applications as daemons 
    - Start stop script 
    - Start at bootup 

- Short roundtrip-time for deploy of a new version 

#### Implementation

Make it possible to use either RPM packages OR [Deploy application with Java Network Launching Protocol (JNLP)](Deploy-application-with-Java-Network-Launching-Protocol-JNLP.md) with JNLPDownloadServlet for deployment. 

RPM for production (and for system administrators) and JNLP for test environments (testers and developers) is the general idea. 
The sequence for webstart is shown in [JNLP - deployment](http://wiki.community.objectware.no/display/smidigtonull/JNLP#JNLP-Howtouse)
A rough sketch of the deployment sequence for rpm is shown below. 
![configService-rpm](../images/gliffy/16515384-configService-rpm.png)

See also [RPM Deployment with Java Service Wrapper](RPM-Deployment-with-Java-Service-Wrapper.md) for how to generate the rpm packages with maven. 

## Logging

- Application should run with default log4j.xml file, but it must be possible to override it. 
    - Deployment (outputPath for logfile), usage (what and at what granularity) and can be both cluster-common and node specific. 
    - Put log4j.file in a jar and copy it to an a conf-folder on disk after first startup of a new version? Manually deleting this file will then result in a clean fetch from the jar when restarting the application. 

## Dynamic addressing 

See [sysadm:Dynamic addressing with service names](../sysadm/Dynamic-addressing-with-service-names.md)

## Virtualisation to keep the cost down 

[sysadm:Virtualization](../sysadm/Virtualization.md)

## Other needs that might need to be addressed by the same architecture 

- Need functionality for "forcing" a restart of a service. E.g., when a need version of a service it uses is deployed. **TODO**: Is this an appropriate location for this "reboot button"? Or can/should the webstart-webapp be used instead? 

- StartupChecker-helper which has functionality to check availability of shared resources like JMS-server, database (when db is used for integration instead of a Repository-approach), ESB, etc. This functionality should be split out into a separate project and shared between all applications/services that use these external services. This will ensure a more consistent startup phase and make it easier for system administrators to setup a complex environment. 

- Live migration of virtual machines (move a virtual machine between physical computers).
