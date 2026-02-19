# JMeter pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.company.app1</groupId>
  <artifactId>systemtest-app1-performance</artifactId>
  <packaging>pom</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>Systemtest: App1 Performance</name>

  <developers>
    <developer>
      <id>Erik</id>
      <name>Erik Drolshammer</name>
      <organization>Objectware AS</organization>
    </developer>
  </developers>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-dependency-plugin</artifactId>
        <version>2.0</version>
        <executions>
          <execution>
            <id>build-classpath</id>
            <phase>generate-resources</phase>
            <goals>
              <goal>build-classpath</goal>
            </goals>
            <configuration>
              <cpFile>${project.build.directory}/classpath</cpFile>
              <includeScope>test</includeScope>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.apache.jmeter</groupId>
        <artifactId>maven-jmeter-plugin</artifactId>
        <version>1.0-SNAPSHOT</version>
        <executions>
          <execution>
            <id>jmeter-tests</id>
            <phase>test</phase>            
            <configuration>
              <reportDir>${project.build.directory}/jmeter-reports</reportDir>
              <classpathDump>${project.build.directory}/classpath</classpathDump>
              <!--
              <jmeterUserProperties>
              </jmeterUserProperties>
              -->
            </configuration>
            <goals>
              <goal>jmeter</goal>
            </goals>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>xml-maven-plugin</artifactId>
        <version>1.0-beta-2</version>
        <executions>
          <execution>
            <phase>pre-site</phase>
            <goals>
              <goal>transform</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <transformationSets>
            <transformationSet>
              <dir>${project.build.directory}/jmeter-reports</dir>
              <stylesheet>src/test/resources/jmeter-results-detail-report_21.xsl</stylesheet>
              <outputDir>${project.build.directory}/site/jmeter-results</outputDir>
              <fileMappers>
                <fileMapper
                    implementation="org.codehaus.plexus.components.io.filemappers.FileExtensionMapper">
                  <targetExtension>html</targetExtension>
                </fileMapper>
              </fileMappers>
            </transformationSet>
          </transformationSets>
        </configuration>
      </plugin>

      <!-- make sure the jmeter icons are copied to the site folder -->
      <!--
      <plugin>
        <artifactId>maven-antrun-plugin</artifactId>
        <executions>
          <execution>
            <phase>site</phase>
            <configuration>
              <tasks>
                <copy file="src/test/resources/expand.jpg" toFile="target/site/jmeter-results/expand.jpg" />
                <copy file="src/test/resources/collapse.jpg" toFile="target/site/jmeter-results/collapse.jpg" />                
              </tasks>
            </configuration>
            <goals>
              <goal>run</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
      -->
    </plugins>
  </build>

  <dependencies>
    <dependency>
      <groupId>org.apache.jmeter</groupId>
      <artifactId>jmeter</artifactId>
      <version>2.3</version>
      <exclusions>
        <exclusion>
          <groupId>junit</groupId>
          <artifactId>junit</artifactId>
        </exclusion>
      </exclusions>
    </dependency>
    <dependency>
      <groupId>javax.activation</groupId>
      <artifactId>activation</artifactId>
      <version>1.1</version>
    </dependency>
    <dependency>
      <groupId>javax.mail</groupId>
      <artifactId>mail</artifactId>
      <version>1.4.1</version>
    </dependency>
    <dependency>
      <groupId>soap</groupId>
      <artifactId>soap</artifactId>
      <version>2.3.1</version>
    </dependency>
  </dependencies>

  <reporting>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-project-info-reports-plugin</artifactId>
        <version>2.1.1</version>
        <reportSets>
          <reportSet>
            <reports>
              <report>index</report>
              <report>cim</report>
              <report>dependencies</report>
              <report>dependencies-convergence</report>
              <report>dependency-management</report>
              <!--<report>issue-tracking</report>-->
              <report>license</report>
              <!--<report>mailing-list</report>-->
              <report>plugins</report>
              <report>project-team</report>
              <report>scm</report>
              <report>summary</report>              
            </reports>
          </reportSet>
        </reportSets>
      </plugin>
    </plugins>
  </reporting>
</project>

```
