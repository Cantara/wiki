# JMeter tutorial

#### Fix plugin 

- Download [Updated maven-jmeter-plugin](http://files.myopera.com/mateamargo/blog/maven-jmeter-plugin.zip)

- Add the changes described [here](http://wiki.apache.org/jakarta-jmeter/JMeterMavenPlugin) to the _updated_ version of the plugin downloaded earlier. Build and install. 

#### Set up the test project 

- Install support jars as described by Ron Alleva in [Maven JMeter Plugin](http://www.ronniealleva.org/index.php/maven-jmeter-plugin/)

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

    - `upgrade.properties, jmeter.properties, jmeter-results-detail-report_21.xsl` and {} can all be found in the [JMeter distribution](http://jakarta.apache.org/site/downloads/downloads_jmeter.cgi). 

    - [JMeter pom.xml](JMeter-pom-xml.md)

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

https://svn.softwareboersen.dk/sosi/tags/release-1.5.6/modules/maven-jmeter-report-plugin/pom.xml
http://www.theserverlabs.com/blog/2009/04/23/performance-tests-with-jmeter-maven-and-hudson/

Other xsl: http://www.programmerplanet.org/pages/projects/jmeter-ant-task.php

###### Tutorials and howtos 

[http://jakarta.apache.org/jmeter](http://jakarta.apache.org/jmeter)
[http://code.google.com/p/jmeter-maven-plugin/downloads/list](http://code.google.com/p/jmeter-maven-plugin/downloads/list)

[Automated Performance Tests using JMeter and Maven](http://jlorenzen.blogspot.com/2008/03/automated-performance-tests-using.html) by James Lorenzen

[Maven JMeter plugin and report generation (the last steps to get it working)](http://technology.amis.nl/blog/2364/getting-the-maven-jmeter-plugin-working-and-generating-a-report-the-last-steps) by Robbrecht van Amerongen

[A better JMeter Maven plugin](http://www.ronniealleva.org/index.php/2008/12/22/a-better-jmeter-maven-plugin/) by Ron Alleva
[Maven JMeter Plugin](http://www.ronniealleva.org/index.php/maven-jmeter-plugin/) by Ron Alleva

http://www.nabble.com/JMeter-Maven-and-JMeter-TestNG-contribution-td18468606.html
