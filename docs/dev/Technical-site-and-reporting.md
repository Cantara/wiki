# Technical site and reporting

## Technical Site and reporting 

_Reporting_ is implemented by "_Plugins which generate reports, are configured as reports in the POM and run under the site generation lifecycle._". The tables below show some of the most popular of these plugins. 

###### From the official [plugin overview](http://maven.apache.org/plugins/index.html):
| Name | Description |  |
| --- | --- | --- |
| [changelog | http://maven.apache.org/plugins/maven-changelog-plugin/] | Generate a list of recent changes from your SCM. |
| [changes | http://maven.apache.org/plugins/maven-changes-plugin/] | Generate a report from issue tracking or a change document. |
| [checkstyle | http://maven.apache.org/plugins/maven-checkstyle-plugin/] | Generate a checkstyle report. |
| [clover | http://docs.atlassian.com/maven-clover2-plugin/2.3.1/] | Generate a Clover report. |
| [doap | http://maven.apache.org/plugins/maven-doap-plugin/] | Generate a Description of a Project (DOAP) file from a POM. |
| [docck | http://maven.apache.org/plugins/maven-docck-plugin/] | Documentation checker plugin. |
| [javadoc | http://maven.apache.org/plugins/maven-javadoc-plugin/] | Generate Javadoc for the project. |
| [jxr | http://maven.apache.org/plugins/maven-jxr-plugin/] | Generate cross-referenced source code for easy navigation in a browser |
| [pmd | http://maven.apache.org/plugins/maven-pmd-plugin/] | Generate a PMD report. |
| [project-info-reports | http://maven.apache.org/plugins/maven-project-info-reports-plugin/] | Generate standard project reports. |
| [surefire-report | http://maven.apache.org/plugins/maven-surefire-report-plugin/] | Generate a report based on the results of unit tests. |

###### Others

| [Taglist | http://mojo.codehaus.org/taglist-maven-plugin/] | Generate a list of tasks based on tags in your code. E.g. TODO, FIXME etc. |
| [JDepend | http://mojo.codehaus.org/jdepend-maven-plugin/]Generate a list of tasks based on tags in your code.] | Module/library dependency report |
| [Cobertura | http://mojo.codehaus.org/cobertura-maven-plugin/] | Test code coverage report |
| [SchemaSpy | http://maven-plugins.sourceforge.net/maven-schemaspy-plugin/] | documentation for your database |

#### How to get graphical UML diagrams in the javadoc

- Install graphviz in Debian (apt) based systems 
```
aptitude install graphviz
```

- Install Graphviz on CentOS 4.6
```
yum install libtool-libs
yum install urw-fonts
wget http://www.graphviz.org/pub/graphviz/ARCHIVE/graphviz-2.18-1.el4.i386.rpm 
```

See [graphviz.org](http://www.graphviz.org/Download..php) for details on what to put in the pom and for binaries for other distributions. 

[Java Parent POM Example](Java-Parent-POM-Example.md) contains an example configuration which adds the UML class diagrams to the javadoc. 

## Resources 

[Apache Maven plugins](http://maven.apache.org/plugins/index.html) 
[Mojo Codehaus](http://mojo.codehaus.org/plugins.html)
[Sonar](http://sonar.codehaus.org/) is an open source enterprise quality control tool. Collects metrics from multiple Maven projects.
