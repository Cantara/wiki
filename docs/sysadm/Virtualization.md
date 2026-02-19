# Virtualization

#### Why virtualization 

The [DNS/webproxy tactics](Dynamic<sub>~addressing</sub><sub>with</sub><sub>service</sub>~names.md)  does not require virtualization and can just as well be applied to multiple physical machines. However, physical machines cost money and the physical machine approach will limit the number of concurrent environments. A virtualized approach can support a lot more environments than physical machines for the same amount of money. 

#### What kind of virtualization? 
[Full virtualization](http://en.wikipedia.org/wiki/Platform_virtualization#Full_virtualization) (e.g. [VMware](http://www.vmware.com/products/server/features.html) that supports different OSs) will save a lot of money, but [operating system<sub>~level virtualization](http://en.wikipedia.org/wiki/Platform_virtualization#Operating_system</sub>~level_virtualization) approaches (e.g. [Solaris zones](http://www.solarisinternals.com/wiki/index.php/Zones)) are recommended due to much lower resource requirements. 

#### Other advantages 

- This approach makes roll-back more feasible, as it is easy (and cheap) to implement the new version of a service in a separate environment. 
- Since it is cheap to hang on to the older versions of a service, we can allow the old service to live for a while just in case we find a problem with the new service. We can then easily switch back to the old version of the service. 
- Implementing hand-over policies can be easier affordable 

#### Concepts based on virtualization
