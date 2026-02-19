# Error Push Setup

## Error push-like log behaviour/setup

### Log4J.properties config

Add the following to log4j.properties

```
* log4j.appender.HUB=org.apache.log4j.net.SocketHubAppender
* log4j.appender.HUB.layout=org.apache.log4j.PatternLayout
* log4j.appender.HUB.layout.ConversionPattern=[cc]%d{MMM-dd HH:mm:ss} %-14.14c{1}- %m%n
* log4j.appender.HUB.port=9004
```

And add the HUB as a logger (I.e. something like: log4j.rootCategory=INFO, LOG_APPENDER, HUB, CONSOLE_APPENDER, LOG_MEMORYAPPENDER)

### Log4j.xml config

```xml
<appender name="HUB" class="org.apache.log4j.net.SocketHubAppender">  
   <param name="Port" value="9004"/>  
   <param name="Threshold" value="INFO"/>  
</appender>

<root>  
   <appender-ref ref="HUB"/>  
   <appender-ref ref="CONSOLE"/>  
   <appender-ref ref="FILE"/>  
</root> 
```

### Chainsaw config

Look up Chainsaw on apache, and use the WebStart link form the download section. If you need SNMP, JMS or Virtual Filsystem connectors, download them seperately and add them to the modules directory as described on the Chainsaw website.

### Log appenders for Chainsaw

- log4J - Use SocketHubAppender as described above
- java.util.logging
    - [[http://commons.apache.org/downloads/download_logging.cgi](../[http/commons-apache-org-downloads-download_logging-cgi.md)] 
- JMS 
    - [[http://logging.apache.org/chainsaw/distributionnotes.html](../[http/logging-apache-org-chainsaw-distributionnotes-html.md)]
- VFS (Virtual Filesystem)
    - [[http://logging.apache.org/chainsaw/distributionnotes.html](../[http/logging-apache-org-chainsaw-distributionnotes-html.md)]
