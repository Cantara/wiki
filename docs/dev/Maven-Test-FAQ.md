# Maven Test FAQ

## Table of Contents

---
#### Which versions of Surefire and TestNG work well together? 

We recommend Surefire 2.4 and TestNG 5.7 or 5.8. This combination has proven to work well. 

```
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>2.4</version>
      <configuration>
        <suiteXmlFiles>
          <suiteXmlFile>src/test/resources/testng.xml</suiteXmlFile>
        </suiteXmlFiles>
      </configuration>
    </plugin>
  </plugins>
</build>
<dependencies>
  <dependency>
    <groupId>org.testng</groupId>
    <artifactId>testng</artifactId>
    <version>5.7</version>
    <scope>test</scope>
    <classifier>jdk15</classifier>
  </dependency>
</dependencies>  
```

#### How to handle different groups of tests separately with TestNG?

TestNG use a configuration file, which can be changed run-time, to decide which tests to run. As of time of writing, this is the best known approach to handle multiple groups of tests. 

- Use annotations to sort your tests into groups. 
- Write one configuration for each environment you want to support (e.g. all unit tests and unit tests + integration tests) 
- Use profiles to select which configuration to run

Example setup follows. 

##### pom.xml 

Add dependency to testng and a configuration to surefire: [recommended combination of surefire and testng](http://wiki.objectware.no/display/java/Maven+FAQ#MavenFAQ-WhichversionsofSurefireandTestNGworkwelltogether%3F)

##### A test method 

```
@Test(groups = { "database"})
public void testSomeThingThatUseADatabase() {
  //some assertions

}
```

##### testng.xml
```
<!DOCTYPE suite SYSTEM "http://beust.com/testng/testng-1.0.dtd">
<suite name="ArtifactName Non-environment dependent test suite">

  <test name="Non-environment dependent tests" verbose="3">
    <groups>
      <run>
        <exclude name="database" />
        <exclude name="jms" />
      </run>
    </groups>

    <packages>
      <package name="no.company.projectName.packageA.*" />
    </packages>
  </test>
</suite>
```

##### testng-jms-database.xml
```
<!DOCTYPE suite SYSTEM "http://beust.com/testng/testng-1.0.dtd">
<suite name="ArtifactName test suite">

  <test name="All tests" verbose="10">
    <packages>
      <package name="no.company.projectName.packageA.*" />
    </packages>
  </test>
</suite>
```

**NOTE!** 
The general group concept is scalable, but many profiles quickly become chaotic. It is thus recommended to use a Continuous Integration server to handle all but two-three profiles. 

#### How to handle different groups of tests separately _without_ TestNG?

Without TestNG there are two approaches to run tests that are not run when executing _mvn test_. Note that this approach can only handle _two_ dimensions. This is why the most common separation is unit tests and integration tests. 

- Put all integration tests in a separate folder (e.g. itest).
    - See \[example \](../[http/svn-objectware-no-repos-objectware-public-examples-maven-itest-examples-itest-directory.md)

- Use a naming convention so separate from regular/unit tests (e.g. all integration tests a postfixed with IntTest
    - See \[example \](../[http/svn-objectware-no-repos-objectware-public-examples-maven-itest-examples-itest-directory.md)

#### How to only run some groups with a maven profile?

##### pom.xml
```
...
  <profiles>
    <profile>
      <id>integration</id>
        <activation>
          <property>
            <name>env</name>
            <value>integration</value>
          </property>
        </activation>
        <build>
          <plugins>
            <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-surefire-plugin</artifactId>
              <version>2.4.2</version>
              <configuration>
                <suiteXmlFiles>
                  <suiteXmlFile>src/test/resources/testngIntegration.xml</suiteXmlFile>
                </suiteXmlFiles>
              </configuration>
            </plugin>
          </plugins>
        </build>
      </profile>
    </profiles>
...
```

##### testngIntegration.xml
```
<!DOCTYPE suite SYSTEM "http://beust.com/testng/testng-1.0.dtd">
<suite name="Name Me">
  <test name="Name Me Suite" verbose="2">
    <groups>
      <run>
      </run>
    </groups>

    <packages>
      <package name="no.objectware.rename.package.*" />
    </packages>
  </test>
</suite>
```

##### testng.xml
```
<!DOCTYPE suite SYSTEM "http://beust.com/testng/testng-1.0.dtd">
<suite name="Name Me">
  <test name="Name Me Suite" verbose="2">
    <groups>
      <run>
        <exclude name="integration" />
      </run>
    </groups>

    <packages>
      <package name="no.objectware.rename.package.*" />
    </packages>
  </test>
</suite>
```

mvn clean install runs all tests, except those who are marked with @Test(groups = {"integration"})
mvn clean install -P integration runs all tests.

#### How to verify that JSPs compile?

To precompile JSPs the [jspc-maven-plugin](http://mojo.codehaus.org/jspc-maven-plugin/) can be used.

Example:
```lang
<build>
  <plugins>
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>jspc-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>jspc</id>
          <goals>
            <goal>compile</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

#### How can we continue building through the reactor when the first modules have test failures?

Configure surefire with {}. Or on the command line:

```
mvn install -Dmaven.test.failure.ignore=true
```

Generally, this is not recommended. But it can be handy if you have a reactor of integration tests, and you want to run through them all. Several CI servers (Bamboo and Hudson, don't know about Continuum) recognize these builds as failed even though maven says that the build is successful with test failures.

#### How do I run a single test?

From http://maven.apache.org/plugins/maven-surefire-plugin/examples/single-test.html :

{}

#### How can we output the test results from surefire directly to console?

If you don't want to burrow into {} for seeing the result report, you can tell surefire to not use files and output will be written to console:

{}

#### How to redirect the testng reporting to target? 

Use the _reportsDirectory_ tag. 

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>${surefireVersion}</version>
  <configuration>
    <reportsDirectory>${basedir}/target/testng</reportsDirectory>
    <suiteXmlFiles>
      <suiteXmlFile>src/test/resources/testng.xml</suiteXmlFile>
    </suiteXmlFiles>
  </configuration>
</plugin>
```
