# Tjenesteversjonering

Fiks dette og publiser på public wiki - Totto 

#### Hvordan 

There can be only one 
Mangler holdning til utfordringen - struts
Tjenester dør alle. 

Løser ikke WS* dette? 

Schema, typer  

Logiske avhengigheter i mellom tjenester - semantiske endringer 

#### Hvor kommer problemet fra? 

- Vanlig dødelige utvikler begynner å fikle med distribuerte systemer 

- Vant til å bruke tid på å definere en standard. Big upfront design. 
- Problemet kom da man ikke brukte tid på å definere en skikkelig standard. 

- Man prøvde å løse _ett_ problem. ref. OWSOA tjenestemanifestet. 
    - API-størrelse: ansvar og skreddersøm 
    - Use case-definerte API-er gir versjonshelvete. 

#### Klient-tjener 

- Logikk isolert i klienten 
- Data endrer seg sjeldnere enn logikk
- Løst typede data 

#### Én mulig løsning 

Big upfront design + løs typing + gjør en ting godt 

#### Noen byggestener 

vCard som format for en person.

Jason inspirert av vCard. 

#### Mulige angrepsvektorer 

- Støtte flere versjoner - side-by-side (eBay's strategi)
    - brukes ved få klienter, ingen endringer 
    - brukes når en tjeneste som skal dø / midlertidig hack 
        - Legge inn tidsbombe - system.exit hvis mer enn 6mnd frem i tid 
    - brukes ved godt definert og god standard 
    - brukes ved Skreddersydde API - use case-orientert 1-1 (her gir WSDL mening)

- Dynamiske endepunkt 
    - svak typing - stringer - konsument bryr seg bare om de dataelementene som de har behov for. XPath, substring, tokenizer  
    - Ikke kontroll på klienter (åpent api)
    - skal endres ofte (identity/aksess management: utypet user token)
    - Infrastruktur (les: alt annet enn domene/businesstjenester)

- Tjenesten leverer fra seg klientproxyen (Jini++) / plug'n'play
    - Sterk typing i klientproxy, men svak typing mellom klientproxy og server 
    - Jini: remote classloading, får tjenesteproxy eller selve tjenesten. Distribuert hashmap for å dele tilstand. 
    - tjenester med mye tilstand (eks. FelleData sitt kassesystem) 
    - utviklere må forstå nettverk - høy kompetanseterskel 
    - høy skalerbarhet, høy robusthet, men vanskelig å få til.

- ESE - adapter tolker versjon/dialekt inn og ut. (Adapter ligger imellom endepunkt og tjeneste)
    - kan implementeres med en ESB men krever svak typing 
    - AI (f.eks. OpenCalais) kan brukes i implementasjon av adapter 
    - 

- Endringer som et nytt aggregat (Coretjeneste er låst, så bygger en ACS på toppen) 
    - der endringer ikke er en endring, men ny funksjonalitet - en slags utvidelse eller begrensning 
    - Gir ekstra remotekall 
    -
