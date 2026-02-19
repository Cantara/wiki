# Generic Parent POM Example

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.company</groupId>
  <artifactId>company-parent</artifactId>
  <version>29</version>
  <packaging>pom</packaging>
  <name>Company Parent POM</name>
  <url>http://m2sites.company.com/sites/</url>

  <scm>
    <connection>
      scm:svn:svn+ssh://svn.company.com/var/local/repo/lib/company-parent/trunk
    </connection>
    <developerConnection>
      scm:svn:svn+ssh://svn.company.com/var/local/repo/lib/company-parent/trunk
    </developerConnection>
  </scm>

  <issueManagement>
    <system>jira</system>
    <url>http://10.0.0.10:8080/</url>
  </issueManagement>

  <ciManagement>
    <system>Continuum</system>
    <url>http://ci.company.com:8080/continuum</url>
    <notifiers>
      <notifier>
        <configuration>
          <address>dev-team-svn@company.com</address>
        </configuration>
      </notifier>
    </notifiers>
  </ciManagement>

  <inceptionYear>2008</inceptionYear>

  <mailingLists>
    <mailingList>
      <name>Dev Team</name>
      <post>dev-team@company.com</post>
    </mailingList>
  </mailingLists>

  <licenses>
    <license>
      <name>Company License</name>
      <comments>Some license</comments>
    </license>
  </licenses>

  <organization>
    <name>Com company</name>
    <url>${pom.url}</url>
  </organization>

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

  <build>
    <extensions>
      <extension>
        <groupId>org.apache.maven.wagon</groupId>
        <artifactId>wagon-webdav</artifactId>
        <version>1.0-beta-2</version>
      </extension>
      <extension>
        <groupId>org.apache.maven.wagon</groupId>
        <artifactId>wagon-ssh</artifactId>
        <version>1.0-beta-2</version>
      </extension>
    </extensions>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>com.google.code.maven-license-plugin</groupId>
          <artifactId>maven-license-plugin</artifactId>
          <version>1.4.0</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-antrun-plugin</artifactId>
          <version>1.3</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-assembly-plugin</artifactId>
          <version>2.2-beta-3</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-clean-plugin</artifactId>
          <version>2.3</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-dependency-plugin</artifactId>
          <version>2.1</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-deploy-plugin</artifactId>
          <version>2.4</version>
        </plugin>

        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-eclipse-plugin</artifactId>
          <version>2.5.1</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-help-plugin</artifactId>
          <version>2.1</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-idea-plugin</artifactId>
          <version>2.2</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-install-plugin</artifactId>
          <version>2.2</version>
          <configuration>
            <createChecksum>true</createChecksum>
          </configuration>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-release-plugin</artifactId>
          <version>2.0-beta-8</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-remote-resources-plugin</artifactId>
          <version>1.0</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-resources-plugin</artifactId>
          <version>2.3</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-scm-plugin</artifactId>
          <version>1.1</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-enforcer-plugin</artifactId>
          <version>1.0-beta-1</version>
        </plugin>
      </plugins>
    </pluginManagement>

    <plugins>
      <!--http://jira.codehaus.org/browse/MRELEASE-271-->
      <plugin>
        <artifactId>maven-release-plugin</artifactId>
        <configuration>
          <useReleaseProfile>false</useReleaseProfile>
          <preparationGoals>clean install</preparationGoals>
        </configuration>
      </plugin>

      <plugin>
        <artifactId>maven-eclipse-plugin</artifactId>
      </plugin>
      <plugin>
        <artifactId>maven-idea-plugin</artifactId>
        <configuration>
          <jdkName>${jdkVersion}</jdkName>
          <jdkLevel>${jdkVersion}</jdkLevel>
        </configuration>
      </plugin>
      <plugin>
        <artifactId>maven-dependency-plugin</artifactId>
        <executions>
          <execution>
            <id>unpack-shared-resources</id>
            <goals>
              <goal>unpack-dependencies</goal>
            </goals>
            <phase>validate</phase>
            <configuration>
              <outputDirectory>${generatedResourcesDir}</outputDirectory>
              <includeArtifactIds>company-reporting-resources</includeArtifactIds>
              <includeGroupIds>com.company.resources</includeGroupIds>
              <excludeTransitive>true</excludeTransitive>
            </configuration>
          </execution>
        </executions>
      </plugin>
      <plugin>
        <groupId>com.google.code.maven-license-plugin</groupId>
        <artifactId>maven-license-plugin</artifactId>
        <configuration>
          <header>${generatedResourcesDir}/company-header.txt</header>
          <failIfMissing>true</failIfMissing>
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

  <dependencies>
    <dependency>
      <groupId>com.company.resources</groupId>
      <artifactId>company-reporting-resources</artifactId>
      <version>9</version>
    </dependency>
  </dependencies>

  <reporting>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-site-plugin</artifactId>
        <version>2.0-beta-7</version>
        <inherited>true</inherited>
        <configuration>
          <locales>en</locales>
          <inputEncoding>${encoding}</inputEncoding>
          <outputEncoding>${encoding}</outputEncoding>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-project-info-reports-plugin</artifactId>
        <version>2.1.1</version>
        <!-- If all goals are relevant, the whole reportSet can be omitted. -->
        <!-- Goals: http://maven.apache.org/plugins/maven-project-info-reports-plugin/plugin-info.html-->
      </plugin>
    </plugins>
  </reporting>

  <distributionManagement>
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
    <site>
      <id>site</id>
      <url>${siteUrl}</url>
    </site>
  </distributionManagement>

  <properties>
    <generatedResourcesDir>${project.build.directory}/generated-resources</generatedResourcesDir>
    <schemaDir>${generatedResourcesDir}/schemas</schemaDir>

    <scmBaseUrl>scm:svn:svn+ssh://svn.company.com/var/local/repo</scmBaseUrl>
    <repoUrl>http://m2repo.company.com:8081/artifactory</repoUrl>
    <m2repoUrl>${repoUrl}/platform</m2repoUrl>
    <releaseRepoUrl>${repoUrl}/libs-releases</releaseRepoUrl>
    <snapshotRepoUrl>${repoUrl}/libs-snapshots</snapshotRepoUrl>
    <siteUrl>file:///var/www/html/sites/${pom.artifactId}/${pom.version}</siteUrl>

    <encoding>UTF-8</encoding>
    <jdkVersion>1.6</jdkVersion>
    <surefireVersion>2.4.3</surefireVersion>
    <cobertura.version>2.2</cobertura.version>
    <pmdVersion>2.4</pmdVersion>
    <findbugsVersion>1.2</findbugsVersion>
  </properties>

  <profiles>
    <profile>
      <id>ide</id>
      <build>
        <plugins>
          <plugin>
            <artifactId>maven-idea-plugin</artifactId>
            <configuration>
              <downloadSources>true</downloadSources>
              <downloadJavadocs>true</downloadJavadocs>
            </configuration>
          </plugin>
          <plugin>
            <artifactId>maven-eclipse-plugin</artifactId>
            <configuration>
              <downloadSources>true</downloadSources>
              <downloadJavadocs>true</downloadJavadocs>
            </configuration>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>

</project>
```
