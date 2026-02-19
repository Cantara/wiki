# Continuous Integration Server Overview

## Introduction

There are plenty of CI servers to choose from. We have selected the three from the five most popular from the following poll: 
[Poll: What Continuous Integration Server are you using in 2008?](http://www.wakaleo.com/polls/18<sub>~what</sub><sub>continuous</sub><sub>integration</sub><sub>server</sub><sub>are</sub><sub>you</sub><sub>using</sub>~in-2008)

and tried to give a rough overview of pros and cons. Note that all three solve the basic task of automating builds, so which server to choose is a matter of personal taste and which properties the development team values the most. 

## Top three CI servers

- [Continuum](http://maven.apache.org/continuum/)
-* (+) Open Source
-* (+) Easy to install
-* (+)(+) Gathers 99% of necessary information from the {}. Easy to initate new projects.
-* (+)(+) Allows grouping of projects (and configuration per group)
-* (+)(+) Easy to set up different kinds of builds in the same project (Build Definitions)
<sub>~* (+)(+) Supports maven</sub>~release from GUI
-* (+) Large community
<sub>~* (</sub>~) Poorly documented
<sub>~* (</sub>~) Used to release very seldom
<sub>~* (</sub>~) Cross-version migration issues

- [Hudson](https://hudson.dev.java.net/)
-* (+) Open Source
-* (+) Easy to install
-* (+)(+) [Lots of plugins](http://hudson.gotdns.com/wiki/display/HUDSON/Plugins)
<sub>~* (+) Good REST</sub>~api
-* (+)(+) Supports slave agents (easy to set up too)
-* (+) Frequent releases and great deployment mechanisms (WebStart for instance) 
-* (+) Quick and snappy pages
-* (+) Good console output
<sub>~* (</sub>~)(-) Each job (project) must be configured from scratch. Duplicates configuration when having many jobs for one project (can copy, but not share)
<sub>~* (</sub>~) Doesn't scale with number of archived builds (having too large history will slow Hudson down as reports are based on numerous xml files)

- [Bamboo](http://www.atlassian.com/software/bamboo/) 
-* (+)(+) Good documentation
-* (+)(+) Tidy configuration
-* (+) Very easy installation procedure
-* (+) Solid and enterprisey, scales well into many many projects (distributed builds on agents)
-* (+) Excellent reporting and output capabilities
<sub>~* (+) Supports Continuum</sub>~like multpiple "plans" for a single project (prevents config duplication)
<sub>~* (</sub>~) Commercial(but not that expensive really)
<sub>~* (</sub>~) Aquired taste: Not immediately intuitive GUI

## Others

- [TeamCity](http://www.jetbrains.com/teamcity/)
-* (+)  God integrasjon med IntelliJ
<sub>~* (</sub>~) Commercial
- [CruiseControl](http://cruisecontrol.sourceforge.net/) - gammel og akterutseilt, bør ikke velges for nye prosjekter
-* (+) Open Source
- [Anthill OS](http://www.anthillpro.com/html/products/anthillos/default.html)
-* (+) Open Source
- [Luntbuild](http://luntbuild.javaforge.com/)
-* (+) Open Source
- [Apache Gump](http://gump.apache.org/)
-* (+) Open Source
- [QuickBuild (Luntbuild professional)](http://www.pmease.com)
<sub>~* (</sub>~) Commercial
- [AnthillPro](https://www.anthillpro.com)
<sub>~* (</sub>~) Commercial
- [Pulse](http://www.zutubi.com/products/pulse/)
<sub>~* (</sub>~) Commercial
- [Parabuild](http://www.viewtier.com/products/parabuild/)
<sub>~* (</sub>~) Commercial

## Resources
[http://confluence.public.thoughtworks.org/display/CC/CI+Feature+Matrix](http://confluence.public.thoughtworks.org/display/CC/CI+Feature+Matrix) (previously hosted at [codehaus](http://damagecontrol.codehaus.org/Continuous+Integration+Server+Feature+Matrix))
- [Quick video introduction to Hudson](http://blog.objectmentor.com/articles/2008/12/11/hudson<sub>~a</sub><sub>very</sub><sub>quick</sub>~demo)
