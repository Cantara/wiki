# C++ parent pom

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.company.app1</groupId>
  <artifactId>app1</artifactId>
  <version>3.7.5-SNAPSHOT</version>
  <packaging>pom</packaging>
  <name>App1</name>
  <description>Build binary and rpm for App1.</description>

  <parent>
    <groupId>com.company</groupId>
    <artifactId>company-parent</artifactId>
    <version>30</version>
  </parent>

  <scm>
    <connection>
      scm:svn:svn+ssh://svn.company.com/var/local/repos/app1/app1/trunk
    </connection>
    <developerConnection>
      scm:svn:svn+ssh://svn.company.com/var/local/repos/app1/app1/trunk
    </developerConnection>
  </scm>

  <profiles>
    <profile>
      <id>add-linux-x86-module</id>
      <activation>
        <os>
          <family>Linux</family>
          <arch>i386</arch>
        </os>
      </activation>
      <modules>
        <module>app1-i686</module>
      </modules>
    </profile>
    <profile>
      <id>add-linux-x86_64-module</id>
      <activation>
        <os>
          <family>Linux</family>
          <arch>amd64</arch>
        </os>
      </activation>
      <modules>
        <module>app1-i686</module>
        <module>app1-x86_64</module>
      </modules>
    </profile>
  </profiles>

  <modules>
    <module>app1-rpm</module>
  </modules>

  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>${project.groupId}</groupId>
        <artifactId>app1-i686</artifactId>
        <version>${pom.version}</version>
        <type>a</type>
      </dependency>
      <dependency>
        <groupId>${project.groupId}</groupId>
        <artifactId>app1-x86_64</artifactId>
        <version>${pom.version}</version>
        <type>a</type>
      </dependency>
      <dependency>
        <groupId>${project.groupId}</groupId>
        <artifactId>app1-rpm</artifactId>
        <version>${pom.version}</version>
      </dependency>
    </dependencies>
  </dependencyManagement>

  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.codehaus.mojo</groupId>
          <artifactId>native-maven-plugin</artifactId>
          <version>1.0-alpha-2</version>
          <extensions>true</extensions>
          <configuration>
            <compilerProvider>generic</compilerProvider>
            <compilerExecutable>g++</compilerExecutable>
            <linkerExecutable>g++</linkerExecutable>
            <compilerStartOptions>
              <compilerStartOption>${commonCompilerOptions}</compilerStartOption>
            </compilerStartOptions>

            <linkerStartOptions>
              <linkerStartOption>${commonLinkerOptions}</linkerStartOption>
            </linkerStartOptions>
            <!-- Necessary to define all folders explicitly. See http://jira.codehaus.org/browse/MOJO-1321 -->
            <sources>
              <source>
                <directory>${native.source.dir}/dir1</directory>
                <includes>
                  <include>**/*.cpp</include>
                </includes>
              </source>
              <source>
                <directory>${native.source.dir}/dir1/subdir1</directory>
                <includes>
                  <include>**/*.cpp</include>
                </includes>
              </source>
            </sources>
          </configuration>
        </plugin>
      </plugins>
    </pluginManagement>

    <plugins>
      <!-- Use the following to skip site-deploy -->
      <!--
      <plugin>
        <artifactId>maven-release-plugin</artifactId>
        <configuration>
          <useReleaseProfile>false</useReleaseProfile>
          <preparationGoals>clean install</preparationGoals>
          <goals>deploy</goals>
        </configuration>
      </plugin>
      -->
      <plugin>
        <groupId>com.google.code.maven-license-plugin</groupId>
        <artifactId>maven-license-plugin</artifactId>
        <configuration>
          <header>${generatedResourcesDir}/ccompany-header.txt</header>
          <failIfMissing>false</failIfMissing>  <!-- Different format on the headers in this project -->
          <includes>
            <include>src/**</include>
          </includes>
        </configuration>
        <executions>
          <execution>
            <goals>
              <goal>check</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>

  <distributionManagement>
    <site>
      <id>site</id>
      <url>${siteUrl}</url>
    </site>
  </distributionManagement>

  <properties>
    <native.source.dir>../src/main/native</native.source.dir>
    <commonCompilerOptions>
      -DHAVE_CONFIG=1 -Wall -pedantic -pthread -Wno-long-long -fno-strict-aliasing -O3 -ggdb
    </commonCompilerOptions>
    <commonLinkerOptions>-Ltarget -ggdb -lpthread</commonLinkerOptions>
  </properties>
</project>
```
