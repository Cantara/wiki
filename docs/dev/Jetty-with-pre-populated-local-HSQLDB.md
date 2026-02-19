# Jetty with pre-populated local HSQLDB

# ERIKS KLADD. Dette virker ikke enda. 

Som hjelp til manuell test/verifikasjon av en webapp så hadde det vært veldig kjekt å dytte litt data til en hsqldb-instans før man starter jetty. 

Jeg øsnker altså å gjøre noe sånt som: 

1. Starte hsqldb 
2. Populere db med data 
3. mvn jetty:run
4. Stoppe jetty og database

1. Ser det ut som kan gjøres med [maven-hsql-plugin](http://www.javagen.com/maven-hsql-plugin)
(konsolloutput tydet i hvert fall på det)

2. Noen som har noen erfaringer med å populere en hsqldb fra maven? 
Er [dbunit-maven-plugin](http://mojo.codehaus.org/dbunit-maven-plugin) måten å gjøre dette på? 

Se forøvrig [How to initialize test database](http://galaxy.andromda.org/forum/viewtopic.php?t=5540&view=previous&sid=171631f6f42fdf1fa83c9d1197ab69b6)

```
<plugin>
        <groupId>org.javagen.revgen</groupId>
        <artifactId>maven-hsql-plugin</artifactId>
        <version>1.0-beta2</version>
        <configuration>
          <database>target/hsqldb/</database>
          <dbname>jettyDB</dbname>
          
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>dbunit-maven-plugin</artifactId>
        <version>1.0-beta-1</version>

        <dependencies>
          <dependency>
            <groupId>hsqldb</groupId>
            <artifactId>hsqldb</artifactId>
            <version>1.8.0.7</version>
          </dependency>
        </dependencies>

        <configuration>
          <driver>org.hsqldb.jdbcDriver</driver>
          <url>jdbc:hsqldb:file:target/hsqldb/jettyDB</url>
          <username>sa</username>
          <password></password>
        </configuration>

        <executions>
          <execution>
            <goals>
              <goal>operation</goal>
            </goals>
            <configuration>
              <format>xml</format>
              <type>CLEAN_INSERT</type>
              <src>dataset.xml</src>
            </configuration>
          </execution>
        </executions>
      </plugin>
      

      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>hibernate3-maven-plugin</artifactId>
        <version>2.0-alpha-1</version>
        <configuration>
          <components>
            <component>
              <name>hbm2ddl</name>
              <implementation>annotationconfiguration</implementation>
            </component>
            <component>
              <name>hbm2hbmxml</name>
              <outputDirectory>src/main/resources</outputDirectory>
            </component>
          </components>
          <componentProperties>
            <outputfilename>schema-export.sql</outputfilename>
            <!-- <propertyfile>/src/main/resources/hibernate.properties</propertyfile> -->
            <export>false</export>
            <drop>true</drop>
            <scan-classes>true</scan-classes>
          </componentProperties>
        </configuration>
        <!--
            <executions>
              <execution>
                <phase>process-classes</phase>
                <goals>
                  <goal>hbm2ddl</goal>
                </goals>
              </execution>
            </executions>
             -->
      </plugin>

```
