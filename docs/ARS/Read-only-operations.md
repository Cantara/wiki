# Read only operations

## Problem/Context
The system is mission critical, and integrity errors are unacceptable; the size of the MRP is too large. 

## Solution
Implement read-only functionality first. Ensure that the new system is technically unable to change the data by using a copy of the real data or read only access.

## Strengths
- Will allow for a release even in a project where security/safety is a prime concern. 
- Will give users a feel of the new system.
 
## Weaknesses
- Degrades value of the new release in some cases. 
- May push architectural prejudices in a wrong direction - towards data warehouse (which is important, but not what this project should do!). 

## Examples
