# Deploy application with native packages

#### Create unix packages 

We recommend using [Unix Maven Plugin](http://mojo.codehaus.org/unix/unix<sub>~maven</sub><sub>plugin/) to generate native packages (pkg, deb, rpm) for the Unix platform. See [Available native package systems](Available</sub><sub>native</sub>~package-systems.md) for other plugins and available Windows installers. 

###### Examples 

- [RPM Deployment with Java Service Wrapper](RPM<sub>~Deployment</sub><sub>with</sub><sub>Java</sub>~Service-Wrapper.md) 
- [RPM Deployment without Java Service Wrapper](RPM<sub>~Deployment</sub><sub>without</sub><sub>Java</sub>~Service-Wrapper.md) 
- [Webapp deployment from RPM](Webapp<sub>~deployment</sub>~from-RPM.md) 
- [RPM Deployment for C++ Applications](http://wiki.community.objectware.no/pages/viewpage.action?pageId=6488505), see also [Build C (plusplus) code for multiple platforms with Maven](Build<sub>~C</sub><sub>plusplus</sub><sub>code</sub><sub>for</sub><sub>multiple</sub><sub>platforms</sub><sub>with</sub>~Maven.md).

###### Synchronize package with repository manager / management system

[Synchronization between Maven repository and RPM repository](Synchronization<sub>~between</sub><sub>Maven</sub><sub>repository</sub><sub>and</sub><sub>RPM</sub>~repository.md)

#### Standardize setup 

Continuously improve the setup and processes and make sure the improvements propagate to all applications (if applicable). It _is_ important standardize across packages.
