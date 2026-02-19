# Domain objects having dependencies to services

There are legitimate reasons why some domain objects should have dependencies to either services, repositories, or factories. The interfaces to the above three type of objects are part of the domain model, and entities and value objects can interact with these as appropriate. This also makes it easier to implement rich domain objects and avoiding bloated service layers/transaction scripts. 

One technical problem is how to inject the service object reference into the domain object in need of the service (or repos or factories). Typically applications use an IOC-container to manage the creation of service objects, while domain objects (usually POJO's) are constructed either manually in code or by an ORM framework. Several solutions exist depending on the tool set available:

1. The preferred technique using Spring as the IOC container, is to use AOP. Annotate the domain class as `@Configurable`, and then either use `@Autowired` or create a bean definition for the class in the Spring xml file. Also remember to include `<context:spring<sub>~configured/>` in the xml configuration. The greatest benefit is that it requires the least effort to implement. The solution however requires Spring version 2.0 or newer, and AspectJ for the AOP weaving. Compile</sub><sub>time weaving is preferable to load</sub><sub>time weaving because you avoid having to modify the startup scripts of your application container. For those using Maven, there is an AspectJ compiler plugin available here: [http://mojo.codehaus.org/aspectj</sub><sub>maven</sub><sub>plugin/](http://mojo.codehaus.org/aspectj</sub>~maven-plugin/). If the use of AOP is not possible, use one of the other two approaches.
1. Create a Hibernate [Interceptor](http://www.hibernate.org/hib_docs/v3/api/org/hibernate/Interceptor.html), and override the onLoad method (plus a few more) so that you can create the object yourself in code and inject the necessary references. It is quite possible to create this Interceptor generic and use Spring to configure the dependencies.
1. Use a [ServiceLocator](http://martinfowler.com/articles/injection.html#UsingAServiceLocator). To make the service locator access the Spring context you can have the class implement the ApplicationContextAware interface and put the context in a static field. Simplified example follows:
```
public class ServiceLocator implements ApplicationContextAware
{
    private static ApplicationContext appContext;

    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        appContext = applicationContext;
    }
	
    public static Object getBean(String beanName) {
        return appContext.getBean(beanName);
    }
}
```
