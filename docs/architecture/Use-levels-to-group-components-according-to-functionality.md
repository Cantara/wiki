# Use levels to group components according to functionality

#### Goals 

Extend an existing, distributed system without compromising scalability with acceptable cost (time/money). The most important drivers are maintainability and reuse/cost. 

#### Context 

We have an existing distributed system where service A _uses_ a service B, which in turn uses a service C. Let service C be responsible for communicating with a certain type of hardware. We now want to add support for a new type of hardware device. The producer of this hardware device offer software to communicate with the device. 

**[Diagram: Original](../Diagram/Original.md)**

#### Strategies

We have the following options: 

1. Extend the existing services to support the new hardware 
2a. Modify B to support services C <sub>1</sub>, C <sub>2</sub>, C <sub>3</sub>...
2b. Modify A to support services B <sub>1</sub>, B <sub>2</sub>, B <sub>3</sub>...

The traditional (pre SOA?) approach is to use option 1. This might or might not be appropriate. In the case where service C is tightly coupled to a specific hardware unit, it seems natural to add more services instead of changing existing ones. The goal is better scalability and better separation of concerns. Below explains two such strategies based on option 2. 

###### System extended at level C
Let us rename service C to C <sub>1</sub> and let C <sub>2</sub>, C <sub>3</sub>, C <sub>4</sub> denote services that support new types of hardware at the same level as the original service C. This option might require some changes to service B, but service A can probably be reused as it is. This is the cheapest and probably the best option. 

**[Diagram: System](../Diagram/System.md)**

###### System extended at level B
Producers of new hardware units often sell their hardware bundled with software to use it. Reusing this 3rd party software might reduce development time, which can be enticing in terms of cost and/or time to market. "Unfortunately" the producer has written functionality that partly overlaps functionality found in our service B. 

If the 3rd part software, D <sub>1</sub>, can function as a C-level service, that might be the best approach. 

If it cannot, we are forced to let it communicate on the _B-level_. We should add a wrapper/bridge/adapter/anti-corruption layer/whatever between D <sub>1</sub> and service A, to avoid having to change service D <sub>1</sub> or changing A. It might seem logical (and easier) to change service A, but changing service A does not scale very well. So when you add support for more hardware ( D <sub>2</sub>, D <sub>3</sub>, D <sub>4</sub>...) you have created an unmaintainable blob of code. Instead we add a separate service/component to handle the differences between the interface of A and the interface of D <sub>1</sub> to separate concerns and make the system as a whole easier to maintain and test. That is, B+C are needed to allow A to communicate with hardware units of a specific type. D + some extra code is needed to add the same support to another type of hardware unit. B+C is thus analog to D + some extra code. 

 

**[Diagram: System](../Diagram/System.md)**

###### Conclusion 
When adding support for multiple "_types_" try to use abstraction to mask the diversity as early in the chain as possible. (Note that this advice is as valid within a service as between services.) The less parts of the system that needs to handle diversity the better. :)
