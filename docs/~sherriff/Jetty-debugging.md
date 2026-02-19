# Jetty-debugging

```
set MAVEN_OPTS=-Xms256m -Xmx1024m -XX:MaxPermSize=128m -agentlib:jdwp=transport=dt_socket,address=7848,server=y,suspend=n
mvn jetty:run
```

Koble til med IntelliJ: JSR4 compatible server, remote, på port 7848.
