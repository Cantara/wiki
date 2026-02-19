# New orders

## Problem/Context
In a [replacement project](replacement<sub>~project.md) or [enhancement project](enhancement</sub>~project.md) the existing system has a steady stream of new orders, requests, cases to be handled, etc (hereafter referred to as orders).

## Solution
Develop enough features in the new system to support new orders of the simplest type. Add a gateway that directs new orders of the appropriate type to the new system. This pattern can be used together with the [Synchronized database](Synchronized<sub>~database.md) or [Replicated database](Replicated</sub>~database.md) patterns in order to make base data available to the new system.

## Strengths
- Greatly reduced [MRP](MRP.md) in some situations
 
## Weaknesses
- The frequency of new orders must not be too high or too low. If the frequency is too high the [MRP](MRP.md) will become large. If new orders are rare there will be too little feedback from having the release in production.

## Examples
- An internet shop could funnel purchases that are to be invoiced to the new system while letting the existing system handle credit card purchases.

- This pattern was evaluated in the [Book club system](Book<sub>~club</sub>~system.md).
