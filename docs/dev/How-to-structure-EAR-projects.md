# How to structure EAR projects?

> ℹ️ Needs verification /extension

The goal is to have an EAR deployment unit. While we could have EJBS, servlets and other code and resources as modules, we recommend putting the "modules" as separate Maven projects to allow easier reuse. E.g. the core functionality may perhaps be reused elsewhere. 

#### EAR Project 
```
<project>
<packaging>ear</packaging>
  <dependencies>
    <dependency>
      <groupId>com.company.app1</groupId>
      <artifactId>app1-core</artifactId>
      <version>1.0-alpha-1-SNAPSHOT</version>
    </dependency>
    <dependency>
      <groupId>com.company.app1</groupId>
      <artifactId>app1-servlets</artifactId>
      <version>1.0-SNAPSHOT</version>
      <type>war</type>      
    </dependency>
    <dependency>
      <groupId>com.company.app1</groupId>
      <artifactId>app1-ejbs</artifactId>
      <version>1.0-SNAPSHOT</version>
      <type>ejb</type>      
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <artifactId>maven-ear-plugin</artifactId>
        <version>2.3.1</version>
        <configuration>
          <archive>
            <manifest>
              <addClasspath>true</addClasspath>
            </manifest>
          </archive>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

#### "Modules" 

###### Core project 

Standard jar project with regular java code. 

```
<project>
  <packaging>jar</packaging>
</project>
```

Standard directory structure

###### EJB project 

```
<project>
  <packaging>ejb</packaging>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-ejb-plugin</artifactId>
        <version>2.1</version>
        <configuration>
          <ejbVersion>3.0</ejbVersion>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

Standard directory structure

###### Servlets project 

```
<project>
  <packaging>war</packaging>
</project>
```

webapp directory structure: 
```
src/main/webapp/index.jsp
src/main/webapp/WEB-INF/web.xml
```
