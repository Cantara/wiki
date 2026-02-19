# Classic Spring configuration tactics

## Tactics 

The tactics can be used in isolation, but it is more common to utilize multiple (if not all) of these together to achieve the desired benefits.

#### How to ensure that required properties are set correctly? 

- Generate example file where all properties that can be set are listed, but only the required ones are active. The rest of the properties should be included as comments. 
- expose properties with jmx
- Servlet 

#### PropertyPlaceholderConfigurer
[PropertyPlaceholderConfigurer](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/beans/factory/config/PropertyPlaceholderConfigurer.html) 

(+) Properties can be defined both in property files and directly in the application context. 
(+) Set a property once, use it everywhere. 
(-) Every property _must_ be defined, which obscures the difference between parameters that _must_ be set to get the application running and properties that _may_ be set. (Setting the "not strictly necessary" parameters directly in the properties object in the application context can reduce this problem.) 

#### PropertyOverrideConfigurer
[PropertyOverrideConfigurer](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/beans/factory/config/PropertyOverrideConfigurer.html) 

(+) All properties are defined directly in the bean where they are used. 
(+) All properties can be overridden in property files. 
(-) It is not possible to use the PropertyOverrideConfigurer to use one property in multiple places and override it only once. 

#### Factory-bean/factory-method

```
<bean id="first" class="firstClass">
  <property name="prop1" value="value1"/>
</bean>

<bean id="second" class="secondClass>
  <property name="prop2><bean factory-bean="first" factory-method="prop1"/>
</bean>
```

- Kan dette brukes til fjerne den største ulempen med _PropertyOverrideConfigurer_? 
    - Nei, "NB: A bean that implements this interface cannot be used as a normal bean", [api](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/beans/factory/FactoryBean.html).
