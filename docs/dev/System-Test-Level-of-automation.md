# System Test - Level of automation

### Introduction 
There are in general three main system test categories; automated, semi-automated and manual. The distribution between test types may vary, but in any non-trivial system there will always be some parts of the system which will never be automatically tested. Thus, while we must always strive for a high degree of automation, we must accept that some things will be too costly or are just too difficult to automate.

As in many other aspects of software engineering, we make a distinction between systems that span multiple nodes/computers and single-node systems. In the following we will assume a **multi-node system**. 

First, choose carefully what you _want_ to test with a system test. If something can be tested with a unit or service test, do so. It is a lot easier and cheaper. The next thing to consider is whether a certain function or aspect is best tested with a automated test or tested manually. 

When it comes to automating the system tests you have decided to try to automate, there are two more dimensions you need to consider. 

1. **Manual** vs **automated deployment and configuration** 
1. **Automated test scripts run manually** vs **fully automated test runs**. The differences might seem subtle, but many of the tools available is limited to the latter. It is therefore important to avoid tools which are not meant to be fully automated if that is your goal. 

### Fully automated test runs, but manual deployment 

1.  Automate routines and scripts to ensure a _reproducible_ base system setup
    - Ensure that each _base system_ setup is identical by using a image or script based approaches.
    - Automate the installation/deployment routines for external packages like for example Java JRE. 

2. Isolate the system from "noise" from users and other systems
    - Tactics: [sysadm:DNS Environment Enclaves](../sysadm/DNS-Environment-Enclaves.md), vlan and firewall. 

3.  Ensure reproducible tests 
    - Create [rpm](RPM-based-Installation.md), dpkg, pkg packages for your applications to automate their installation.
    - Document the configuration and put the configuration for the whole system under **version control**. Tip: [ConfigService](ConfigService.md) is an elegant solution to this requirement. 

4. Automate the test runs 
    - Test can be started automatically by for example cron or a CI server or initiated manually. 

### Brainstorming and questions to be solved 

##### Deployment 

- Should we automate installation of Operating system, java, users and groups, etc.? 
    - Virtualization makes automation of this process feasible. 

- How to automate deployment to Linux-based systems given rpm packages? 
    - Always use latest release from a repo? 
    - Let the test decide which rpm package and use bash or similar scripting to do the deployment? (Fragile) 

- What options are available for automated deployment to Windows nodes? 
  
- Can be automate deployment of _some_ deployment units and not everyone? 

##### Configuration 

Automating the deployment is of little value unless we also can control the configuration. 

It might thus seem reasonable to implement a configuration management system before fully automating the deployment process. [Constretto](http://constretto.org/) seems like a good starting point, because it supports multi-dimensional configurations.
