# Logging

The purpose of this page is to collect sound advice with regards to how to set up logging in large and possibly distributed systems.

### Purpose and responsibility

- [Debug log](/web/20210225100951/https://wiki.cantara.no/display/dev/Debug+log "Debug log")

- Error log to trigger actions from operations.
  - [Error Handling And Exception Management](/web/20210225100951/https://wiki.cantara.no/display/dev/Error+Handling+And+Exception+Management "Error Handling And Exception Management")

- [Audit log](/web/20210225100951/https://wiki.cantara.no/display/dev/Audit+log "Audit log")

See also [Logging FAQ](/web/20210225100951/https://wiki.cantara.no/display/dev/Logging+FAQ "Logging FAQ").

### Implementation

The log implementation should match the requirements for the application, but it is possible to use different implementations for different needs.

- File based logging
- Loghost - centralized logging
- Event based logging - implemented with for example JMS Topics.

### Resources

- [Log Tools](/web/20210225100951/https://wiki.cantara.no/display/dev/Log+Tools "Log Tools")

- [The best way to clean things up is to avoid them getting dirty in the first place, by Johannes Brodwall](http://brodwall.com/johannes/blog/2008/09/27/the-best-way-to-clean-things-up-is-to-avoid-them-getting-dirty-in-the-first-place/)
- [Verbose logging will disturb your sleep, by Johannes Brodwall](http://brodwall.com/johannes/blog/2008/10/28/verbose-logging-will-disturb-your-sleep/)
- [The Problem With Logging, by Jeff Atwood](http://www.codinghorror.com/blog/archives/001192.html)
- Best Practice within Java Web Application Development. Was at: <http://org.ntnu.no/feta/report.pdf>, chap 5.4 and 5.3.

### References

- <http://www.javacodegeeks.com/2011/01/10-tips-proper-application-logging.html>
