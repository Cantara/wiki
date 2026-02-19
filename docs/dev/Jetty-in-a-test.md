# Jetty in a test

## How to use Jetty in a test

Use this alternative for automated tests and debugging. 

#### Add the jetty dependencies to pom.xml 
```xml
<!-- standard jetty server -->
<dependency>
  <groupId>org.mortbay.jetty</groupId>
  <artifactId>jetty</artifactId>
  <version>6.0.0</version>
  <scope>test</scope>
</dependency>
<!-- classes for running jetty as a normal java library -->
<dependency>
  <groupId>org.mortbay.jetty</groupId>
  <artifactId>start</artifactId>
  <version>6.0.0</version>
  <scope>test</scope>
</dependency>
```

#### Launch the jetty server

```java
public class JettyLauncher {
  public static void main(String[] args) {
  SocketConnector connector = new SocketConnector();
  connector.setPort(9090);
  WebAppContext firstHandler = new WebAppContext();
  firstHandler.setContextPath("/my-webapp");
  firstHandler.setWar("./skade-web/src/main/webapp");
  Server server = new Server();
  server.addConnector(connector);
  server.setHandler(firstHandler);
  try {
    server.start();
    Thread.sleep(100000); //Makes sure the server doesn't die
  } catch (Exception e) {
    e.printStackTrace();
  }
}
```
