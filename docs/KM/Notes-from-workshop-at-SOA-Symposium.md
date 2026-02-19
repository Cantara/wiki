# Notes from workshop at SOA Symposium

Workshop with the [SOA patterns commitee](http://www.soapatterns.org/soa_committee.asp) at the [International SOA Symposium](http://www.soasymposium.com/)

### Participants

Sheperd: Ian Robinson, [Thoughtworks](http://www.thoughtworks.com/)
Dr. Thomas Rischbeck, [ipt](www-ipt-ch.md)
Radovan Janecek, [CA](www-ca-com.md)

### First impression.
Management summary of the pattern needed. Need a selling text for the problem, and why to use the pattern.
Need to develop a more presice communiation for the pattern.
Need to tell why this is more than Master Data Management, and pure data synchronization.
Need to distinguish this "Business service" from "Data services". 

### Improvements
Describe that the view is from a businees perspective. This is a Business Object service. Distinguish the difference between EDR and a service providing data from one of the providers. Eg. a SAP Customer service.

Narrow the scope.

Split functionallity between data handling (DataMasterMgmt, DataServicePlatform, ESB) and the extra functionallity we get from EDR.

Describe that we handle different endpoints:
- soap
- rest 
- java/.net serialized object
- versioning

Must build on other patterns for communication.
- Mutiual update
- Unified Data Model
...

### Similarities worth investigating
**DataServicePlatform** - product from Aqualogic, possibly discontinued or integrated with other products.
This is now named [MetaMatrix Enterprise Data Services Platform](http://www.jboss.com/products/platforms/dataservices/), and
characterized as a Data Service.

**Business Entity Service** pr Business Object

### Naming
The current name is misleading. 
Have a look at something like:
- Business object ...
- Reconciliation 

Look to ITIL for inspiration?

### References

- [MetaMatrix EDS FAQ](http://www.jboss.com/pdf/0508_MetaMatrixFAQ.pdf)
