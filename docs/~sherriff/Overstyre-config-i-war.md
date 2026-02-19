# Overstyre config i war

```xml
<bean id=propertyConfigurer class=org.springframework.beans.factory.config.PropertyPlaceholderConfigurer^gt;
<property name=locations>
<list>
<value>classpath:/competities.properties</value>
<value>file:${user.home}/someApp.properties</value>
</list>
</property>
<property name=ignoreResourceNotFound value=true/>
</bean>
```

http://www.summa-tech.com/blog/2009/04/20/6-tips-for-managing-property-files-with-spring/
