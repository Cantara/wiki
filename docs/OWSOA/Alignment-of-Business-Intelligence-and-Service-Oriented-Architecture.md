# Alignment of Business Intelligence and Service Oriented Architecture

## Intro to Business Intelligence

[Slides from Trond Brande about Data warehouse BI from Microsoft](http://wiki.objectware.no/download/attachments/1015847/Microsoftbasert_Datavarehus_BI.ppt)

|  | The **battle** for control of the enterprise **Entity/BusinessObject/Dimension** |

## Today's BI alternatives

Nowadays, we have to distinct approaches to BI. The traditional BI/DW strategy and the *real-time* BI strategy from the enterprise search platforms. The BI/DW approach is the dominant in today`s market, but the enterprise search approach has gained momentum the last few years.

| Technology | Strengths | Weaknesses |
| --- | --- | --- |
| [Data Warehouse (DW) and Business Intelligence (BI)](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Data+Warehouse+%28DW%29+and+Business+Intelligence+%28BI%29 "Data Warehouse (DW) and Business Intelligence (BI)") | Tools, skill-set in the markets, analytical tools | Batch-oriented, anti-agile, **not real time** , **ability to include non-structured data** |
| [Search-driven Business Intelligence](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Search-driven+Business+Intelligence "Search-driven Business Intelligence") | Real-time, non-structured data | analytical tools, skill set in the market |

## Common perspectives

[Data Warehouse (DW) and Business Intelligence (BI)](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Data+Warehouse+%28DW%29+and+Business+Intelligence+%28BI%29 "Data Warehouse (DW) and Business Intelligence (BI)") and [Search-driven Business Intelligence](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Search-driven+Business+Intelligence "Search-driven Business Intelligence") is real-only focused solution areas. If we add an Master Data Service strategy, we have the complete lifecycle of data covered in our architecture.

## Case

- [Mini-Case - Analysis of email traffic - Data warehouse or enterprise search platform?](/web/20201205184401/https://wiki.cantara.no/pages/viewpage.action?pageId=8486949 "Mini-Case - Analysis of email traffic - Data warehouse or enterprise search platform?")
- [Case - Return Of Investment of a company internal strategic knowledge initiative](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Case+-+Return+Of+Investment+of+a+company+internal+strategic+knowledge+initiative "Case - Return Of Investment of a company internal strategic knowledge initiative")

## Technical responsibilities and patterns

### Architectural responsibility considerations

**The wedding [Data Warehouse (DW) and Business Intelligence (BI)](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Data+Warehouse+%28DW%29+and+Business+Intelligence+%28BI%29 "Data Warehouse (DW) and Business Intelligence (BI)") and [Search-driven Business Intelligence](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Search-driven+Business+Intelligence "Search-driven Business Intelligence")**

**The wedding OW SOA, [Data Warehouse (DW) and Business Intelligence (BI)](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Data+Warehouse+%28DW%29+and+Business+Intelligence+%28BI%29 "Data Warehouse (DW) and Business Intelligence (BI)") and [Search-driven Business Intelligence](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Search-driven+Business+Intelligence "Search-driven Business Intelligence")**

### Patterns

- BI CSV provider
- Domain Object Change receiver

## Conclusions

We have drafted some [Example solutions combining Service-Oriented Architectrure, Business Inteligence and Enterprise Search Platforms](/web/20201205184401/https://wiki.cantara.no/display/OWSOA/Example+solutions+combining+Service-Oriented+Architectrure%2C+Business+Inteligence+and+Enterprise+Search+Platforms "Example solutions combining Service-Oriented Architectrure, Business Inteligence and Enterprise Search Platforms") to describe the responsibility and roles to the different parts of the architecture, and how they relate and collaborate to each oither.
