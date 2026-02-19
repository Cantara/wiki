# logback.xml example

```xml
<configuration scan="true" scanPeriod="60 seconds">
    <property name="LOG_DIR" value="logs" />
    <property name="AUDIT_LOG_DIR" value="logs/audit" />

    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <appender name="logfile" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_DIR}/app1.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${LOG_DIR}/app1-%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>50MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
        </rollingPolicy>
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{35} - %msg%n</pattern>
        </encoder>
    </appender>
   
    <appender name="performance" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_DIR}/performance.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${LOG_DIR}/performance-%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>7</maxHistory>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>50MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
        </rollingPolicy>
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{35} - %msg%n</pattern>
        </encoder>
    </appender>
 
    <appender name="auditlog_login" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${AUDIT_LOG_DIR}/auditlog_login.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${AUDIT_LOG_DIR}/auditlog_login-%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>50MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
        </rollingPolicy>
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} %msg%n</pattern>
        </encoder>
    </appender>
   

    <!-- Redirect logging to other appenders -->    
    <logger name="auditlog_login" level="INFO" additivity="false">
        <appender-ref ref="auditlog_login" />
    </logger>

    <!-- Reduce logging from dependencies -->
    <logger name="org.hibernate" level="WARN"/>
    <logger name="org.apache" level="WARN"/>

    <logger name="com.company.app1" level="INFO"/>

    <root level="INFO">
        <appender-ref ref="logfile" />
    </root>
</configuration>
```
