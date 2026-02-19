# Security Token

### Intro

\*Gjennomgående sikkerhetstoken

### Token karakteristikk

- Data-felter, hvem, kanal, applikasjon, på vegne av, samtykke, State-info på alle i call-stacken (Kan desverre ikke bruke standard sikkerhetsprodukter, da de ikke har alle disse egenskapene)
- enveis hash for å verifisere at tokenet er konsistent
- ekstern token-verifier som verifiserer hash mot gyldige hash i et gitt tidsrom (remote kall)

### Service invocation karakteristika

- Pre-method filter
  - Token not OK, return dummy data
  - Token OK, run method
- Post-invocation filter
  - Token not OK, return dummydata
  - Token OK, Run defined filter for token - if not found, run remove-all-fields\_and\_values filter

- Full audit-logging in both filters and in service-internal security rules.
