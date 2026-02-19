# Change environment at build-time using profiles

## Background

Deployment configuration like username, passwords, urls, etc. should _never_ be included in artifacts. The output of a build should be environment independent! 
However, it is quite useful to be able to _**test**_ an artifact in different environments without too much hassle. This can be achieved with the use of profiles.

#### Drivers for the solution

- one simple command to switch between environments
- easy to see which properties are used 
- no template files in Version Control System (VCS)

## Solution

By default the application has no dependencies to external systems. HSQLDB is used as an embedded, in-memory database and is configured without use of a profile. HSQLDB is used when running _mvn install_. 

There is one profile for _test_ (aka. staging, CI, rc, etc.) and one profile for _prod_. The difference between test and prod can typically be different hardware, different OS or the amount of test data. The profiles are activated by setting the system property _env_; e.g., _mvn install -Denv=test_. A system property was chosen instead of just activation the profile directly, because the property is also used by Spring's applicationContext to select which property files to read (PropertyOverrideConfigurer), AND it is used to activate another profile in settings.xml which makes username and password available (with filtering). 

#### Proof of Concept
A working, real-life example of this PoC can be found in the [NAUT project](http://svn.abakus.no/naut/tags/release-1.3.1). The links above each code snippet links directly to NAUTs subversion repository. 

[pom.xml](http://svn.abakus.no/naut/tags/release-1.3.1/pom.xml)

```
<profiles>
  <profile>
    <id>test</id>
    <activation>
      <property>
        <name>env</name>
        <value>test</value>
      </property>
    </activation>
    <build>
      <resources>
        <resource>
          <filtering>true</filtering>
          <directory>src/main/conf</directory>
          <includes>
            <include>${env}-*.properties</include>
          </includes>
        </resource>
      </resources>
      <plugins>
        <plugin>
          <artifactId>maven-antrun-plugin</artifactId>
          <executions>
            <execution>
              <phase>process-resources</phase>
              <goals>
                <goal>run</goal>
              </goals>
              <configuration>
                <tasks>
                  <delete>
                    <fileset dir="${project.build.outputDirectory}"
                             includes="*-hibernate.properties" excludes="${env}-hibernate.properties"/>
                  </delete>
                </tasks>
              </configuration>
            </execution>
          </executions>
        </plugin>
        <plugin>
          <artifactId>maven-war-plugin</artifactId>
          <configuration>
            <classifier>${env}</classifier>
            <outputDirectory>/var/www/test.abakus.no/app</outputDirectory>
          </configuration>
        </plugin>
      </plugins>
    </build>
  </profile>
  <profile>
    <id>prod</id>
    <activation>
      <property>
        <name>env</name>
        <value>prod</value>
      </property>
    </activation>
    <build>
      <resources>
        <resource>
          <filtering>true</filtering>
          <directory>src/main/conf</directory>
          <includes>
            <include>${env}-*.properties</include>
          </includes>
        </resource>
      </resources>
      <plugins>        
        <plugin>
          <artifactId>maven-antrun-plugin</artifactId>
          <executions>
            <execution>
              <phase>process-resources</phase>
              <goals>
                <goal>run</goal>
              </goals>
              <configuration>
                <tasks>
                  <fileset dir="${project.build.outputDirectory}"
                             includes="*-hibernate.properties" excludes="${env}-hibernate.properties"/>
                </tasks>
              </configuration>
            </execution>
          </executions>
        </plugin>
        <plugin>
          <artifactId>maven-war-plugin</artifactId>
          <configuration>
            <classifier>${env}</classifier>
            <outputDirectory>/var/www/abakus.no/app</outputDirectory>
          </configuration>
        </plugin>
      </plugins>
    </build>
  </profile>
</profiles>
```
 

[test-hibernate.properties](http://svn.abakus.no/naut/tags/release-1.3.1/src/main/conf/test-hibernate.properties):

```
dataSource.driverClassName=org.postgresql.Driver
dataSource.url=jdbc:postgresql://dev-db.abakus.no/testDBname
dataSource.username=username
dataSource.password=${test.dataSource.password} #Set this property in settings.xml

sessionFactory.hibernateProperties[java:hibernate.dialect]=org.hibernate.dialect.PostgreSQLDialect
```

[prod-hibernate.properties](http://svn.abakus.no/naut/tags/release-1.3.1/src/main/conf/prod-hibernate.properties):
```
dataSource.driverClassName=org.postgresql.Driver
dataSource.url=jdbc:postgresql://db.abakus.no/prodDBname
dataSource.username=username
dataSource.password=${prod.dataSource.password}     #Set this property in settings.xml

sessionFactory.hibernateProperties[java:hibernate.dialect]=org.hibernate.dialect.PostgreSQLDialect
```

[applicationContext.xml](http://svn.abakus.no/naut/tags/release-1.3.1/src/main/resources/applicationContext.xml):

```
 <bean id="propertyConfigurer"
        class="org.springframework.beans.factory.config.PropertyOverrideConfigurer">
    <property name="ignoreResourceNotFound" value="true" />
    <property name="location">
      <value>classpath:${env}-hibernate.properties</value>
    </property>
  </bean>

  <bean id="dataSource"
        class="org.apache.commons.dbcp.BasicDataSource"
        destroy-method="close">
    <property name="driverClassName">
      <value>org.hsqldb.jdbcDriver</value>
    </property>
    <property name="url">
      <value>jdbc:hsqldb:mem:naut</value>
    </property>
    <property name="username">
      <value>sa</value>
    </property>
    <property name="password">
      <value></value>
    </property>

    <property name="removeAbandoned">
      <value>true</value>
    </property>
    <property name="removeAbandonedTimeout">
      <value>60</value>
    </property>
    <property name="logAbandoned">
      <value>true</value>
    </property>
  </bean>

  <bean id="sessionFactory"
        class="org.springframework.orm.hibernate3.LocalSessionFactoryBean">
    <property name="dataSource" ref="dataSource"/>

    <!-- XDoclet Mappings -->
    <property name="mappingDirectoryLocations">
      <list>
        <value>classpath:/no/abakus/naut/entity</value>
      </list>
    </property>

    <property name="hibernateProperties">
      <props>
        <prop key="hibernate.dialect">org.hibernate.dialect.HSQLDialect</prop>
        <prop key="hibernate.query.substitutions">true 'T', false 'F'</prop>
        <!--<prop key="hibernate.hbm2ddl.auto">create-drop</prop>-->
        <prop key="hibernate.show_sql">false</prop>

        <prop key="hibernate.c3p0.acquire_increment">3</prop>
        <prop key="hibernate.c3p0.idle_test_period">30</prop>
        <prop key="hibernate.c3p0.timeout">600</prop>
        <prop key="hibernate.c3p0.max_size">50</prop>
        <prop key="hibernate.c3p0.min_size">5</prop>
        <prop key="hibernate.c3p0.max_statements">50</prop>
      </props>
    </property>
  </bean>
```

Sensitive properties can be overridden by adding them to ~/.m2/settings.xml. E.g.: 

```
<settings>
 <profiles>  
    <profile>
      <id>test-erik</id>
      <activation>
        <property>
          <name>env</name>
          <value>test</value>
        </property>
      </activation>
      <properties>
        <!--<dataSource.url>jdbc:postgresql://dev-db.abakus.no/naut</dataSource.url>-->
        <test.dataSource.password>pwForTestDBFromSettings</test.dataSource.password>
      </properties>
    </profile>
    <profile>
      <id>prod-erik</id>
      <activation>
        <property>
          <name>env</name>
          <value>prod</value>
        </property>
      </activation>
      <properties>
        <!--<dataSource.url>jdbc:postgresql://dev-db.abakus.no/naut</dataSource.url>-->
        <prod.dataSource.password>pwForProdDBFromSettings</prod.dataSource.password>
      </properties>
    </profile>
  </profiles>
</settings>
```

## Pros and cons

- Pro
    - Minimal impact, can be shared across projects
    - Creates artifacts with "classifiers": dev, test, prod
    - Maven and VCS makes it easier to share 
- Con 
    - Deployment configuration is included in the artifact
    - Every environment needs its own profile 

## Resources

[Configuration-management with Spring](http://blog.arendsen.net/index.php/2005/03/12/configuration-management-with-spring/)
[Multiple, separate PropertyPlaceholderConfigurers in Spring](http://www.cwinters.com/news/display/3395) 
[Building for different environments](http://maven.apache.org/guides/mini/guide-building-for-different-environments.html)
[A Maven2 multi-environment filter setup](http://sujitpal.blogspot.com/2006/10/maven2-multi-environment-filter-setup.html)
