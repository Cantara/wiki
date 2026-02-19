# Service Management, Operations and Monitoring

### Service Management beyond OS-Operations

|  | **Vision** Observe, notify, brag of success or fix problem. |

###### What you need

- Heartbeat on each service.
- Trace metrics for every service call, in prod. You must know your daily behavior to efficiently find your performance hickups.
- Each service must show it's usage, and value.
- Usable, and available logs
  - Info (add new user, new operation)
  - Error handling (user/consumer tried to do something that didn't work)
  - Exception (something unexpectedly wrong happened)
- Audit Logs

|  | **% Average is a lie!** Use metrics like 80, 90, 95% percentile. Record all individual calls that are extremely slow. |

### Metrics

###### Base elements

- Business Value → Observe userstorries accomplished. Tell the success story. What value did you provide to your customers.
- Operational Metrics → Observe functionality. Which functions are used, which functions are not used? Does upgrade increase or decrease end-user usage?
- Technical Metrics → Observe usage, what is the number of requests. What is the rate of 200/404/5xx responses?
  - Performance Metrics → Observe everything that happen in production. Sumarize valuable metrics, then discard raw data. Create a basic understanding of how your services operate in the wild.

### Tools available

**Available Logs**

- [Logback](http://logback.qos.ch/) - log4j successor. Has web front for logs.

**Heartbeat**

- [Metrics Health Check - pull](http://metrics.codahale.com/getting-started/#health-checks)
- We do need a framework that let the service itself push "i'm alive and fine/not fine" signal.

**Metrics provider**

- <http://metrics.codahale.com/>
- [Metrics 4 Spring](http://metrics.codahale.com/manual/spring/)

**Metrics consumer and GUI**

- [Ganglia, scalable distributed monitoring](http://ganglia.sourceforge.net/)
- [Graphite, scalable Realtime Graphing](http://graphite.wikidot.com/)
- [Nagios](http://nagios.org/)

### Commercial tools

- [AppDynamics](http://www.appdynamics.com/) - Monitor each service, GUI, non-introsiv - expensive. Follow trace through chain of servers.
  - [AppDynamics Lite](http://info.appdynamics.com/free_java_profiler_monitoring_tool.html) - Free for single JVM.
- [New Relic](https://newrelic.com/) - Monitor performance metrics in production. Monitor all services.
