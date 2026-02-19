# How? Eventing?

## What
Some sort of eventing from out of bounds updates that trigger the service to synchronize the underlaying data sources as a means to achieve  master data management

## When
"Real time" synchronization has to be done through core services due to validation of complex business rules implemented there. 

## How
The source system where the out of bounds update occurs fires an event which is then picked up by a listening service. The contents of the event has to contain the needed information for the core service to update the other source systems it   encapsulates. The payload contents of the event might contain: originating source system of the update, event sequence number, time stamp, pre and post versions of the changed data.   

## When Not 
When "real time" synchronization is not required
