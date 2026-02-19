# Anti-agile architecture choices

###### Proprietary communication protocols  

Proprietary protocols is costly, because you must maintain libraries for each programming language used to communicate over the protocol in addition to development and maintenance of the protocol itself. Standard protocols should thus be preferred to proprietary whenever possible. 

###### Proprietary data formats  

Custom/proprietary formats have the disadvantage of unnecessary development and maintenance cost. In addition, standard formats often has a community to ask for help and good tool support. For proprietary formats you are all on your own. 

###### Tight coupling between services 

Tight coupling between methods, classes and packages is something developers generally understand and try to avoid. The principles must be followed at the system level. Loose coupling gives better architectures than tight coupling! Tight coupling also makes it harder (and more costly) to test each application in isolation. For example often it is necessary to develop a _simulator_ or extensive _stubs_ to replace the application(s) the test subject communicates with. 

 
###### Heavyweight application servers, ESBs, etc. 

To fully automate tests we need to be able to control the test environment. Heavyweight services like application servers and ESBs are not easy to install and configure. This makes it hard (impossible?) to implement service and multi-service tests that can run on any computer. Heavyweight servers thus rely heavily on costly system tests. Further, since these servers are not created for automated control, system tests are also hard to automate. 

In other words, there is a **trade-off** between the value provided by a heavyweight server compared to a lightweight server and the added development, test and maintenance cost.
