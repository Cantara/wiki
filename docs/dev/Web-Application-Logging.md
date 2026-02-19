# Web Application Logging

Some logging features can be configured in the webapp from day 1:

- A console appender for development use
- Log session-id together with each log statement (if any) - this is useful for filtering out the activity of one user
- For test/prod-use, use file appenders (or something better if you have available)
- Roll files daily (depending on traffic)
- Split DEBUG-files from WARN-files, and from ERROR-files

ERROR-log files are just for ERROR-level log statements. These are the ones that should wake you up in the middle of the night by SMS, phone-call, etc.

WARN-log files are for problems that you want to monitor. They should be reviewed daily (send mail report each morning, etc). This can be failing services, depending on how critical it is. These are errors that we can't do anything about there and then.

Use different sort of exceptions to seperate between ERROR and WARN. Try to keep the use of them solely in the top level exception handler.

DEBUG-log files are for all the things you want to have a look at happened before or after a WARNING or ERROR occurs.

You can also use INFO for collecting data that product owners, yourself or others are curious about. It could be wise not to have additivity on this logger.

Be sure to try out SLF4J.
