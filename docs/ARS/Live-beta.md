# Live beta

## Problem/Context
The system being built cannot be completed within a reasonable timeframe

## Solution
Let old and new systems live side-by-side which supporting the same workflows. New functionality is implemented in the new system, while the old system is used for other functionality

## Strengths
- Allows smaller releases
- Provides an alternative if the new solution doesn't perform as expected.
- The old system can serve as a fallback solution if a release doesn't perform sufficiently
 
## Weaknesses
- Limitations and the current structure of the existing system will constrain the new system. For example, only very limited changes can be made to the database.
- Users may be forced to work with both systems, which can be a net loss in usability.

## How
- Find isolated areas of the system
- Find isolated or new users
- Simplify by letting the new system be a gateway into the old system. For example, by implementing a better customer search functionality in the new system and letting the user open the selected customer in the old system, the new system may realize some value to many users.
