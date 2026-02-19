# Umbrella

## Problem/Context
A [replacement project](replacement<sub>~project.md) or [enhancement project](enhancement</sub>~project.md) where the old and new system will coexist. The goal is to avoid confusing users as to which system they should use.

## Solution
Create a layer that provides a unified view of the two systems. Users will in the ideal case not be aware that there are different systems. Route the user to the correct system based on some aspect of the user.

## Strengths
- Users do not have to keep track of which system they should use.
 
## Weaknesses
- This pattern does not work well if the user often needs to switch between systems. Loss of context will become noticeable.

## Examples
- In an insurance system the new system could handle one type of insurance. The umbrella collects enough information from a potential customer so that it can decide which system to route the customer to.
