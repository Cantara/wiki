# Code-centric test tools

#### Unit Test oriented test tools 

| Tool | M2-plugin | Type | Rating | Comment |
| --- | --- | --- | --- | --- |
| [TestNG | http://testng.org] | [maven<sub>~surefire</sub>~plugin | http://maven.apache.org/plugins/maven<sub>~surefire</sub>~plugin/] | General purpose | (+)(+) |  |
| [Junit4 | http://www.junit.org/] | [maven<sub>~surefire</sub>~plugin | http://maven.apache.org/plugins/maven<sub>~surefire</sub>~plugin/] | Unit tests | (+) | Comparable to TestNG, but lacks support for groups. Backwards compatible with JUnit3. \\ |
| [XmlUnit | http://xmlunit.sourceforge.net/] | none needed\\ | Unit test XML | (+)(+) | Use the utility classes |
| [Springs TestContext Framework | http://static.springframework.org/spring/docs/2.1.x/reference/testing.html#testcontext-framework] | none needed |  | (+) | Extends JUnit and TestNG. Injection of fixtures. Test grouping. Transaction control plus other utils. \\ |
| [JUnit4 Extensions | http://junitext.sourceforge.net/] | unknown | unknown |  |  |
|  | [shitty<sub>~maven</sub>~plugin | http://mojo.codehaus.org/shitty<sub>~maven</sub>~plugin/] | Integration tests |  | The plugin provides a simple way to run integration tests for a project (single module or multi-module). |

#### RDBMS testing 

| Tool | M2-plugin | Rating | Comment |
| --- | --- | --- | --- |
| [DBUnit | http://www.dbunit.org/] | [maven<sub>~dbunit</sub>~plugin | http://maven<sub>~plugins.sourceforge.net/maven</sub>~dbunit-plugin/] | (+) |  |
| [unitils | http://www.unitils.org] |  |  |  |
|  | [sql<sub>~maven</sub>~plugin | http://mojo.codehaus.org/sql<sub>~maven</sub>~plugin/] |  |  |
|  | [hibernate3<sub>~maven</sub>~plugin | http://mojo.codehaus.org/maven<sub>~hibernate3/hibernate3</sub>~maven-plugin/] |  |  |
|  | [maven<sub>~hsql</sub>~plugin | http://www.javagen.com/maven<sub>~hsql</sub>~plugin] |  |  |

[Derby](http://db.apache.org/derby/papers/DerbyTut/embedded_intro.html) embedded database
[hsqldb](http://hsqldb.org/) 

#### Mock Frameworks 

| Tool | M2-plugin | Type | Rating | Comment |
| --- | --- | --- | --- | --- |
| [Mockito | http://mockito.org/] | none needed | Mock framework | (+) | Relatively new framework, improvement of EasyMock |
| [EasyMock | http://www.easymock.org/] | none needed | Mock framework | (+) |  |
| [jMock | http://www.jmock.org/] | none needed | Mock framework | (-) |  |
