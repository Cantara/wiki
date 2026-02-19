# RPM Deployment with Java Service Wrapper

## Requirements 

- Artifact must be deployed to a Maven repository. See [Enterprise Maven Infrastructure](Enterprise<sub>~Maven</sub>~Infrastructure.md) for details. 
- Jar project is assumed and mainClass must be set up. (Have not tried other artifact types.) 
- Artifact does not need build-time configuration. 

## How 

- Generate Java Service Wrapper scripts with maven<sub>~appassembler</sub>~plugin

- Generate rpm package with dependencies, scripts and configuration 

- Make the rpm user friendly 
    - Create a symlink in /etc/init.d/
    - Set up runlevels
    - chown and chmod according to $RUN_AS_USER system variable.
    - Clean up when the package is removed. 

See [Example JSW and RPM](Example<sub>~JSW</sub>~and-RPM.md) for pom.xml configuration. 

## Resources 

- [appassembler<sub>~maven</sub><sub>plugin](http://mojo.codehaus.org/appassembler/appassembler</sub><sub>maven</sub>~plugin/)

- [Java Service Wrapper (JSW)](http://wrapper.tanukisoftware.org)
 
- [unix<sub>~maven</sub><sub>plugin](http://cobain.arktekk.no/</sub>trygvis/hg/unix/)

- [rpm<sub>~maven</sub><sub>plugin](http://mojo.codehaus.org/rpm</sub><sub>maven</sub>~plugin/)
    - [rpm<sub>~maven</sub><sub>plugin](http://mojo.codehaus.org/rpm</sub><sub>maven</sub>~plugin/)
    - http://svn.apache.org/repos/asf/archiva/trunk/archiva-jetty/pom.xml
    - [Jetty pom<sub>~xml (use rpm</sub>~plugin with init-scripts)](http://jira.codehaus.org/secure/attachment/26488/pom.xml) 
    - [rpm<sub>~maven</sub><sub>plugin with multiple modules](rpm</sub><sub>maven</sub><sub>plugin</sub><sub>with</sub>~multiple-modules.md)

- RedHat and RPM resources 
    - [RPM, %config, and (noreplace)](http://www-uxsup.csx.cam.ac.uk/~jw35/docs/rpm_config.html)
    - [RPM at Idle](http://www.rpm.org/RPM-HOWTO/) 
    - [Scripts: RPM's Workhorse](http://www.rpm.org/max<sub>~rpm/s1</sub><sub>rpm</sub><sub>inside</sub>~scripts.html)
    - [How To Create RPMs and Init Scripts That Are Compatible On Both SUSE Linux and Red Hat Linux](http://www.novell.com/coolsolutions/feature/11256.html)
    - [Redhat run levels](http://www.chinalinuxpub.com/doc/www.siliconvalleyccie.com/linux-hn/runlevels.htm)
