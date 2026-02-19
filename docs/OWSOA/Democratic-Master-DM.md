# Democratic Master (DM)

# What
Choosing one truth for a domain entity when multiple providers hold their own version of the entity. E.g. CRM, Billing ++ (providers) holds different values for customer (domain entity) address. How to achieve consensus on the correct address across all providers?

# How
The Democratic Master (DM) strategy involves all providers voting that their own domain entity is correct. The DM collects votes and chooses the winner.  The winner is the domain entity version that got the most votes.

## FUQ
- When to check if democratic voting should occur on a domain entity?
    - Create?
    - Read?
    - Update?
    - Delete?
    - Others?
- Which providers have suffrage?
- How to handle a tie? 
    - Combine other strategies with CoR?
        - [Master Changed OOB-Update Remaining Sources (McOOBURS)](Master-Changed-OOB-Update-Remaining-Sources-McOOBURS.md) ?
        - [Last Attribute Update Wins (LAUW)](Last-Attribute-Update-Wins-LAUW.md)?
    - Last option is to perform manual data washing.

# When
DM could be used when the enterprise architecture does not have a distinct master.

# Advantages
- DM is fairly simple to implement.

Possible use (not valid):
- Median values of competitors to price own products.

**No good advantages (usages) found.**

# Disadvantages
- Failure to achieve consensus may be high due to ties. Depends on the number of providers.
- Results in at least n service invokations given n providers.
- Responds slow to changes.
- Cannot write back to providers.
