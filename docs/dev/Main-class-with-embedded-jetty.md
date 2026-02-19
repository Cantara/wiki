# Main class with embedded jetty

```
public class Main {

private static final Logger log = LoggerFactory.getLogger(Main.class);

    private Server server;

    public static void main(String[] arguments) {
        int portNumber = 4302;
        Main main = new Main(portNumber);
        main.start();
        main.join();
    }

    public void start()  {
        ResourceHandler resource_handler = new ResourceHandler();
        resource_handler.setDirectoriesListed(true);
        resource_handler.setWelcomeFiles(new String[]{"index.html"});

        URL urlToStaticResources = ClassLoader.getSystemResource("index.html");
        String resourceBaseStatic = urlToStaticResources.toExternalForm().replace("index.html", "");

        URL urlToStaticResources2 = ClassLoader.getSystemResource("config_override.js");
        String[] resourcePaths = new String[]{resourceBaseStatic};
        if (urlToStaticResources2 != null) {
            String resourceBaseStatic2 = urlToStaticResources2.toExternalForm().replace("config_override.js", "");
            log.debug("resourceBaseStatic2={}", resourceBaseStatic2);
            resourcePaths = new String[]{resourceBaseStatic, resourceBaseStatic2};
        }
        resource_handler.setBaseResource(new ResourceCollection(resourcePaths));

        HandlerList handlers = new HandlerList();
        handlers.setHandlers(new Handler[]{resource_handler, new DefaultHandler()});
        server.setHandler(handlers);

        try {
            server.start();
        } catch (Exception e) {
            log.error("Error during Jetty startup. Exiting", e);
            System.exit(1);
        }
        int localPort = getPortNumber();
        log.info("Jetty server started on port {}", localPort);
    }

}

```
