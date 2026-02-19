# Control state

It is possible to write tests that verify that a service work even though it has a dependency on some external environment. Integration with a database, a JMS server, reading files from file system or a remote share are typical examples of external environment. All these services have _state_. In this context we consider state to entail both configuration and test data. We will now describe how different strategies fit into the Jigzaw model. 

#### Which test data suited for different contexts? 

- Canned data (record production data and playback) 
    - Tests based on this strategy need to be run _after_ tests that verify that the functionality works as the developer intended. Otherwise time is wasted analyzing whether the overall business logic is incorrect or the code was fed unexpected input data. 

- A standard dataset shared by all or a group of tests 
    - High maintenance cost 
    - Suited for contexts with a limited (and preferably few) relevant combinations of test data. 
    - Unsuited for big/complex systems as the number of permutations which must be included in the shared dataset is too big. 

- **Each test responsible for its own test data**
    - Scales well
    - High cohesion: code, test logic and test data can be developed and modified without affecting everything else. 
    - Generally cheaper than the alternatives above. 

#### How to ensure the expected testdata? 

###### restoreDefaultState

Our first need is be _know_ what state the system is in when we start a test. Without knowing the state we cannot repeat the test, and we cannot reliably conclude on anything. We can execute queries to detect what state the system is in, but this concept rely on _controlling_ the state. We thus need functionality to restore the default state. I.e., it must be possible to call a function, {}, and be confident that when it finishes we have a known and consistent state every time. 

###### cleanDataAndHistory

Sometimes restoring the default state can be an expensive and time-consuming procedure. It is therefore convenient to have a faster version of the {} function. To make it faster we can skip restoring the datastructures and infrastructure and only delete data and history. Note that application data (f.eks. the version of the database or application) should not be removed. 

We suggest the name {} for such a function. 

###### **TODO** Describe the combination 

Unitils + dbmaintain generally use cleanDataAndHistory, but fail-over to restoreDefaultState when necessary. 

[< Back](JigZaw<sub>~Design</sub><sub>Principles</sub><sub>and</sub><sub>Drivers.md) to Design Principles and Drivers   [Next >](Tools</sub><sub>and</sub>~implementation.md) Tools and implementation
