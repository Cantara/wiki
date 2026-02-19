# Monitoring

| Implementation/Product | Type | Description |
| --- | --- | --- |
| [Java Service Wrapper (JSW)](http://wrapper.tanukisoftware.org/doc/english/introduction.html#reliability) | JVM | The Wrapper monitors a JVM process and automatically restarts it if it that the JVM has crashed or hung. This process takes just a few seconds once the Wrapper has decided there is a problem. There is also a way to configure the Wrapper to monitor the console output of a JVM and react to certain strings by restarting or shutting down the JVM. |
| [Solaris Service Management Facility (SMF)](http://www.sun.com/bigadmin/content/selfheal/smf-quickstart.jsp) | Process | Failed services are automatically restarted in dependency order |
| HP Openview Operations |  | Agent |
| [Big Brother](http://bb4.com/) | Application, network |  |
| [Monitoring and Management Using JMX](http://java.sun.com/j2se/1.5.0/docs/guide/management/agent.html) |  |  |
| Life-cycle messages to JMS Topic |  |  |
