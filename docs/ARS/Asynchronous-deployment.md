# Asynchronous deployment

## Problem/Context
When upgrading or replacing multiple systems that are interconnected. 

## Solution
Deploy upgrades/replacements to the systems at different times.

## Strengths
- Deployment can be more flexible than with [synchronous deployment](synchronous-deployment.md)
 
## Weaknesses
- A deployment sequence must be created to handle situations where parts of one system are dependent on other systems.
- Circular dependencies are difficult and must be broken into a sequence.
