# New product

## Problem/Context
In a [replacement project](replacement-project.md) or [enhancement project](enhancement-project.md) where the business is regularly creating new products.

## Solution
Develop enough features in the new system to support a new product. Add a gateway that directs customers of the new product to the new system. This pattern can be used together with the [Synchronized database](Synchronized-database.md) or [Replicated database](Replicated-database.md) patterns in order to make base data available to the new system.

## Strengths
- Greatly reduced [MRP](MRP.md) if the business is willing to keep the new product simple to start with.
- Migration of some types of data is postponed and possibly reduced since the new system can operate more or less independently of the old system.
 
## Weaknesses
- If there are strong interdependencies between the new product and existing products it will be difficult to achieve a real reduction in [MRP](MRP.md) with this pattern.
- The business must be willing to launch at least one new product as soon as possible after the release.
- There will probably be some base data that must be migrated. This pattern does not work if it is difficult to isolate what data to migrate.

## Examples
- This pattern was evaluated in the [Book club system](Book-club-system.md). New book clubs would have been started in the new system.
- Writely, now Google Docs, released their first version after four weeks. Instead of implementing all the features that were essential for a word processor, they implemented only what people miss with the existing offering. Specifically, sharing, availability on the web and versioning.
- The evolution of the programming language Java is constrained by current large user base. The Scala programming language is positioning itself to become a Java 2.0. Whether it will succeed is still not clear.
