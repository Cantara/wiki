# JSW Daemon Parent POM Example

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.company</groupId>
  <artifactId>company-parent-jsw-daemon</artifactId>
  <version>12-SNAPSHOT</version>
  <packaging>pom</packaging>
  <name>Company JSW Daemon Parent</name>

  <parent>
    <groupId>com.company</groupId>
    <artifactId>company-parent</artifactId>
    <version>29</version>
  </parent>
  

  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.codehaus.mojo</groupId>
          <artifactId>appassembler-maven-plugin</artifactId>
          <version>1.0</version>
        </plugin>
        <plugin>
          <groupId>org.codehaus.mojo</groupId>
          <artifactId>unix-maven-plugin</artifactId>
          <version>1.0-alpha-3-SNAPSHOT</version>
        </plugin>
      </plugins>
    </pluginManagement>

    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>appassembler-maven-plugin</artifactId>
        <configuration>
          <repositoryLayout>flat</repositoryLayout>
          <includeConfigurationDirectoryInClasspath>true</includeConfigurationDirectoryInClasspath>
          <target>${appassemblerTarget}</target>
          <assembleDirectory>${appassemblerAssembleDirectory}</assembleDirectory>
          <repoPath>lib</repoPath>

          <defaultJvmSettings>
            <initialMemorySize>${initialMemorySize}</initialMemorySize>
            <maxMemorySize>${maxMemorySize}</maxMemorySize>

            <systemProperties>
              <systemProperty>user.timezone=UTC</systemProperty>
            </systemProperties>
          </defaultJvmSettings>

          <daemons>
            <daemon>
              <id>${rpm.appname}</id>
              <mainClass>${mainClass}</mainClass>
              <commandLineArguments>
                <commandLineArgument>start</commandLineArgument>
              </commandLineArguments>
              <platforms>
                <platform>jsw</platform>
              </platforms>
              <generatorConfigurations>
                <generatorConfiguration>
                  <generator>jsw</generator>
                  <includes>
                    <include>linux-x86-32</include>
                    <include>linux-x86-64</include>
                  </includes>
                  <configuration>
                    <property>
                      <name>configuration.directory.in.classpath.first</name>
                      <value>etc</value>
                    </property>
                    <property>
                      <name>set.default.REPO_DIR</name>
                      <value>lib</value>
                    </property>
                    <property>
                      <name>wrapper.logfile</name>
                      <value>logs/wrapper.log</value>
                    </property>
                    <property>
                      <name>run.as.user.envvar</name>
                      <value>${rpm.username}</value>
                    </property>
                  </configuration>
                </generatorConfiguration>
              </generatorConfigurations>
            </daemon>
          </daemons>
        </configuration>
        <executions>
          <execution>
            <phase>generate-resources</phase>
            <goals>
              <goal>create-repository</goal>
              <goal>generate-daemons</goal>
            </goals>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>unix-maven-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <assembly>
            <copy-directory>
              <from>src/main/unix/files</from>
              <to>${rpm.path}/</to>
            </copy-directory>

            <copy-directory>
              <from>${appassemblerAssembleDirectory}</from>
              <to>${rpm.path}</to>
              <excludes>
                <exclude>**/maven-metadata-appassembler.xml</exclude>
              </excludes>
            </copy-directory>

            <mkdirs>
              <paths>
                <path>${rpm.path}/run</path>
                <path>${rpm.path}/logs</path>
              </paths>
            </mkdirs>

            <set-attributes>
              <basedir>${rpm.path}/bin</basedir>
              <fileAttributes>
                <user>${rpm.username}</user>
                <group>${rpm.groupname}</group>
                <mode>6774</mode>
              </fileAttributes>
            </set-attributes>
            <set-attributes>
              <basedir>${rpm.path}/logs</basedir>
              <fileAttributes>
                <group>${rpm.log.groupname}</group>
              </fileAttributes>
            </set-attributes>

          </assembly>
          <contact>Erik Drolshammer</contact>
          <contactEmail>someEmail</contactEmail>
          <revision>${rpm.revision}</revision>
          <defaults>
            <fileAttributes>
              <user>${rpm.username}</user>
              <group>${rpm.groupname}</group>
              <mode>0664</mode>
            </fileAttributes>
            <directoryAttributes>
              <user>${rpm.username}</user>
              <group>${rpm.groupname}</group>
              <mode>0775</mode>
            </directoryAttributes>
          </defaults>
          <rpm>
            <softwareGroup>Applications/Engineering</softwareGroup>
          </rpm>
        </configuration>
      </plugin>
    </plugins>
  </build>

  <properties>
    <mainClassPackage>${pom.groupId}</mainClassPackage>
    <mainClass>${mainClassPackage}.SomeLauncher</mainClass>

    <rpm.appname>${pom.artifactId}</rpm.appname>
    <rpm.username>${rpm.appname}</rpm.username>
    <rpm.groupname>common-system-group</rpm.groupname>
    <rpm.log.groupname>${rpm.groupname}-log</rpm.log.groupname>
    <rpm.path>/usr/local/${rpm.appname}</rpm.path>
    <rpm.revision>1</rpm.revision>

    <appassemblerTarget>${project.build.directory}/appassembler</appassemblerTarget>
    <appassemblerAssembleDirectory>${appassemblerTarget}/jsw/${rpm.appname}</appassemblerAssembleDirectory>

    <initialMemorySize>128M</initialMemorySize>
    <maxMemorySize>1024M</maxMemorySize>
  </properties>

</project>
```
