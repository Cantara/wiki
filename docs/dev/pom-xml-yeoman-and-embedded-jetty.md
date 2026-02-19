# pom.xml yeoman and embedded jetty

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.company</groupId>
    <artifactId>admin-gui</artifactId>
    <version>0.3-SNAPSHOT</version>
    <description>Admin GUI</description>

    <parent>
        <groupId>com.company.emi</groupId>
        <artifactId>parent</artifactId>
        <version>5</version>
    </parent>

    <scm>
        <developerConnection>scm:git:ssh://server/data/git/admin-gui.git</developerConnection>
    </scm>

    <repositories>
        <!-- Needed for parent pom-->
        <repository>
            <id>company-releases</id>
            <name>Company Release Repository</name>
            <url>http://ciserver:8081/nexus/content/repositories/releases/</url>
        </repository>
    </repositories>

    <properties>
        <service.name>Admin GUI</service.name>
        <slf4j.version>1.7.7</slf4j.version>
        <jetty.version>9.2.1.v20140609</jetty.version>
    </properties>

    <build>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <filtering>false</filtering>
            </resource>
            <!-- Add static content to embed it in the jar file. -->
            <resource>
                <directory>yo/dist</directory>
            </resource>
        </resources>

        <plugins>
            <plugin>
                <artifactId>maven-clean-plugin</artifactId>
                <configuration>
                    <filesets>
                        <fileset>
                            <directory>yo/dist</directory>
                        </fileset>
                        <fileset>
                            <directory>yo/.tmp</directory>
                        </fileset>
                        <fileset>
                            <directory>yo/app/bower_components</directory>
                        </fileset>
                        <fileset>
                            <directory>yo/node_modules</directory>
                        </fileset>
                    </filesets>
                </configuration>
            </plugin>

            <!-- https://github.com/trecloux/yeoman-maven-plugin -->
            <plugin>
                <groupId>com.github.trecloux</groupId>
                <artifactId>yeoman-maven-plugin</artifactId>
                <version>0.2</version>
                <executions>
                    <execution>
                        <phase>generate-resources</phase>
                        <goals>
                            <goal>build</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>

            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>appassembler-maven-plugin</artifactId>
                <version>1.3</version>
                <configuration>
                    <repositoryLayout>flat</repositoryLayout>
                    <includeConfigurationDirectoryInClasspath>false</includeConfigurationDirectoryInClasspath>
                    <target>${project.build.directory}</target>
                    <daemons>
                        <daemon>
                            <id>${project.name}</id>
                            <mainClass>com.company.Main</mainClass>
                            <platforms>
                                <platform>jsw</platform>
                            </platforms>
                            <generatorConfigurations>
                                <generatorConfiguration>
                                    <generator>jsw</generator>
                                    <includes>
                                        <!--<include>windows-x86-32</include>-->
                                        <include>windows-x86-64</include>
                                    </includes>
                                    <configuration>
                                        <property>
                                            <name>configuration.directory.in.classpath.first</name>
                                            <value>config_override</value>
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
                                            <name>wrapper.console.title</name>
                                            <value>${service.name}</value>
                                        </property>
                                        <property>
                                            <name>wrapper.ntservice.name</name>
                                            <value>${service.name}</value>
                                        </property>
                                        <property>
                                            <name>wrapper.ntservice.displayname</name>
                                            <value>${service.name}</value>
                                        </property>
                                    </configuration>
                                </generatorConfiguration>
                            </generatorConfigurations>
                            <jvmSettings>
                                <initialMemorySize>32M</initialMemorySize>
                                <maxMemorySize>256M</maxMemorySize>
                                <extraArguments>
                                    <extraArgument>-XX:PermSize=32m</extraArgument>
                                    <extraArgument>-XX:MaxPermSize=32m</extraArgument>
                                    <extraArgument>-Dlogback.configurationFile=file:config_override/logback.xml</extraArgument>
                                </extraArguments>
                            </jvmSettings>
                        </daemon>
                    </daemons>
                </configuration>
                <executions>
                    <execution>
                        <id>generate-jsw-scripts</id>
                        <phase>package</phase>
                        <goals>
                            <goal>generate-daemons</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <artifactId>maven-assembly-plugin</artifactId>
                <configuration>
                    <descriptors>
                        <descriptor>src/main/assembly/assembly.xml</descriptor>
                    </descriptors>
                    <appendAssemblyId>false</appendAssemblyId>
                </configuration>
                <executions>
                    <execution>
                        <id>assemble-zip</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>

        </plugins>
    </build>

    <dependencies>
        <dependency>
            <groupId>org.eclipse.jetty</groupId>
            <artifactId>jetty-server</artifactId>
            <version>${jetty.version}</version>
        </dependency>

        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>${slf4j.version}</version>
        </dependency>
        <dependency>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
            <version>1.1.2</version>
            <scope>runtime</scope>
        </dependency>
        <!-- Used by logback SmtpAppender -->
        <dependency>
            <groupId>javax.activation</groupId>
            <artifactId>activation</artifactId>
            <version>1.1.1</version>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>javax.mail</groupId>
            <artifactId>mail</artifactId>
            <version>1.4.1</version>
            <scope>runtime</scope>
        </dependency>
    </dependencies>
</project>

```
