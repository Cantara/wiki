# Top-3 list of problems an enterprise architect generates - Cantara Community Wiki

#### 1. N-layers of indirection and generic objects

- Generic objects
  - How often is not the customer object almost identical to the product object?
    - Too generic
    - Too big
    - Does not help
    - Pushes the complexity from the architecture to every usage of the object
    - Customer object is not common, but has different features and data in different contexts... this should come from the enterprise architect, not the generic property-value customer object or the 10+ pages ER-diagram of a Customer object...

- - [Simplicity before generality, use before reuse](http://97-things.near-time.net/wiki/Simplicity%20before%20generality,%20use%20before%20reuse) by Kevlin Henney

#### 2. Enterprise DNA and magic boxes

Enterprise DNA - coupling between systems of legacy reasons. Magic boxes is the "solution". I.e. encapsulate the spaghetti in box (ESB).

#### 3. Project complexity in integration, deployment and processes

- systems, boxes and processes tend to grow until nobody even dare to challenge them.. The idea of control. Forces the project to deliver huge sets of (non-working) features. 3 months+ deployment time...

#### 4. "Application hell"

- The idea of standard systems and the idea of quick-wins.
- Violates Tottos axiom
  - [Clear and consistent responsibility powers all great architectures](http://wiki.community.objectware.no/display/OWSOA/Clear+and+consistent+responsibility+powers+all+great+architectures)
