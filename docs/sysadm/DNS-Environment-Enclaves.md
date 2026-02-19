# DNS Environment Enclaves

### Introduction

When the number of environments grow, the need for more elaborate addressing schemes arise. This tactic describes how DNS can be used to support implement a logical "grouping" called _enclaves_. The primary purpose of this tactic is to improve communication. A secondary effect is simplified system administration, as the DNS names used by users are not directly coupled to the IP address. 

### How 

DNS enclaves can be used to model multiple dimensions. Relevant dimensions can vary, but the following can be used as a basis for discussion: 

- **Group** - who needs access to the environment 
- **Function** / usage - what types if usage is the environment intended for 
- **Location** - where is the environment located 

The DNS enclave tactic can theoretically support any number of dimensions, but we recommend that multiple _levels_ is used when number of dimensions is more than two. For example, prefer  

app1.systemX.production.company.com **CNAME** hostname1.locationA.company.com
hostname1.locationA.company.com -> IP 

instead of 

app1.systemX.production.company.com **CNAME** hostname1.company.com
hostname1.company.com -> IP 

This recommendation is based on the assumption that only system administrators are interested in physical location, while developers, testers, managers, etc. really don't care where a service is located as long as it performs as expected. 

See also: [Dynamic addressing with service names](Dynamic-addressing-with-service-names.md) or/and webproxy + [Virtualization](Virtualization.md) (OS level or para) 

The figure is a simplified view of the concept. 

**Diagram: dns.enclaves**

### List records in a domain

[DNS Zone transfer](http://en.wikipedia.org/wiki/DNS_zone_transfer) can be used to list all records in a DNS zone. This is not an ideal soluation, but it is the only one available. 

Assume bind DNS server. 

1. In /etc/bind/named.conf setup allow-transfer for the host that will perform the lookup.
1. Ask for the entire zone `dig AXFR company.com @dns1.company.com` from a host where transfer is allowed.
