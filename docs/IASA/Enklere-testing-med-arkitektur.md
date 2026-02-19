# Enklere testing med arkitektur?

- Governance 
    - Endrer aldri på en versjon av en tjeneste. Må da legge ut en ny versjon. Versjon x-1 går ut om 12mnd. 

For mye oppdeling, fler produkter, mer nettverk gir økt kompleksitet og dårligere testbarhet. 

#### Ekstremvariant 1: Siloapp 

Muligens god testbarhet, men blir fort stort og tungt. Noe så enkelt som kompileringstid blir kjipt når det tar 20min...

#### Ekstremvariant 2: SOA på syre med ufattelig antall tjenester 

Får økt kompleksitet mht. deployment, antall produkter, antall rammeverk, flere servere, osv. 

Kan teste enheter i isolasjon i større grad.
