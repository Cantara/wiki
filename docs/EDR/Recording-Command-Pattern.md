# Recording Command Pattern

### Problem

~~Most enterprises have several systems which own parts of a domain object. These domain object parts are usually both disjoint and the data quality/SLA is of varied quality. We need a standarized way to handle multi-source domain objects, and to extend the Domain reposotory to handle the real-world CRUD of todays enterprises.~~

### Context

~~The exposure of services that provide an Enterprise Domain Repository usually form the Core Services in an architecture based on the Service Categorization model. This pattern should be applied to establish maintainable Core Services which can support multiple providers of data for domain-object construction. The Domain Objects exposed usually map to core business terminology such as:~~

### Forces

- ~~Business definition of a Domain Object requires data from disparate systems~~

### Solution

[excerpt}The Recording Gateway Pattern provides recording and playback of traffic through a service.[excerpt}

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unable to render embedded object: File (unknown.gif) not found. | | Element | Responsibility | Details | | --- | --- | --- | | OperationFactory | Produce the Operation with the appropriate gateway | Inserts Recording-, or PlaybackGateway if needed. | | Operation | The operation to record | Is constructed by a factory and inserted with a Gateway | | OperationGateway |  |  | | RecordingGateway | Extends the OperationGateway |  | | PlaybackGateway | Extends the OperationGateway |  | | Recorder | Persistence mechanism for the gateways | Exposes Record() and Play() operations | |

### Resulting Context

When enabled in record mode the Recording Gateway persists all operations and responses to a store to enable offline playback for identical requests later on.

### Rationale

### Extensions / Advanced Scenarios
