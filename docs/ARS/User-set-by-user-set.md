# User set by user set

## Problem/Context
The system has multiple user sets that require different sets of features.

## Solution
Create enough features in a release to support the essential requirements of one user set. Migrate that set of users first. This pattern is closely related to the [Limited releases](Limited-releases.md) principle. 

## Strengths
- By limiting the number of users that are exposed to a release the advantages of a [limited release](limited-release.md) are achieved.
- If there is a large variation in features that are needed for different user sets this pattern reduces [MRP](MRP.md) significantly
 
## Weaknesses
- This pattern does not work well if there are strong interdependencies between user sets.
- If users that have been migrated gain significant advantages over the rest this strategy can cause discontent

## Examples
- In an administrative application one release could be focused on the needs of customer support. The release would only contain features that allowed customer support to do look ups of customer data.
