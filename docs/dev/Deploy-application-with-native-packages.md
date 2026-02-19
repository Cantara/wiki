# Deploy application with native packages

#### Create unix packages 

We recommend using [Unix Maven Plugin](http://mojo.codehaus.org/unix/unix-maven-plugin/) to generate native packages (pkg, deb, rpm) for the Unix platform. See [Available native package systems](Available-native-package-systems.md) for other plugins and available Windows installers. 

###### Examples 

- [RPM Deployment with Java Service Wrapper](RPM-Deployment-with-Java-Service-Wrapper.md) 
- [RPM Deployment without Java Service Wrapper](RPM-Deployment-without-Java-Service-Wrapper.md) 
- [Webapp deployment from RPM](Webapp-deployment-from-RPM.md) 
- [RPM Deployment for C++ Applications](http://wiki.community.objectware.no/pages/viewpage.action?pageId=6488505), see also [Build C (plusplus) code for multiple platforms with Maven](Build-C-plusplus-code-for-multiple-platforms-with-Maven.md).

###### Synchronize package with repository manager / management system

[Synchronization between Maven repository and RPM repository](Synchronization-between-Maven-repository-and-RPM-repository.md)

#### Standardize setup 

Continuously improve the setup and processes and make sure the improvements propagate to all applications (if applicable). It _is_ important standardize across packages.
