# Maven FUQ

## Maven Frequently Unanswered Questions

#### How do I use maven<sub>~jaxb</sub><sub>schemagen</sub><sub>plugin (generate xsd from java) and jaxws</sub>~maven-plugin (generate java classes from WSDL) on java 6 on the same prosject?
Current content of pom that does **not** work:
```
<plugin>
        <groupId>com.sun.tools.jxc.maven2</groupId>
        <artifactId>maven-jaxb-schemagen-plugin</artifactId>
        <executions>
        <execution>
        <phase>process-sources</phase>
        <configuration>
        <destdir>${project.build.directory}/generated-schema</destdir>
        <includes>
        <include>no/tele/lifestyle/core/userservice/User.java</include>
        </includes>
        <schemas>
        <schema>
        <namespace>http://life.tele.no/</namespace>
        <file>LifeStyleTool.xsd</file>
        </schema>
        </schemas>
        <srcdir>${project.build.sourceDirectory}</srcdir>
        <verbose>true</verbose>
        </configuration>
        <goals>
        <goal>generate</goal>
        </goals>
        </execution>
        </executions>
        </plugin> -->
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>jaxws-maven-plugin</artifactId>
        <executions>
          <execution>
            <goals>
              <goal>wsimport</goal>
            </goals>
            <configuration>
              <wsdlUrls>
                <wsdlUrl>http://px.pats.no/px/services/TerminalLocation?wsdl</wsdlUrl>
              </wsdlUrls>
              <packageName>no.tele.life.pats</packageName>
            </configuration>
          </execution>
        </executions>
      </plugin>
```
