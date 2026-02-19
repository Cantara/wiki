# Platform dependent artifacts

## Example with JMS-client 

While we strive to make our artifacts platform independent, this is not always possible. The _java.naming.factory.initial_<sub>~property needed by [JndiTemplate](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/jndi/JndiTemplate.html) requires that the given implementation of _ContextFactory_ is present on the classpath. Putting the property in a external property</sub><sub>file is a good idea and makes the Spring</sub><sub>setup environment independent. However, switching between multiple jms</sub>~servers requires different jar-files. 

#### Switch jar-files directly with assembly

If different jar-files is the only difference, and all combinations are relevant, assembly seems a suitable choice. 

1. Create a component that includes everything that is common. 
1. Create one component and one assembly descriptor for each different jms-implementation 

#### Switch jar-files using profiles 
 
If you have other changes in addition to switching dependency or you just are interested in one assembly or the other, use profiles. Here is how to implement: 

Use profiles to choose which dependency to include. 
 
  <profiles>
    <profile>
      <id>jmsImpl_activemq</id>
      <activation>
        <property>
          <name>jmsImpl</name>
          <value>activemq</value>
        </property>
      </activation>
      <properties>
        <jmsImpl>activemq</jmsImpl>
      </properties>
      <dependencies>
        <dependency>
          <groupId>org.apache.activemq</groupId>
          <artifactId>activemq-core</artifactId>
          <version>5.1.0</version>
        </dependency>
      </dependencies>
    </profile>
    <profile>
      <id>jmsImpl_weblogic</id>
      <activation>
        <property>
          <name>!jmsImpl</name>
        </property>
      </activation>
      <properties>
        <jmsImpl>weblogic</jmsImpl>
      </properties>
      <dependencies>
        <dependency>
          <groupId>bea.weblogic</groupId>
          <artifactId>wlclient</artifactId>
          <version>9.2.0.0</version>
        </dependency>
        <dependency>
          <groupId>bea.weblogic</groupId>
          <artifactId>wljmsclient</artifactId>
          <version>9.2.0.0</version>
        </dependency>
      </dependencies>
    </profile>
  </profiles>
```

Note that if _jmsImpl_ is not set, we use weblogic by default. ActiveMQ can be used by using _-DjmsImpl=activemq_. 

The jmsImpl-property should be used as part of the assembly outputname to illustrate which jms-implementation it supports. [Classifier | http://maven.apache.org/plugins/maven-assembly-plugin/assembly-mojo.html#classifier] is the natural choice, but it is also possible to postfix it to the finalName. 

```
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven<sub>~assembly</sub>~plugin</artifactId>
  <configuration>
    <finalName>$-$</finalName>
  </configuration>
</plugin> 
```

```
