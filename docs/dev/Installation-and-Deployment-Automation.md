# Installation and Deployment Automation

#### Goals and drivers

- Same artifact (primary artifact, can have multiple distribution artifacts) should be deployed to all environments, build-time configuration is unacceptable.
- The number of manual steps required to deploy should be kept at a bare minimum. => minimize the number of *required* settings + automate as much as possible
- System administrators need to monitor and tweak the application to best utilize the production environment.
- Support multiple environments (e.g test, pre-prod and production)

#### Available strategies

There are two approaches when generating deployment archives/packages; create native installation packages that integrate closely with the operating system or try to create one generic package that supports multiple platforms. Java can be run on any platform, so a single deployment package that can be used on all platforms would be nice. The straight-forward approach is to generate an archive (e.g. zip or tar.gz) and add start and stop scripts for multiple platforms. Some manual steps can be avoided by using [Deploy application with Java Network Launching Protocol (JNLP)](/web/20230531234658/https://wiki.cantara.no/display/dev/Deploy+application+with+Java+Network+Launching+Protocol+%28JNLP%29 "Deploy application with Java Network Launching Protocol (JNLP)") for deployment, but JNLP is designed for client applications and is not well-suited 24/7 server applications as the support for running the application as a service/daemon is poor.

See following tables for an overview:

|  | Archive | JNLP | Native installation packages |
| --- | --- | --- | --- |
| Platform independent |  |  |  |
| Simple to use. |  |  |  |
| Simple to setup. |  |  |  |
| Tool support for setting it up as a service/daemon |  |  |  |
| Tool support for pre and post installation scripts. |  |  |  |
| Tool support for removing the application |  |  |  |
| Built-in distribution mechanism |  |  |  |
| Built-in auto-upgrade mechanism |  |  |  |
| Method known by both developers and system administrators |  |  |  |

Read more

- [Deploy application with Java Network Launching Protocol (JNLP)](/web/20230531234658/https://wiki.cantara.no/display/dev/Deploy+application+with+Java+Network+Launching+Protocol+%28JNLP%29 "Deploy application with Java Network Launching Protocol (JNLP)")

- [Deploy application with native packages](/web/20230531234658/https://wiki.cantara.no/display/dev/Deploy+application+with+native+packages "Deploy application with native packages")

#### Other Resources

Reference to other people that might think similar to us, but not quite.   
[Automated Deployment Resources](/web/20230531234658/https://wiki.cantara.no/display/dev/Automated+Deployment+Resources "Automated Deployment Resources")
