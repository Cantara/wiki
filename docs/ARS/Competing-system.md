# Competing system

## Problem/Context
The system to be replaced is difficult to integrate with on any level.

## Solution
Create a new system that can handle the simplest kind of new business. Grow the system over time to handle more and more types of business.

## Strengths
- Migration of some types of data is postponed and possibly reduced since the new system can operate more or less independently of the old system.
- The new system and the old system will not have to communicate.

 
## Weaknesses
- The [MRP](MRP.md) for the first release will in many cases be too large. A very aggressive approach to feature reduction in the first version must be used.
- If there are strong interdependencies between new orders and existing orders it will be difficult to achieve a real reduction in [MRP](MRP.md) with this pattern.
- There will probably be some base data that must be migrated. This pattern does not work if it is difficult to isolate what data to migrate.

## Examples
