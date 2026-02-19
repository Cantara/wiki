# Architectural building blocks

## Building blocks

Vi trenger å finner en granularitert abstraksjonsnivå.

Vi trenger også å vite hvem er mottaker (hvem som skal bruker det).

some possible dimmensions
- Teknisk
- Løsning
- Forretning

Vi ønsker å lager en abstraksjon som lingner på det vi skal skaper. Slik at vi
kan resonere og finner feil i domene via abstraksjonen og finne at dette også er
sant i systemet vi skal lager.

Før vi kan skape en abstraksjon av et kunderegister, trenger vi og være enig om
definisjon av en kunde.

En kunde kan være en av
- personkunde
- bedriftkunde
- organisasjonkunde

To make the point that everything is an entitiy gives no real value as a
building block, almost as much value as stating that everying in java inherits
from java.lang.Object.

## Session Two

![architectural](../images/gliffy/2064427-architectural-building-blocks-from-organsation.png)

It's important to create a mapping from high level business models to software building blocks.

Breaking down the semantic information model into the domain objects and again down into context specific domain objects and repositories you can see the dependencies an object has in the all the different contexts and use this to
- perform change impact analysis
- identify objects with high value
- measure the value each individual building block provides to the organisation for prioritisation

### Dictionary

| Term | Definition |
| --- | --- |
| System Map |  |
| Process model |  |
| Activities | High level activities that can be combined to implement a process model |
| Activity Services | Small discrete activities that can be combined to achieve a greater task |
| Semantic information model | Data model within the context of a business process |
| Logic domain model |  |
| Domain objects |  |
| Context specific domain objects | Domain objects that are tailored specific to the specific building block |

### Example - Banking system

To fully understand the concepts we started working through some examples from the context of a bank.

#### Process - Sell Loan

This process covers the case of an employee in a bank actively selling a loan to a customer (i.e. the customer did not come to the bank looking for a loan the sales person is making the first move.

Activities
- ...

## Reference
- [Understand The Business Domain](http://97-things.near-time.net/wiki/Understand%20The%20Business%20Domain)
