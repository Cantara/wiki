# Example RPM Parent

```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.company</groupId>
  <artifactId>company-parent-rpm</artifactId>
  <version>6</version>
  <packaging>pom</packaging>
  <name>company RPM Parent</name>

  <scm>
    <connection>scm:svn:svn+ssh://svn.company.local/var/local/repos/pl_common/lib/company-parent-rpm</connection>
    <developerConnection>scm:svn:svn+ssh://svn.company.local/var/local/repos/pl_common/lib/company-parent-rpm</developerConnection>
  </scm>

  <repositories>
    <repository>
      <id>central</id>
      <url>${m2repoUrl}</url>
      <snapshots>
        <enabled>true</enabled>
      </snapshots>
      <releases>
        <enabled>true</enabled>
      </releases>
    </repository>
  </repositories>
  <pluginRepositories>
    <pluginRepository>
      <id>central</id>
      <url>${m2repoUrl}</url>
      <releases>
        <enabled>true</enabled>
      </releases>
      <snapshots>
        <enabled>true</enabled>
      </snapshots>
    </pluginRepository>
  </pluginRepositories>

  <distributionManagement>
    <site>
      <id>site</id>
      <url>${siteUrl}</url>
    </site>
    <repository>
      <id>libs-releases</id>
      <name>Company Internal Release Repository</name>
      <url>dav:${releaseRepoUrl}</url>
    </repository>
    <snapshotRepository>
      <id>libs-snapshots</id>
      <name>Company Internal Snapshot Repository</name>
      <url>dav:${snapshotRepoUrl}</url>
    </snapshotRepository>
  </distributionManagement>

  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>appassembler-maven-plugin</artifactId>
        <version>1.0-beta-2</version>
        <configuration>
          <repositoryLayout>flat</repositoryLayout>
          <includeConfigurationDirectoryInClasspath>true</includeConfigurationDirectoryInClasspath>
          <target>${project.build.directory}</target>
          <defaultJvmSettings>
            <initialMemorySize>${initialMemorySize}</initialMemorySize>
            <maxMemorySize>${maxMemorySize}</maxMemorySize>

            <systemProperties>
              <!--<systemProperty>java.security.policy=conf/policy.all</systemProperty>-->

              <systemProperty>user.timezone=GMT+1</systemProperty>
              <systemProperty>com.sun.management.jmxremote</systemProperty>
              <systemProperty>com.sun.management.jmxremote.port=${jmxremote.port}</systemProperty>
              <systemProperty>com.sun.management.jmxremote.authenticate=false</systemProperty>
              <systemProperty>com.sun.management.jmxremote.ssl=false</systemProperty>
            </systemProperties>

            <extraArguments>
              <extraArgument>-server</extraArgument>
            </extraArguments>
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
                  </configuration>
                </generatorConfiguration>
              </generatorConfigurations>
            </daemon>
          </daemons>
        </configuration>
        <executions>
          <execution>
            <id>libsAndScripts</id>
            <phase>package</phase>
            <goals>
              <goal>generate-daemons</goal>
            </goals>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>rpm-maven-plugin</artifactId>
        <version>2.0-beta-1</version>
        <executions>
          <execution>
            <phase>pre-integration-test</phase>
            <goals>
              <goal>rpm</goal>
            </goals>
          </execution>
        </executions>

        <configuration>
          <requires>
            <require>jdk &gt; 1.6.0</require>
          </requires>
          <release>99999</release> <!-- 99999 means SNAPSHOT -->
          <copyright>${pom.inceptionYear}, ${pom.organization.name}</copyright>
          <group>Applications/Engineering</group>
          <prefix>${rpm.path}</prefix>
          <mappings>
            <mapping>
              <directory>${rpm.path}/run</directory>
              <filemode>660</filemode>
              <username>${rpm.username}</username>
              <groupname>${rpm.groupname}</groupname>
            </mapping>
            <mapping>
              <directory>${rpm.path}/logs</directory>
              <filemode>660</filemode>
              <username>${rpm.username}</username>
              <groupname>${rpm.groupname}</groupname>
            </mapping>
            <mapping>
              <directory>${rpm.path}/bin</directory>
              <filemode>770</filemode>
              <username>${rpm.username}</username>
              <groupname>${rpm.groupname}</groupname>
              <sources>
                <source>
                  <location>${jswDir}/bin</location>
                  <excludes>
                    <exclude>*.bat</exclude>
                    <exclude>*.exe</exclude>
                  </excludes>
                </source>
                <source>
                  <location>bin</location>
                </source>
              </sources>
            </mapping>
            <mapping>
              <directory>${rpm.path}/conf</directory>
              <configuration>true</configuration>
              <filemode>660</filemode>
              <username>${rpm.username}</username>
              <groupname>${rpm.groupname}</groupname>
              <sources>
                <source>
                  <location>${jswDir}/conf</location>
                </source>
                <source>
                  <location>conf</location>
                </source>
              </sources>
            </mapping>
            <mapping>
              <directory>${rpm.path}/etc</directory>  <!-- configuration files which must be in classpath -->
              <configuration>true</configuration>
              <filemode>660</filemode>
              <username>${rpm.username}</username>
              <groupname>${rpm.groupname}</groupname>
              <sources>
                <source>
                  <location>etc</location>
                </source>
              </sources>
            </mapping>
            <mapping>
              <directory>${rpm.path}/lib</directory>
              <filemode>660</filemode>
              <username>${rpm.username}</username>
              <groupname>${rpm.groupname}</groupname>
              <sources>
                <source>
                  <location>${jswDir}/lib</location>
                </source>
              </sources>
            </mapping>
            <mapping>
              <directory>${rpm.path}/lib</directory>
              <filemode>660</filemode>
              <username>${rpm.username}</username>
              <groupname>${rpm.groupname}</groupname>
              <dependency/>
            </mapping>
          </mappings>
          <preinstall>echo Installing ${pom.name}...</preinstall>
          <postinstall>
            echo Configuring ${pom.name} init scripts
            #!/bin/sh
            #echo RPM_INSTALL_PREFIX: $RPM_INSTALL_PREFIX
            #echo prefix: %{prefix}

            ln -s $RPM_INSTALL_PREFIX/bin/${rpm.appname} /etc/init.d/${rpm.appname}
            #update-rc.d ${rpm.appname} start 20 3 5 . stop 20 0 1 2 4 6 .

            # configure chkconfig install

            if [ -x /sbin/chkconfig ]; then
            /sbin/chkconfig --add ${rpm.appname}
            else
            ln -sf /etc/init.d/${rpm.appname} /etc/rc.d/rc3.d/S20${rpm.appname}
            ln -sf /etc/init.d/${rpm.appname} /etc/rc.d/rc5.d/S20${rpm.appname}

            ln -sf /etc/init.d/${rpm.appname} /etc/rc.d/rc0.d/K10${rpm.appname}
            ln -sf /etc/init.d/${rpm.appname} /etc/rc.d/rc1.d/K10${rpm.appname}
            ln -sf /etc/init.d/${rpm.appname} /etc/rc.d/rc2.d/K10${rpm.appname}
            ln -sf /etc/init.d/${rpm.appname} /etc/rc.d/rc4.d/K10${rpm.appname}
            ln -sf /etc/init.d/${rpm.appname} /etc/rc.d/rc6.d/K10${rpm.appname}
            fi

            if [ "$RUN_AS_USER" = "" ]; then
            echo Variable RUN_AS_USER not set, defaulting to root.
            export RUN_AS_USER=root
            fi
            echo Changing ownership according to RUN_AS_USER=$RUN_AS_USER
            chown -Rc $RUN_AS_USER $RPM_INSTALL_PREFIX
            echo chmod ug+x on directories in $RPM_INSTALL_PREFIX
            find $RPM_INSTALL_PREFIX -type d -exec chmod -c ug+x {} \;
          </postinstall>
          <preremove>
            echo Removing ${rpm.appname} ...

            #chkconfig scripts removal
            #only on uninstall, not on upgrades.
            if [ $1 = 0 ]; then
            /etc/init.d/${rpm.appname} stop
            if [ -x /sbin/chkconfig ]; then
            echo "chkconfig --del ${rpm.appname}"
            /sbin/chkconfig --del ${rpm.appname}
            else
            echo "Deleting /etc/rc.d/rc?.d/???${rpm.appname}"
            rm -f /etc/rc.d/rc?.d/???${rpm.appname}
            fi
            fi
          </preremove>

          <postremove>
            echo "Deleting /etc/init.d/${rpm.appname}"
            rm /etc/init.d/${rpm.appname}
            echo ${rpm.appname} is Successfully Removed!
          </postremove>
        </configuration>
      </plugin>
    </plugins>
  </build>

  <properties>
    <repoUrl>http://m2repo.company.local:8081/artifactory</repoUrl>
    <m2repoUrl>${repoUrl}/platform</m2repoUrl>
    <releaseRepoUrl>${repoUrl}/libs-releases</releaseRepoUrl>
    <snapshotRepoUrl>${repoUrl}/libs-snapshots</snapshotRepoUrl>
    <siteBaseUrl>file:///var/www/html/sites</siteBaseUrl>
    <siteUrl>${siteBaseUrl}/lib</siteUrl>

    <rpm.appname>someAppName</rpm.appname>
    <mainClassPackage>com.company</mainClassPackage>
    <mainClass>${mainClassPackage}.SomeLauncher</mainClass>
    <rpm.username>someUserNameHere</rpm.username>
    <rpm.groupname>company-amm</rpm.groupname>
    <rpm.path>/opt/${rpm.appname}</rpm.path>
    <jswDir>${project.build.directory}/jsw/${rpm.appname}</jswDir>
    <!-- TODO  requires manual update -->
    <rpmOutputFile>${project.build.directory}/rpm/RPMS/noarch/${pom.artifactId}-1.1-99999.noarch.rpm</rpmOutputFile>
    <jmxremote.port>8998</jmxremote.port>

    <maxMemorySize>512M</maxMemorySize>
    <initialMemorySize>128M</initialMemorySize>
  </properties>

</project>
```
