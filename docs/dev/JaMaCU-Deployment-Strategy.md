# JaMaCU Deployment Strategy

###### Motivation

Developers and architects have too long neglected the needs of system administration. The excuses   
vary, but the symptoms are much the same;

- Complex and time consuming deployments.
- Complex and error prone configuration.
- Too much, too little or just plain bad logging.
- Poor or missing exception management.
- "I do it my way" instead of "I do it the standard way".
- Little or poor communication between sysadmins and developers.
- etc.

**Enough with the excuses!**   
We will here explain what we consider to be good practices for integrating and collaborating with system administrators and their systems and processes.

###### Goals

- Make it easy to deploy an application in a new environment.
- Describe a solution for Configuration Management based on sound [SOA ] principles and open source software.
- Describe the relevant solutions and means we need to solve the most painful problems.

###### Prerequisites and assumptions

The documentation and examples are written in a Java and Unix/Linux context. While most of the ideas can (/ought to be) possible on Windows, we have opted to complete an end-to-end solution on one platform before expanding to multiple platforms. We have also chosen Confluence for documentation, Maven as build system and unix-maven-plugin for packaging.

The strategy is therefore called **JaMaCU** (Java, Maven, Confluence, Unix-maven-plugin).

|  |  |
| --- | --- |
| Table of Contents  - [Maven-based Software Release](/web/20210226151640/https://wiki.cantara.no/display/dev/Maven-based+Software+Release "Maven-based Software Release")  - [Installation and Deployment Automation](/web/20210226151640/https://wiki.cantara.no/display/dev/Installation+and+Deployment+Automation "Installation and Deployment Automation")  - [Confluence-based Documentation Release](/web/20210226151640/https://wiki.cantara.no/display/dev/Confluence-based+Documentation+Release "Confluence-based Documentation Release")  - [ConfigService](/web/20210226151640/https://wiki.cantara.no/display/JAU/ConfigService "ConfigService") - [Logging](/web/20210226151640/https://wiki.cantara.no/display/dev/Logging "Logging") - [Error Handling And Exception Management](/web/20210226151640/https://wiki.cantara.no/display/dev/Error+Handling+And+Exception+Management "Error Handling And Exception Management")   - [States of a distributed application](/web/20210226151640/https://wiki.cantara.no/display/dev/States+of+a+distributed+application "States of a distributed application")  - [SysAdmin Production Toolbox](/web/20210226151640/https://wiki.cantara.no/display/dev/SysAdmin+Production+Toolbox "SysAdmin Production Toolbox")   **Legend**   - documentation good enough as guide   - documentation NOT good enough as guide | JaMaCU_graphical_overview |
