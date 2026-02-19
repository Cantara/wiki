# Deploy to different environments - run-time

## Run-time approach 

The goal is to avoid building artifacts for different environments. This problem can be divided into the following sub-problems: 

- Make the application environment-independent. I.e., by default is should not have any dependencies to external systems. 

- Use property files from classpath to override default configuration. It should for example be possible to use an external database instead of the default embedded one by defining properties in a property file. 

## Suggested implementation 

We assume that the application use _Dependency Injection_. The default configuration should depend on embedded products only. 

The Proof-of-Concept code uses Spring's IoC container. To override this defaults we use _PropertyOverrideConfigurer_ instead of the more common _PropertyPlaceholderConfigurer_. The following example use HSQLDB by default, but can be configured to use another database by adding a deploy.properties file to classpath. 

```
<bean id="propertyConfigurer"
      class="org.springframework.beans.factory.config.PropertyOverrideConfigurer">
    <property name="location">
          <value>classpath:deploy.properties</value>
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
 
Note that we have explicitly specified _deploy.properties_ in the PropertyOverrideConfigurer, because there should only be one such deployment descriptor. To use PostgreSQL instead of HSQLDB, put the following into deploy.properties: 

```
dataSource.driverClassName=org.postgresql.Driver
dataSource.url=jdbc:postgresql://db.abakus.no/naut
dataSource.username=naut
dataSource.password=prodDataSourcePasswordHere

sessionFactory.hibernateProperties[java:hibernate.dialect]=org.hibernate.dialect.PostgreSQLDialect
```

If you need to change **many** properties, it might be better to choose _beans_ using a configurer and just use deploy.properties to set which combination of beans to use. See [Alef Arendsen's blog](http://blog.arendsen.net/index.php/2005/03/12/configuration-management-with-spring/) for details on how to set this up. (NOTE! Erik tried this approach, but could not get it to work.) 

#### How to enforce that all relevant properties are changed when deploying to a different environment? 

(If one or two settings are off, the result might be very hard to debug.) 
This problem can be reduced by minimizing the number of properties that needs to be set. 

- We could distribute the application as a zip archive that contains template-files and readmes in addition to the artifact. This solution is far from ideal, but it is currently my best suggestion.
