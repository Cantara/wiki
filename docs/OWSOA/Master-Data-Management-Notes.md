# Master Data Management Notes

# Mastering Strategies

Initial discussions identified some core concepts related to mastering strategies. These concepts requires definitions in this context:

- Master
- Synchronization
- Mapping
- Complex Validation

All mastering strategies are primarily focused towards categorized [Core Services](http://wiki.community.objectware.no/display/OWSOA/CS) implementing [Enterprise Domain Repository](http://wiki.community.objectware.no/display/EDR) and utilizing multiple providers.

## Problem

|  | **From CIO "Demystifying Master Data Management"** *Unfortunately, most companies don't have a precise view about their customers, products, suppliers, inventory or even employees. Whenever companies add new enterprise applications to "manage" data, they unwittingly contribute to an overall confusion about a corporation's overall view of the enterprise. As a result, the concept of master data management (MDM)~~-~~**creating a single, unified view of an organization{-}*--is growing in importance.  [Read more..](http://www.cio.com/article/106811/Demystifying_Master_Data_Management) |

|  | **From MSDN "The What, Why, and How of Master Data Management"** *Here is a typical master-data horror story: A credit-card customer moves from 2847 North 9th St. to 1001 11th St. North. The customer changed his billing address immediately, but did not receive a bill for several months. One day, the customer received a threatening phone call from the credit-card billing department, asking why the bill has not been paid. The customer verifies that they have the new address, and the billing department verifies that the address on file is 1001 11th St. N. The customer asks for a copy of the bill, to settle the account. After two more weeks without a bill, the customer calls back and finds the account has been turned over to a collection agency. This time, they find out that even though the address in the file was 1001 11th St. N, the billing address is 101 11th St. N. After a bunch of phone calls and letters between lawyers, the bill finally gets resolved and the credit-card company has lost a customer for life. In this case, the master copy of the data was accurate, but another copy of it was flawed. Master data must be both correct and consistent.*  [Read more..](http://msdn2.microsoft.com/en-us/library/bb190163.aspx) |

## Related reading

[Solving the SOA Data Dilemma with Master Data Services](http://www.b-eye-network.com/print/6034)  
[Master\_Data\_Management at wikipedia](http://en.wikipedia.org/wiki/Master_Data_Management)  
[Master Data Management Meets SOA](http://soa.sys-con.com/read/366853.htm)  
[MDS](http://objectsecurity-mds.blogspot.com/)

## Vendor Software and approach

This section describes the various vendors approach and sales pitch within this topic area.

### Microsoft

[Microsoft buys into master data management](http://www.zdnet.com.au/news/software/soa/Microsoft-buys-into-master-data-management/0,130061733,339278352,00.htm)  
[The What, Why, and How of Master Data Management on MSDN](http://msdn2.microsoft.com/en-us/library/bb190163.aspx)  
[Stratature (bought by Microsoft)](http://www.stratature.com/)

### Oracle

|  | Exception:  oracle.mds.config.MDSConfigurationException: MDS-01333: Element "mds-config" ontbreekt.  at oracle.mds.config.MDSConfig.<init>(MDSConfig.java:563) |

[Oracle about MDM](http://www.oracle.com/master-data-management/index.html)

### Tibco

## Terms & Concepts

### Mapping

Mapping is about moving data from one or many provider object(s) into domain objects and vice verse.

- [Traditional Single System Master](/web/20210127055824/https://wiki.cantara.no/display/OWSOA/Traditional+Single+System+Master "Traditional Single System Master")
- [EDR Simple Master Mapping](/web/20210127055824/https://wiki.cantara.no/display/OWSOA/EDR+Simple+Master+Mapping "EDR Simple Master Mapping")  
  ([MasterPerAttribute](/web/20210127055824/https://wiki.cantara.no/display/OWSOA/MasterPerAttribute "MasterPerAttribute") concept)

### Synchronization

[Synchronization](/web/20210127055824/https://wiki.cantara.no/display/OWSOA/Synchronization "Synchronization") is about keeping data in sync across core systems.

- [Last Attribute Update Wins (LAUW)](/web/20210127055824/https://wiki.cantara.no/display/OWSOA/Last+Attribute+Update+Wins+%28LAUW%29 "Last Attribute Update Wins (LAUW)")
- [Master Changed OOB-Update Remaining Sources (McOOBURS)](/web/20210127055824/https://wiki.cantara.no/display/OWSOA/Master+Changed+OOB-Update+Remaining+Sources+%28McOOBURS%29 "Master Changed OOB-Update Remaining Sources (McOOBURS)")
- [Democratic Master (DM)](/web/20210127055824/https://wiki.cantara.no/display/OWSOA/Democratic+Master+%28DM%29 "Democratic Master (DM)")
- [Human Consensus Master (HCM)]
- [Voting Master (VM)]
- [How? Eventing?](/web/20210127055824/https://wiki.cantara.no/pages/viewpage.action?pageId=8487023 "How? Eventing?")

### Matrise

| Complexity / Scalability | Minimal | Normal | Høy |
| --- | --- | --- | --- |
| Lav |  | EdrSimpleMasterMapper |  |
| Middels | ETL Sync | MasterChanged |  |
| Høy | LastUpdateWins, Democratic |  |  |

## Some potential MDM related patterns

**NewGuyOnTheBlock**  
New system is introduced and is assigned responsibility as master. Example: Collab migrations Lotus -> Microsoft.

**BiggestLegacy**  
The least evolvable, biggest, baddest system is assigned master responsibilty because any other options make architects piss their pants.

[SurrogateMaster](/web/20210127055824/https://wiki.cantara.no/display/OWSOA/SurrogateMaster "SurrogateMaster")
