# Master Changed OOB-Update Remaining Sources (McOOBURS)

### What
This strategy describes an approach to data synchronization conducted by a service that acts as a [Surrogate Master](Surrogate-Master.md) on behalf of multiple providers (data sources). The aim of this strategy is to instrument the service such that it can maintain the highest possible degree of consitency amongst the data sources.

### How
The service has the responsibility of determining the master datasource for each separate attribute of the domain object. The service utilizes the [Enterprise Domain Repository](http://wiki.community.objectware.no/display/EDR) pattern to aid construction and deconstruction of domain objects based on provider data. The [MasterPerAttribute](MasterPerAttribute.md) concept is implemented in the domain object factory. 

Given that the service has complete knowledge of the [MasterPerAttribute](MasterPerAttribute.md) setup for the domain object, it may also detect inconsistencies in the datasources. When a difference is identified on a field 

### When
The need for implementing this strategy becomes evident in scenarios involving [out-of-bounds updates](out-of-bounds-updates.md). Services that are relying on data sources that will be updated outside the control of the service need to do some extra job to fulfill their responsiblity. In this scenario the service must implement a strategy to detect changes in the underlying master data source and automatically replicate these changes to the remaining sources (slaves) on a [MasterPerAttribute](MasterPerAttribute.md) basis.

By default the mechanism is executed on Get operations. 

### Advantages
- Existing [MasterPerAttribute](MasterPerAttribute.md) logic already implemented in the service is reused
- Guaranteed consitency after service "touch" of data

### Disadvantages
- Synchronization only occurs when data passes through the service
- Temporary inconsitency if edit restrictions are not implemented on attributes in slave systems (service should be only allowed editor of slave system attributes)

### Compensation strategies for disadvantages
- [Datasource eventing](Datasource-eventing.md) is about using eventing mechanisms of the datasource to notify the service about a change. The eventing should not be more than a simple hint about what entity might have changed, and the service then uses this to query its sources in order to perform automatic synchronization as described by this strategy.
- [Datasource polling](Datasource-polling.md) is about using available service resources to traverse its data sources to look for changes. The implementation is simply a sequential traversing of the data which applies the same synchronization mechanisms that are used on regular gets.
