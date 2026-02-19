# How to start ActiveMQ JMS Broker in a separate process

[How do I embed a Broker inside a Connection](http://activemq.apache.org/how-do-i-embed-a-broker-inside-a-connection.html)

TODO: Remember to explain how to set up JNDI. 

Create a helper class, a BrokerManager, to manage the JMS broker. 

```java

protected ActiveMQBrokerManager(final BrokerService brokerService) {
  this.brokerService = brokerService;
}

public void startBroker(final String url)

public void stopBroker() 

public boolean isStarted() 

public void purgeQueue(final Destination destination)

public void purgeAllQueues()

public long getDestinationMessageCount(final Destination destination)

```

Spring wiring for the BrokerService 

```xml
  <bean id="broker" class="org.apache.activemq.broker.BrokerService">
    <property name="persistent" value="false"/>
    <property name="useJmx" value="false"/>
    <property name="deleteAllMessagesOnStartup" value="true"/>
    <!--<property name="useShutdownHook" value="false"/>-->
    <property name="transportConnectorURIs">
      <list>
        <value>tcp://localhost:61616</value>
      </list>
    </property>
  </bean>

  <bean id="brokerManager" class="com.company.ActiveMQBrokerManager">
    <constructor-arg ref="broker"/>   
  </bean>

```
