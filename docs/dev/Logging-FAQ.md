# Logging FAQ

#### What are the most popular log levels? 

###### Log4j Log Levels 
| Log level | Description |  |
| --- | --- | --- |
| FATAL | The FATAL level designates very severe error events that will presumably lead the application to abort. |
| ERROR | The ERROR level designates error events that might still allow the application to continue running. |
| WARN | The WARN level designates potentially harmful situations. |
| INFO | The INFO level designates informational messages that highlight the progress of the application at coarse-grained level. |
| DEBUG | The DEBUG Level designates fine-grained informational events that are most useful to debug an application. |
| TRACE | The TRACE  Level designates finer-grained informational events than the DEBUG. |
| TRACE_INT | TRACE level integer value. |
| OFF | The OFF has the highest possible rank and is intended to turn off logging. |
| ALL | The ALL has the lowest possible rank and is intended to turn on all logging. |

Reference: [log4j LEVEL](http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/Level.html)

###### java.util.logging Levels 
| Log level | Description |  |
| --- | --- | --- |
| SEVERE | SEVERE is a message level indicating a serious failure. |
| WARNING | WARNING is a message level indicating a potential problem. |
| INFO | INFO is a message level for informational messages. |
| CONFIG | CONFIG is a message level for static configuration messages. |
| FINE | FINE is a message level providing tracing information. |
| FINER | FINER indicates a fairly detailed tracing message. |
| FINEST | FINEST indicates a highly detailed tracing message. |
| OFF | OFF is a special level that can be used to turn off logging. |
| ALL | ALL indicates that all messages should be logged. |

Reference: [java.util.logging.Level](http://java.sun.com/javase/6/docs/api/java/util/logging/Level.html)

#### commons-logging or not? 

commons<sub>~logging 1.1 brought in a series of unnecessary transitive dependencies and was it's use was considered to be an anti</sub>~pattern. This has been fixed in version 1.1.1, but still very few use cases justify the use of commons-logging.
So, avoid commons-logging. A facade to the logging tool seldom adds any value and the level of indirection can thus be avoided. 

#### How to choose tool 

For debug logging prefer slf4j over log4j and prefer log4j over java.util.logging. 

**TODO** write about which features make slf4j a more enticing choice than log4j. 

#### log4j: xml or properties configuration? 

If log4j is used, prefer the xml configuration, because it has more features than .property configuration. 

#### Can AOP be used to wrap log statements in if (isDebugEnabled()) statements? 

No, it appears that (at least with AspectJ) this is not a possible as illustrated by the following mail threads: 

- [Preventing method parameters from being evaluated in advice](http://dev.eclipse.org/mhonarc/lists/aspectj-users/msg09674.html)
- [Logging enabled check idea](http://dev.eclipse.org/mhonarc/lists/aspectj-users/msg06225.html) 

#### When to use is<LogLevel>Enabled

(+) Gives a tiny performance improvement
(-) Reduces readabiliry

- [When to call isDebugEnabled](http://livingtao.blogspot.com/2007/05/when<sub>~to</sub><sub>call</sub><sub>isdebugenabled</sub>~before.html)

**TODO**: Update with better references and more details.
