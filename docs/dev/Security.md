# Security

|  | The intentions for this space is to highlight problems, solutions and what to (not) do. |

- [Attackers](/web/20210306085326/https://wiki.cantara.no/display/dev/Attackers "Attackers") This section will contain a short description of the types of attackers out there.
- [Attacks](/web/20210306085326/https://wiki.cantara.no/display/dev/Attacks "Attacks") This section will describe known attacks and their enablers.
- [Strategy concepts and best practices](/web/20210306085326/https://wiki.cantara.no/display/dev/Strategy+concepts+and+best+practices "Strategy concepts and best practices") This section will examine the broader concepts of security, the common denominators of successful security management.
- [Standard security measures](/web/20210306085326/https://wiki.cantara.no/display/dev/Standard+security+measures "Standard security measures") This section is the hands-on section where well known measures are described and where open source implementations exists, they will be presented.
- [Environment](/web/20210306085326/https://wiki.cantara.no/display/dev/Environment "Environment") This section discusses does not discuss green house effects, rather other potentially harmful effects of the environment where web applications reside.
- [Security Resources](/web/20210306085326/https://wiki.cantara.no/display/dev/Security+Resources "Security Resources") This section lists resources available on the web; well written articles and different security organisations.

- [IoT Security](/web/20210306085326/https://wiki.cantara.no/display/dev/IoT+Security "IoT Security")

## Webapp security

Webapplication security is much more than just firewalls and SSL. It's the practice of **building security in**. Basically the idea is that it's difficult/impossible to secure an application by putting up a defensive parameter (Hard shell, soft core approach). The main reason this won't work is because it is so difficult to put up a complete defense. Instead the application should be able to handle attacks without falling apart.

### The underlying problems

Below are some reasons webapp security is difficult:

- Easy access, potential attackers can reside anywhere in the world. The attack surface cannot be controlled and is large.
- Often will Webapps be a frontend or interface for other systems that were not intended to be accessable on a network, like old banking applications. These applications are not developed with a focus on security and are often complex, making it difficult to assess potential security issues. This means that the webapp may be the last line of defence for these systems.
- Developers are generally not educated in the field of software security and todays development techniques has'nt incorporated security as a part of the process.
- Webapps will typically interact with users, other systems and depend upon servers that runs other applications. A weakness in other systems or applications can therefore give attackers a different attack vector and circumvent security measures which were based upon assumptions about the environment.

### Different sources and how security should be incorporated into practice.

- [Web framework security tactics](/web/20210306085326/https://wiki.cantara.no/display/dev/Web+framework+security+tactics "Web framework security tactics") How frameworks should be handled.

- [OWASP Top Ten](http://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)  Project that maintains the ten most serious web application vulnerabilities.

- [Incorporating best security practices in development](/web/20210306085326/https://wiki.cantara.no/display/dev/Incorporating+best+security+practices+in+development "Incorporating best security practices in development")

- [Tomcat production setup](/web/20210306085326/https://wiki.cantara.no/display/dev/Tomcat+production+setup "Tomcat production setup")
