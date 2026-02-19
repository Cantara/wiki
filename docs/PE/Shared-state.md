# Shared state

### Komponenten bruker distr.cache i back. Alle deler alt. (Shuffle state)

Stateful \-> Session i cache orget av samme tjenester
|  | Integration | Versioning | Gjenbruk | Scale |
| --- | --- | --- | --- | --- |
| Distribuert cache | 0 | 0 | 1 | 8 |
| Publish subscribe | 7 | 3 | 5 | 6 |
| RMI | 6 | 0 | 3 | 5 |
