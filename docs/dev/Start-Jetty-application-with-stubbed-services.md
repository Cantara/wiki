# Start Jetty application with stubbed services

###### Start the application, but override what services are initialized 

Inspiration: [https://github.com/ivarconr/jersey2<sub>~spring3</sub><sub>webapp](https://github.com/ivarconr/jersey2</sub><sub>spring3</sub>~webapp) 

###### Main class

```
public Main(int jettyPort) {
    this.jettyPort = jettyPort;
    server = new Server(jettyPort);

    URL url = ClassLoader.getSystemResource("webapp/WEB-INF/web.xml");
    resourceBase = url.toExternalForm().replace("/WEB-INF/web.xml", "");
}

public void start() throws Exception {
    WebAppContext context = new WebAppContext();
    log.debug("Start Jetty using resourcebase={}", resourceBase);
    context.setDescriptor(resourceBase + "/WEB-INF/web.xml");
    context.setResourceBase(resourceBase);
    context.setContextPath(CONTEXT_PATH);
    context.setParentLoaderPriority(true);
    server.setHandler(context);

    server.start();
}
```

###### Test class 

```
@BeforeClass
public void startServer() throws Exception {
    main = new Main(8301);

    //Override web.xml and application context to applicationContext-stubbed-service-layer.xml.
    String rootPath = ClassLoader.getSystemResource("logback.xml").toExternalForm().replace("/target/classes/logback.xml", "");
    String resourceBase = rootPath + "/src/test/webapp";
    main.setResourceBase(resourceBase);
    main.start();
}

```
