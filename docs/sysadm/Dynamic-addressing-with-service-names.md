# Dynamic addressing with service names

#### Motivation: 

- http://www.dancres.org/blitzblog/2008/01/21/static-shock/ 
- Simple rollback to earlier versions of the service
- Useful to use zones (virtualisation) to reduce cost of many separate environments 

#### DNS setup 

A general introduction to how to use DNS for dynamic addressing can be found in [DNS to the rescue](http://www.dancres.org/blitzblog/2008/02/27/dns<sub>~games/). These tactics is assumed to be well</sub>~known material for most system administrators, but it can be briefly explained as 

- Use logical names to map to machine names that again map to IP addresses. Webproxy/DNS can thus be used to control which version of a service that is currently the primary source.
- Use sub-domains to denote different enclaves (physical environments) 
- Examples: 
    - serviceA.environment1.company.com -> serviceA-v123.environment1.company.com -> machineA.company.com -> 10.0.0.x
    - serviceA.environment2.company.com -> serviceA-v225.environment2.company.com -> machineBB.company.com -> 172.0.0.y

#### Webproxy extension
