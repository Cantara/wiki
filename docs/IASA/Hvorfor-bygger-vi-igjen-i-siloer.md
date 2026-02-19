# Hvorfor bygger vi igjen i siloer?

Vi opplever nå igjen en stor interesse for å samkjøre utvikling og forvaltning av løsninger for å redusere kompleksitet og dermed kostnader forbundet med dette. Det er vel dette vi ofte kaller arkitekturarbeid...
 
Det interessante er at mange IT-sentriske virksomheter var igjennom dette på 90-tallet (ca. midt på...) og etablerte sentral og standardisert middleware for å tilgjengeliggjøre fagsystemer mot bruker-fokuserte klient-plattformer. Dette skapte gode resultater i form av raskere og forutsigbar fremdrift på utvikling av nye løsninger på nye klienter. Endringen var motivert av at de taktiske utviklingsløpene for å få til brukervennlige løsninger ble for kostbare og tidkrevende å få inn når en skulle løse integrasjon mot fagsystemer i hvert prosjekt. På den tiden var det også aksept for å gjøre sentrale investeringer som tok 1-2 år å realisere.
 
Med internett-bølgen (.com bølgen) på slutten av 90-tallet/start på 2000 ble dette fokuset redusert i takt med at nye internett-baserte løsninger utviklet seg. Disse dro nytte av den etablerte middlewaren samtidig som det ble utviklet avanserte og ressurskrevende fagsystemer i tillegg, og samtidig som man også knyttet seg direkte til nye fagsystemer; interne og eksterne. Det ble mao. akseptert å bygge siloer igjen, og det er på mange måter resultatet av det mange virksomheter erfarer i dag - samtidig som det er liten villighet til å gjøre tilsvarende satsning idag som man gjorde for 12-15 år siden.
 
Hvorfor er det slik? Er det blitt akseptert å bygge i siloer igjen, eller er det andre forhold? Hva kan vi tilfelle gjøre med det?
 
Årsaken er sannsynligvis sammensatt. Her er noen forhold som kan tas i betraktning:

- Svært få (om noen) evner å se helheten i IT-systemene lenger. Sannsynligvis derfor det er så stor interesse for virksomhetsarkitektur for tiden - for å klare å få et slikt perspektiv 
- I praksis svært stor fokus på enkelt-løsninger og de resultater som de skapes av de framfor virksomheten som helhet 
- Prosjekter måles på levering av løsningen og i svært liten grad (om noen) på kompleksitet og kostnader med forvaltning (herunder evne til å knytte seg til andre systemer) 
- Liten vilje, evne eller muligheter for å gjøre investeringer på tvers av funksjonelle eller tekniske områder i en virksomhet 
- IT-organisasjonene er ofte organisert langs tekniske dimensjoner som har utviklet et sett med løsninger - noe som skaper fokus kun på kompleksiten i løsningen i seg selv og ikke i helheten 
- Stor fokus på raske leveranser går ofte på bekostning av koordinering og samkjøring

Mange jobber aktivt mot å komme tilbake til felles IT-løsninger ( a la middleware ) igjen, men opplever at dette er svært tungt, og at det er vanskelig å få med seg hele organisasjon, samt det å få finansiert en slik satsning. En skal også være obs på at stor grad av samkjøring og koordinering i de fleste tilfeller vil hemme fremdrift på en måte som for mange prosjekter ikke er akseptabelt. 

Det kan følgelig være svært aktuelt å vurdere en "gyllen middelvei" for å få til en kombinasjon av ofte motstridende mål: styring mot bruk av fellesressurser og raske leveranser. Forslaget til en slik "gyllen middelvei" går på å gruppere domenemessig like løsninger sammen og etablere en infrastruktur som lar slike grupper av systemer effektivt kommunisere med hverandre. Denne retningen er motivert av at en slik gruppe av systemer kan ha behov for å kommunisere effektivt tett sammen og at det for de tilfeller aksepteres tette koplinger, mens de sporadisk kommuniserer med andre grupperinger av løsninger gjennom løse koplinger der det er nødvendig. En slik tilnærming vil bidra til å redusere kompleksitet i samhandling med andre systemer og sikre fokus innenfor sin gruppe av løsninger og gjøre det mulig å optimalisere IT-arkitekturen opp mot behovene til aktuelt domene. Denne tilnærmingen har mye til felles med domene-drevet design som er en utviklingsmetode med eksplisitt fokus på gode domenemodeller.
Det er mange forhold som taler for at en slik retning kan fungere:
- Stor interesse for domene-drevet design blant dagens utviklere 
- SOA-fokus og EDA konsepter støtter opp om tydelig og effektiv kommunikasjon mellom domener. Teknologi som er iferd med å etablere seg gjør dette enda mer effektivt og attraktivt (pub/sub teknikker f.eks.)
- Bidrar til å skape fokus innenfor et domene - uavhengig av teknologi 
- Høy liming (high cohesion) innenfor domenet for å håndtere det mest mulig effektivt, løs kopling mellom domener slik at de kan fungere uavhengig av hverandre 
- Sunn balanse mellom høy produktivitet og gjenbruk av ressurser som effektivt kan gjenbrukes 
- Domenegruppene kan organiseres til å være kompetansemessig komplette - en lager løsningene tvers igjennom innenfor domenegruppen 
- For de fleste virksomheter kan en slik retning realiseres med små og enkle organisasjonsmessige justeringer (langs domener) - og dermed er sannsynligheten større for at en kan realisere IT-arkitekturen på den måten
