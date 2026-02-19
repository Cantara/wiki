# Tag data

## Problem/Context
A release of a new system is going to write information into the legacy system database. The nature of the legacy system makes it unfeasible to completely validate that the new release will not corrupt data. 

## Solution
Add a tag that makes it possible to identify records that have been modified by the new system. This will make error recovery much easier.

## Strengths
- Easy to implement
 
## Weaknesses
- This pattern will only help if the number of records that are modified by the new system is reasonably small.
