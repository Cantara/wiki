# JMeter tutorial

#### Fix plugin 

- Download [Updated maven<sub>~jmeter</sub><sub>plugin](http://files.myopera.com/mateamargo/blog/maven</sub><sub>jmeter</sub>~plugin.zip)

- Add the changes described [here](http://wiki.apache.org/jakarta-jmeter/JMeterMavenPlugin) to the _updated_ version of the plugin downloaded earlier. Build and install. 

#### Set up the test project 

- Install support jars as described by Ron Alleva in [Maven JMeter Plugin](http://www.ronniealleva.org/index.php/maven<sub>~jmeter</sub>~plugin/)

- Download [JMeter distribution](http://jakarta.apache.org/site/downloads/downloads_jmeter.cgi). 

- Create the following file structure

```
|-- bin
|   `-- upgrade.properties
|-- pom.xml
|-- src
|   |-- site
|   |   `-- site.xml
|   `-- test
|       |-- jmeter
|       |   |-- app1-testplan.jmx
|       |   `-- jmeter.properties
|       `-- resources
|           |-- jmeter-results-detail-report_21.xsl
|           `-- jmeter-results-report_21.xsl
```

    - `upgrade.properties, jmeter.properties, jmeter<sub>~results</sub>~detail-report_21.xsl` and {} can all be found in the [JMeter distribution](http://jakarta.apache.org/site/downloads/downloads_jmeter.cgi). 

    - [JMeter pom.xml](JMeter<sub>~pom</sub>~xml.md)

    - JMX files must be generated (and updated) using JMeter desktop application. 

    - site.xml 
```xml
<project name="App1 Performance Tests">
  <body>    
    <menu name="Test reports">
      <item name="app1-testplan" href="/jmeter-results/app1-testplan/"/>
    </menu>
    <menu ref="reports" />
  </body>
</project>
```

Note! Make sure the log_file.jmeter property in jmeter.properties is NOT set: #log_file.jmeter=jmeter.log

#### Resources 

###### Continuous integration 
http://wiki.hudson-ci.org/display/HUDSON/JMeter+Plugin

https://svn.softwareboersen.dk/sosi/tags/release<sub>~1.5.6/modules/maven</sub><sub>jmeter</sub><sub>report</sub>~plugin/pom.xml
http://www.theserverlabs.com/blog/2009/04/23/performance<sub>~tests</sub><sub>with</sub><sub>jmeter</sub><sub>maven</sub><sub>and</sub>~hudson/

Other xsl: http://www.programmerplanet.org/pages/projects/jmeter<sub>~ant</sub>~task.php

###### Tutorials and howtos 

[http://jakarta.apache.org/jmeter](http://jakarta.apache.org/jmeter)
[http://code.google.com/p/jmeter<sub>~maven</sub><sub>plugin/downloads/list](http://code.google.com/p/jmeter</sub><sub>maven</sub>~plugin/downloads/list)

[Automated Performance Tests using JMeter and Maven](http://jlorenzen.blogspot.com/2008/03/automated<sub>~performance</sub>~tests-using.html) by James Lorenzen

[Maven JMeter plugin and report generation (the last steps to get it working)](http://technology.amis.nl/blog/2364/getting<sub>~the</sub><sub>maven</sub><sub>jmeter</sub><sub>plugin</sub><sub>working</sub><sub>and</sub><sub>generating</sub><sub>a</sub><sub>report</sub><sub>the</sub><sub>last</sub>~steps) by Robbrecht van Amerongen

[A better JMeter Maven plugin](http://www.ronniealleva.org/index.php/2008/12/22/a<sub>~better</sub><sub>jmeter</sub><sub>maven</sub>~plugin/) by Ron Alleva
[Maven JMeter Plugin](http://www.ronniealleva.org/index.php/maven<sub>~jmeter</sub>~plugin/) by Ron Alleva

http://www.nabble.com/JMeter<sub>~Maven</sub><sub>and</sub><sub>JMeter</sub><sub>TestNG</sub><sub>contribution</sub>~td18468606.html
