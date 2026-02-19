# How to use a zip file to share resources between projects

The producer creates an zip file containing some sql files. These are attached to the build and thus deployed alongside the primary artifact using a _classifier_. 

The consumer unpacks the zip and can utilize the sql files as if they were included in the consumer project. 

#### Producer 

In pom.xml 
```
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-assembly-plugin</artifactId>
  <version>2.2-beta-1</version>
  <configuration>
    <descriptors>
      <descriptor>src/main/assembly/sqlAsZip.xml</descriptor>
    </descriptors>
  </configuration>
  <executions>
    <execution>
      <id>assembleSqlAsZip</id>
      <phase>package</phase>
      <goals>
        <goal>single</goal>
      </goals>
    </execution>
  </executions>
</plugin>
```

In src/main/assembly/sqlAsZip.xml: 
```
<assembly>
  <id>sqlscripts</id>
  <formats>
    <format>zip</format>
  </formats>
  <!--<includeBaseDirectory>false</includeBaseDirectory>-->
  <fileSets>
    <fileSet>
      <directory>src/main/sql</directory>
      <filtered>true</filtered>
      <outputDirectory>/</outputDirectory>
    </fileSet>
    <fileSet>
      <directory>target/hibernate3/sql</directory>
      <filtered>true</filtered>
      <outputDirectory>/</outputDirectory>
    </fileSet>
  </fileSets>
</assembly>
```

#### Consumer 

In pom.xml: 
```
<plugin>
  <artifactId>maven-dependency-plugin</artifactId>
  <configuration>
    <artifactItems>
      <artifactItem>
        <groupId>com.company</groupId>
        <artifactId>artifact1</artifactId>
        <version>2.0-alpha-3-SNAPSHOT</version>
        <type>zip</type>
        <classifier>sqlscripts</classifier>
        <overWrite>true</overWrite>
        <outputDirectory>${generatedResourcesDir}</outputDirectory>              
      </artifactItem>
    </artifactItems>
  </configuration>
  <executions>
    <execution>
      <id>unpack-sqlscripts</id>
      <goals>
        <goal>unpack</goal>
      </goals>
      <phase>generate-resources</phase>
    </execution>
  </executions>
</plugin>
```
