# Test Frameworks and Tools

## Code-centric test tools

#### Unit Test oriented test tools

| Tool | M2-plugin | Type | Rating | Comment |
| --- | --- | --- | --- | --- |
| [TestNG](http://testng.org/) | [maven-surefire-plugin](http://maven.apache.org/plugins/maven-surefire-plugin/) | General purpose |  |  |
| [Junit4](http://www.junit.org/) | [maven-surefire-plugin](http://maven.apache.org/plugins/maven-surefire-plugin/) | Unit tests |  | Comparable to TestNG, but lacks support for groups. Backwards compatible with JUnit3. |
| [XmlUnit](http://xmlunit.sourceforge.net/) | none needed | Unit test XML |  | Use the utility classes |
| [Springs TestContext Framework](http://static.springframework.org/spring/docs/2.1.x/reference/testing.html#testcontext-framework) | none needed |  |  | Extends JUnit and TestNG. Injection of fixtures. Test grouping. Transaction control plus other utils. |
| [JUnit4 Extensions](http://junitext.sourceforge.net/) | unknown | unknown |  |  |
|  | [shitty-maven-plugin](http://mojo.codehaus.org/shitty-maven-plugin/) | Integration tests |  | The plugin provides a simple way to run integration tests for a project (single module or multi-module). |

#### RDBMS testing

| Tool | M2-plugin | Rating | Comment |
| --- | --- | --- | --- |
| [DBUnit](http://www.dbunit.org/) | [maven-dbunit-plugin](http://maven-plugins.sourceforge.net/maven-dbunit-plugin/) |  |  |
| [unitils](http://www.unitils.org/) |  |  |  |
|  | [sql-maven-plugin](http://mojo.codehaus.org/sql-maven-plugin/) |  |  |
|  | [hibernate3-maven-plugin](http://mojo.codehaus.org/maven-hibernate3/hibernate3-maven-plugin/) |  |  |
|  | [maven-hsql-plugin](http://www.javagen.com/maven-hsql-plugin) |  |  |

[Derby](http://db.apache.org/derby/papers/DerbyTut/embedded_intro.html)  embedded database  
[hsqldb](http://hsqldb.org/)

#### Mock Frameworks

| Tool | M2-plugin | Type | Rating | Comment |
| --- | --- | --- | --- | --- |
| [Mockito](http://mockito.org/) | none needed | Mock framework |  | Relatively new framework, improvement of EasyMock |
| [EasyMock](http://www.easymock.org/) | none needed | Mock framework |  |  |
| [jMock](http://www.jmock.org/) | none needed | Mock framework |  |  |

## Performance test tools

| Tool | Type | Opinions and notes |
| --- | --- | --- |
| [JMeter](http://jakarta.apache.org/jmeter/) | Load test functional behavior and measure performance | Maven plugin: [chronos](http://mojo.codehaus.org/chronos-maven-plugin/) |
| [The Grinder](http://grinder.sourceforge.net/) | load testing framework that makes it easy to run a distributed test using many load injector machines | ... |
| [Hudson Grinder Plugin](http://wiki.hudson-ci.org/display/HUDSON/Grinder+Plugin) |  | ... |
| [Perf4j](http://perf4j.codehaus.org/) | <http://www.infoq.com/articles/perf4j> | ... |

## Web tests

| Tool | Type | Opinions and notes |
| --- | --- | --- |
| [FITNesse](http://fitnesse.org/) | integrated standalone wiki, and acceptance testing framework |  |
| [GreenPepper](http://www.greenpeppersoftware.com/confluence/display/GPW/Home/) | executable specifications and automated functional testing |  |
| [Selenium](http://selenium.openqa.org/) | Web tests | See our [Selenium](/web/20210226162141/https://wiki.cantara.no/display/dev/Selenium "Selenium") notes |
| [Celerity](http://celerity.rubyforge.org/) | Web tests | JRuby/Watir wrapper around HTMLUnit, i.e. fast! |
| [CubicTest](http://cubictest.openqa.org/) | eclipse plugin for automatic acceptance testing of webapps |  |
| [WebDriver](http://code.google.com/p/webdriver/) | Web tests |  |

## Other test tools

| Tool | Type | Opinions and notes |
| --- | --- | --- |
| [FIT](http://fit.c2.com/) | Requirement/test mapper | Very popular tool. |
| [Concordian](http://www.concordion.org/) | Requirement/test-mapper | Like FIT, but better for Java |
| [JBehave](http://jbehave.org/) | Requirement/test-mapper | Java powered. Follows BDD |
| [RSpec](http://rspec.info/) | Requirement/test-mapper | Ruby powered. Follows BDD |
| [Cucumber](http://github.com/aslakhellesoy/cucumber/wikis) | Requirement/test-mapper | Rewrite of RSpec. Follows BDD |
| [MActor](http://mactor.sourceforge.net/) | Component level mock framework | Functional tests of any XML-based integration. |
| [PushToTest](http://www.pushtotest.com/) | Test Automation for Web Applications, Web Services, SOA, Ajax | ... |
| [SoapUI](http://www.soapui.org/) | Web Services Testing tool | ... |
| [BCT] | Backward Compatibility Tester, Continuum extension |  |
| [Testaco](http://testaco.org/) | data driven testing and database refactoring |  |
