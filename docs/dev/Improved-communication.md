# Improved communication

### Forbedret kommunikasjon
- Definere en trappemodell for hva man kommuniserer når. Det endelige målet er å bidra til best mulig økonomi for forretningen. 
- Fjerne seg fra TCO mål, rette seg mot "best mulig økonomi for forretningen, over tid".
    - Dette støtter endringsvillig funksjonalitet, og lav tco.
    - Mest mulig automatisering kan være et delmål på vegen.

### Del opp JigZaw i flere deler.
Kjerne:
1. Single responsibility principle.
1. Foretrekke billigst mulige tester.
1. Minst mulig overlapp mellom tester.

Bruke kategorisering som et verktøy for å oppnå kjernefunksjonaliteten.

Bruke de andre verktøyene i dagens JigZaw som verktøy for å nå det endelige målet

### Mål videre

- Hvordan fikse gradvis introduksjon av JigZaw i eksisterende kodebase/prosjekter/produkter.
    - Tenk i vertikaler, eksiterende kode lever ok ved siden av forbedret test-funksjonalitet.
    - Endre i vertikal når vi skal rette feil. Det samme når vi skal endre ting som begynner å bli vanskelig.
    - I forhold til "green field" så vil man ofte her foretrekke en mer top-down approach, men helst starte med tester som verifiserer at hver applikasjon fungerer i isolasjon.
