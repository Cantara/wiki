# Pull deployment script for Windows

#### Prerequisites 

- Application use Java Service Wrapper. 

- Packaged as zip file

#### Download script - pseudo code
1. Input version to deploy. Latest = "latest" [Command line input windows](Command<sub>~line</sub>~input-windows.md)
1. Find latest version in repository [Find latest version in NEXUS repo](Find<sub>~latest</sub><sub>version</sub><sub>in</sub>~NEXUS-repo.md)
1. Compare version installed with latest. [Text compare in Windows](Text<sub>~compare</sub>~in-Windows.md)
    1. Do nothing (print info message to screen) if file name and file size is identical to current. 
1. Download zip file from Nexus [Download latest Artifact from Nexus](Download<sub>~latest</sub><sub>Artifact</sub><sub>from</sub>~Nexus.md) (/)
1. Unzip 
1. Copy configuration folders from old service. 
1. Execute stop and uninstall service 
1. Execute install and start scripts/windows service see [Download latest Artifact from Nexus](Download<sub>~latest</sub><sub>Artifact</sub><sub>from</sub>~Nexus.md)
1. Print success message with info about service name, port, jmx port, logs folder 
1. Improvement: stop new service and start previous service if start up failed (check exit code)  

#### Full script 
- [Script to download and unpack - Windows](Script<sub>~to</sub><sub>download</sub><sub>and</sub>~unpack-Windows.md)

#### Download script - implementation tips

- Use a version control system 
    - installation scripts
    - installation property files 
    - binaries (curl, wget, etc) 
    - config_override 

- A single **generic installation script** for all installations. 

- A **separate installation property file** per installation 

###### Download 
Use wget or curl, should rely only on a single file, not on any installation. It is also possible to use powershell - http://superuser.com/questions/362152/native<sub>~alternative</sub><sub>to</sub><sub>wget</sub><sub>in</sub><sub>windows</sub>~powershell. 

#### Resources 

http://www.vectorsite.net/tsbatch.html

https://docs.sonatype.com/display/SPRTNXOSS/Nexus+FAQ#NexusFAQ-Q.HowcanIretrieveasnapshotifIdon%27tknowtheexactfilename%3F

http://mytechscratchpad.blogspot.no/2012/03/download<sub>~latest</sub><sub>snapshot</sub><sub>from</sub>~nexus.html

[Downloading artifacts from Nexus with bash](http://www.sonatype.com/people/2011/01/downloading<sub>~artifacts</sub><sub>from</sub><sub>nexus</sub>~with-bash/) 

[Windows XP batch help](http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/batch.mspx?mfr=true)

http://en.wikibooks.org/wiki/Guide_to_Windows_commands

http://www.askapache.com/windows/advanced<sub>~batch</sub>~scripting.html#PARAMTESTHELP_show_params_returns_CALLer
