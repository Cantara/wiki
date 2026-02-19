# StatisticsService-ClientLibrary

### Background

- Common library used by all clients that want to report to StatisticsService.

Simplify the implementation in each module.

- Try to reuse existing libraries eg
  - [ValueReporter-Agent](https://github.com/Cantara/Valuereporter-Agent) - run without --java\_agent directive. May be run with also.
  - [Metrics](http://metrics.dropwizard.io/)

### Usage responsibility

- Collect data specified in [StatisticsService](/web/20220817065126/https://wiki.cantara.no/display/whydah/StatisticsService "StatisticsService")
- Non-blocking behavior
- Low latency
- Low on network activity.
  - Avoid "fan-out" effect. A single request must have not more than one additional network function used for statistics.

### Performance and HealthCheck responsibility.

Recomend to reuse Dropwizard Metrics for health check and performance reporting.  
See [Metrics Spring](https://dropwizard.github.io/metrics/2.2.0/manual/spring/) for @Timed, @Gauge etc.  
We then need to create our own Reporter, based on [Metrics-Graphite](http://metrics.dropwizard.io/3.1.0/manual/graphite/)
