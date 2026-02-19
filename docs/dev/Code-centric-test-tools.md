# Code-centric test tools

#### Unit Test oriented test tools 

| Tool | M2-plugin | Type | Rating | Comment |
| --- | --- | --- | --- | --- |
| [TestNG | http://testng.org] | [maven-surefire-plugin | http://maven.apache.org/plugins/maven-surefire-plugin/] | General purpose | (+)(+) |  |
| [Junit4 | http://www.junit.org/] | [maven-surefire-plugin | http://maven.apache.org/plugins/maven-surefire-plugin/] | Unit tests | (+) | Comparable to TestNG, but lacks support for groups. Backwards compatible with JUnit3. \\ |
| [XmlUnit | http://xmlunit.sourceforge.net/] | none needed\\ | Unit test XML | (+)(+) | Use the utility classes |
| [Springs TestContext Framework | http://static.springframework.org/spring/docs/2.1.x/reference/testing.html#testcontext-framework] | none needed |  | (+) | Extends JUnit and TestNG. Injection of fixtures. Test grouping. Transaction control plus other utils. \\ |
| [JUnit4 Extensions | http://junitext.sourceforge.net/] | unknown | unknown |  |  |
|  | [shitty-maven-plugin | http://mojo.codehaus.org/shitty-maven-plugin/] | Integration tests |  | The plugin provides a simple way to run integration tests for a project (single module or multi-module). |

#### RDBMS testing 

| Tool | M2-plugin | Rating | Comment |
| --- | --- | --- | --- |
| [DBUnit | http://www.dbunit.org/] | [maven-dbunit-plugin | http://maven-plugins.sourceforge.net/maven-dbunit-plugin/] | (+) |  |
| [unitils | http://www.unitils.org] |  |  |  |
|  | [sql-maven-plugin | http://mojo.codehaus.org/sql-maven-plugin/] |  |  |
|  | [hibernate3-maven-plugin | http://mojo.codehaus.org/maven-hibernate3/hibernate3-maven-plugin/] |  |  |
|  | [maven-hsql-plugin | http://www.javagen.com/maven-hsql-plugin] |  |  |

[Derby](http://db.apache.org/derby/papers/DerbyTut/embedded_intro.html) embedded database
[hsqldb](http://hsqldb.org/) 

#### Mock Frameworks 

| Tool | M2-plugin | Type | Rating | Comment |
| --- | --- | --- | --- | --- |
| [Mockito | http://mockito.org/] | none needed | Mock framework | (+) | Relatively new framework, improvement of EasyMock |
| [EasyMock | http://www.easymock.org/] | none needed | Mock framework | (+) |  |
| [jMock | http://www.jmock.org/] | none needed | Mock framework | (-) |  |
