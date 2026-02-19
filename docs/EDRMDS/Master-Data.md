# Master Data

|  | Data is really your revenue... Do you treat is as such? |

### Data strategies - Data mastering in 2008]

Today, we are experiencing a huge battle for the ownership of your enterprise data between huge IT platforms

- Data Warehouse/Business Intelligence platforms
- Enterprise Search platforms
- Service Oriented Architecture/SOA platforms

On top of this, the "new kid on the block" arrives as the much over-hyped MDS platforms..

### Definitions

#### Master data should not contain:

- Parent-child relationships
- Degenerate dimensional information
- Junk
- Data that is unrelated or weakly related to the business key.
- multi-part business keys that represent relationships in the **business** world.

#### Master data structures should contain:

- The business key, the whole business key and nothing but the business key.
- In addition to the business key, all descriptive data about the business key (to provide the business key current context)
- 1 to 1 relationship with a surrogate generated number to the business key.
- Load date, create date, last updated date, original record source, updated record source
