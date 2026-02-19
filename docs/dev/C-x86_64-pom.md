# C++ x86_64 pom

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.company.app1</groupId>
  <artifactId>app1-x86_64</artifactId>
  <packaging>a</packaging>
  <name>App1 binary for x86_64</name>
  <description>Create a binary a package for App1 </description>

  <parent>
    <groupId>com.company.app1</groupId>
    <artifactId>app1</artifactId>
    <version>3.7.4-SNAPSHOT</version>
  </parent>

  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>native-maven-plugin</artifactId>
        <configuration>
          <compilerStartOptions>
            <compilerStartOption>-m64 ${commonCompilerOptions}</compilerStartOption>
          </compilerStartOptions>
          <linkerStartOptions>
            <linkerStartOption>-m64 ${commonLinkerOptions}</linkerStartOption>
          </linkerStartOptions>                     
        </configuration>
      </plugin>
    </plugins>
  </build>

  <distributionManagement>
    <site>
      <id>site</id>
      <url>file:///var/www/html/sites/${parent.artifactId}/${parent.version}/${pom.artifactId}</url>
    </site>
  </distributionManagement>
</project>
```
