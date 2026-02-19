# Maven Webstart - static website

## Contents

## Example template.vm

In _src/main/jnlp/template.vm_: 
```
<?xml version="1.0" encoding="utf-8"?>
<jnlp
    spec="1.0+"
    codebase="http://objectware.no/webstart/$project.ArtifactId/"
    href="$outputFile">

    <information>
        <title>$project.Name $project.Version</title>
        <vendor>$project.Organization.Name</vendor>
        <homepage>$project.Organization.Url</homepage>
        <description kind="one-line">$project.Description</description>
        <offline-allowed>true</offline-allowed>
    </information>

    <security>
        <all-permissions/>
    </security>
    
    <resources>
        <j2se version="1.5+" initial-heap-size="256m" max-heap-size="384m"/>
        $dependencies
    </resources>
    <application-desc main-class="$mainClass"/>
</jnlp>
```

## Certificate management

Generate certificate:
`keytool -genkey -keyalg rsa -alias myAlias -validity 3650`

View certificate 

` keytool -v -list -alias myAlias -keystore ~/.keystore `

Move the generated keystore into the project: 
` mv ~/.keystore src/main/jnlp/projectName_2007.12.02.keystore`

For more on this see [Java SSL - Keystores](Java-SSL-Keystores.md)

## Differences between single-module and multi-module 

- Multimodule should use the inline goal: 
` <goal>jnlp-inline</goal> ` 

- In a multimodule project the webstart setup should be placed in a separate module. 

- The webstart module must have a dependency to the module where the main class is located. 

- Run webstart from the module's root, not the parent: 
`mvn org.codehaus.mojo.webstart:webstart-maven-plugin:jnlp-inline`

## Single module, self-signed certificate 

_pom.xml_: 
```
<properties>
    <packageName>no.objectware.package</packageName>
    <mainClass>${packageName}.NameOfMainClass</mainClass>
    <webstart-dir>/data/webstart/${artifactId}</webstart-dir>
    <keystore.file>${basedir}/src/main/jnlp/testKeystore.keystore</keystore.file>
  </properties>
  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo.webstart</groupId>
        <artifactId>webstart-maven-plugin</artifactId>
        <version>1.0-alpha-2-SNAPSHOT</version>
        <executions>
          <execution>
            <phase>deploy</phase>
            <goals>
              <goal>jnlp</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <libPath>lib</libPath>
          <jnlp>
            <outputFile>${name}.jnlp</outputFile>
            <mainClass>${mainClass}</mainClass>
          </jnlp>
          <sign>
            <keystore>${keystore.file}</keystore>
            <storepass>m2m2m2</storepass>
            <alias>myAlias</alias>
            <validity>3650</validity>  
            <verify>true</verify>
            <keystoreConfig>
              <delete>false</delete>
              <gen>false</gen>
            </keystoreConfig>
          </sign>
          <outputJarVersions>false</outputJarVersions>
          <pack200>false</pack200>
          <gzip>false</gzip>
          <verbose>false</verbose>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-antrun-plugin</artifactId>
        <executions>
          <execution>
            <phase>deploy</phase>
            <goals>
              <goal>run</goal>
            </goals>
            <configuration>
              <tasks>
                <copy todir="${webstart-dir}" overwrite="true" verbose="false" failonerror="true">
                  <fileset dir="target/jnlp" includes="**/*.*" />
                </copy>
              </tasks>
            </configuration>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
```

## Single module, new certificate for every clean

_pom.xml_:
```
  <properties>
    <packageName>no.objectware.package</packageName>
    <mainClass>${packageName}.NameOfMainClass</mainClass>
    <webstart-dir>/data/webstart/${pom.artifactId}</webstart-dir>
  </properties>
  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo.webstart</groupId>
        <artifactId>webstart-maven-plugin</artifactId>
        <version>1.0-alpha-2-SNAPSHOT</version>
        <executions>
          <execution>
            <phase>deploy</phase>
            <goals>
              <goal>jnlp</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <libPath>lib</libPath>
          <jnlp>
            <outputFile>${pom.name}.jnlp</outputFile>
            <mainClass>${mainClass}</mainClass>
          </jnlp>
          <sign>
            <keystore>${project.build.directory}/keystore</keystore>
            <keypass>m2m2m2</keypass>
            <storepass>m2m2m2</storepass>
            <alias>projectNameHere certificate</alias>
            <validity>365</validity>            
            <dnameCn>objectware.no</dnameCn>
            <dnameOu>None</dnameOu>
            <dnameO>projectName</dnameO>
            <dnameL>Oslo</dnameL>
            <dnameSt>Oslo</dnameSt>
            <dnameC>NO</dnameC>
            <verify>true</verify>
            <keystoreConfig>
              <delete>true</delete>
              <gen>true</gen>
            </keystoreConfig>
          </sign>
          <outputJarVersions>false</outputJarVersions>
          <verbose>false</verbose>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-antrun-plugin</artifactId>
        <executions>
          <execution>
            <phase>deploy</phase>
            <goals>
              <goal>run</goal>
            </goals>
            <configuration>
              <tasks>
                <copy todir="${webstart-dir}" overwrite="true" verbose="false" failonerror="true">
                  <fileset dir="target/jnlp" includes="**/*.*"/>
                </copy>
                <copy todir="${webstart-dir}" overwrite="true" verbose="true" failonerror="true">
                  <fileset dir="target" includes="**/*-jar-with-dependencies.jar"/>
                </copy>
              </tasks>
            </configuration>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
```

## Resources 

[webstart-maven-plugin](http://mojo.codehaus.org/webstart/webstart-maven-plugin/)
 
[http://java.sun.com/j2se/1.5.0/docs/tooldocs/windows/keytool.html](http://java.sun.com/j2se/1.5.0/docs/tooldocs/windows/keytool.html)
[http://www.duckcreeksoftware.com/products/jnlp-wrapper/doc/create-certificate.jsp](http://www.duckcreeksoftware.com/products/jnlp-wrapper/doc/create-certificate.jsp)
