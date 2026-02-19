# Scalability and HA requirements for distributed systems

1. Read [Fallacies of distributed computing](http://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)
2. Read [Fallacies of distributed computing](http://en.wikipedia.org/wiki/Fallacies_of_distributed_computing) again!
3. Guaranteed delivery is difficult.
   1. Handle duplicates and use [*at least once semantics*](/web/20220702163635/https://wiki.cantara.no/display/architecture/At-least+once+semantics "At-least once semantics").
4. XA don't work.
   1. Build for at-least once semantics.
   2. Use retry and support duplicates instead of transactions to handle consistency requirements.
5. High Availability is mandatory for all services.
6. Automated deployment and upgrades is mandatory for all services.
7. Optimize for writing, handle read performance with caching.
8. Persistence is expensive. Optimize for it early.
   1. Disks are slow.
      1. Optimize number of I/O operations.
   2. When disks become too slow, consider technology which can guarantee not to loose data without persisting to disk.
      1. Coherence,
9. Latency requirements will probably vary for different services. Design for it!
10. Reduce coupling between services by defaulting to asynchronous integration.
11. There will be many consumers of the data.
12. Data will be needed in different forms.
13. Polyglot persistence
    1. Not only SQL!
14. Duplicating data is (usually not a problem)
    1. Consumers can get their own copy
    2. Especially relevant to duplicate data if consumers have separate [bounded context](http://martinfowler.com/bliki/BoundedContext.html).
15. Producer, especially hardware sensors (or hardware systems) *will* behave badly!
