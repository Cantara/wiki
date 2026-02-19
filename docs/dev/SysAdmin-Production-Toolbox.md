# SysAdmin Production Toolbox

Probably a good idea to create a (web) portal to have one central point of access to these tools. 

- End-to-end "_shallow ping_" through the system, _service_ _level_ 

- Front end for centralized [Logging](Logging.md) 

- [Monitoring](Monitoring.md) of the system and services 
    - Monitoring the workflow/value chain is often a good idea 

- Client for [ConfigService](ConfigService.md) 

- Metrics and reports (BI?) 

- Management tools for the applications and hardware. 

- JMX

#### JMS

- check that all topics and queues exist and that add/remove messages work. 

- Performance 
    - throughput (Object and TextMessage) 
    - is the sending or the receiving the bottleneck?  

- Cleanup
    - purge a Queue/Topic 
    - purge _all_ Queues/Topics

- Information 
    - supported transport protocols 
    - is messages persisted? 
    - number of sessions 
    - number of consumers per Destination 
    - Min, max and average values for each Destination
