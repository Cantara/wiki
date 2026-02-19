# Typical micro service technology stack (java)

Some moments worth considering as a baseline for building micro services in java

Note: This is meant as a baseline, not a quick-start.

|  |  |
| --- | --- |
| - Build as executable jar-file (with maven)   - run as simple as java -jar <filename.jar>   - Dockerized   - Windows Service Enabled - Web container   - embedded jetty if service has extensive API   - embedded netty if service need high scaleability   - jersey (RESTFull services) - Resources   - hystrix circuit breaker to all non-embedded/non-local resources (DB, http(s) ++) - State   - hazelcast (state distribution) - non included yet, mainly because the codebase does not have state (yet) - Useful "extras"   - com.jayway.jsonpath / jackson (json & jsonpath)   - constretto (property resolving and overrides)   - commons.logging/org.slf4j (bridging logging from libraries above) - Seurity   - Basic Auth Internal Resources   - Oauth2 Internal and External Resources - Obvious limitations   - micro services should in most cases log to a central component, most likely AWS CloudWatch - but as of today, we have to pick, add the dependency and adjust the configuration   Legend:   - In baseline codebase on github - Not in baseline codebase on github | Template: <https://github.com/Cantara/microservice-baseline>  Unknown macro: {gliffy} |
