# Setup for Selenium on CI using Maven, Jetty and JUnit

**Diagram: CiSeleniumSetup**

Note!The setup is version dependent! (not for JUnit) 

Junit:
```
<dependencies>
...
 <!-- Junit -->
 <dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.5</version>
    <scope>test</scope>
 </dependency>

  <!-- Selenium -->
  <dependency>
     <groupId>org.openqa.selenium.client-drivers</groupId>
     <artifactId>selenium-java-client-driver</artifactId>
     <version>1.0-beta-1</version>
     <scope>test</scope>
  </dependency>
...
</dependencies>
```

Plugins:

```

    <build>
        <plugins>

<plugin>
        <groupId>org.mortbay.jetty</groupId>
        <artifactId>maven-jetty-plugin</artifactId>
        <version>6.1.10</version>
        <configuration>
 
                <scanIntervalSeconds>10</scanIntervalSeconds>
                <stopKey>foo</stopKey>
                <stopPort>9999</stopPort>
        </configuration>
        <executions>
                <execution>
                        <id>start-jetty</id>
                        <phase>pre-integration-test</phase>
                        <goals>
                                <goal>run</goal>
                        </goals>
                        <configuration>
                                <scanIntervalSeconds>0</scanIntervalSeconds>
                                <daemon>true</daemon>
                        </configuration>
                </execution>
                <execution>
                        <id>stop-jetty</id>
                        <phase>post-integration-test</phase>
                        <goals>
                                <goal>stop</goal>
                        </goals>
                </execution>
        </executions>
</plugin>

            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>selenium-maven-plugin</artifactId>
                <version>1.0-rc-1</version>
                <executions>
                    <execution>
                        <phase>pre-integration-test</phase>
                        <goals>
                            <goal>start-server</goal>
                        </goals>
                        <configuration>
                            <background>true</background>
                        </configuration>
                    </execution>
                </executions>
            </plugin>

            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>2.4.2</version>
                <configuration>
                    <!-- Skip the normal tests, we'll run them in the integration-test phase -->
                    <skip>true</skip>
                </configuration>

                <executions>
                    <execution>
                        <phase>integration-test</phase>
                        <goals>
                            <goal>test</goal>
                        </goals>
                        <configuration>
                            <skip>false</skip>
                        </configuration>
                    </execution>
                </executions>
            </plugin>

        </plugins>
    </build>

```

Selenium tests can be recorded, exported to Java code and used without any major changes.

The test below has been sligtly changed.
```

package tutorial;

import org.junit.Test;

import com.thoughtworks.selenium.SeleneseTestCase;
import org.junit.Before;
import org.junit.Ignore;

public class IndexActionTest extends SeleneseTestCase {

    @Before
	public void setUp() throws Exception {
		setUp("http://localhost:8080/", "*chrome");
	}

    @Test
	public void testNew() throws Exception {
        selenium.open("/coolapp/index.action");
        selenium.waitForPageToLoad("1500000");
        selenium.isTextPresent("Welcome, World!");
	}

}
```
