# Whydah and Websockets

### Idea and background

- Noe vi bør se på hvordan vi støtter er whydah i real-time context. Les: skrive anbefaling kanskje.
 Tenker spesiellt på web-sockets/mobil-api
 push/pull

- Websocket er en TODO, helt klart.

- Websocket er ikke så vanskelig. Det blir applikasjonen som får ansvaret for å håndtere at en token er tiimet ut.
Så blir det opp til design om hvor ofte socet-producer verifiserer tokenet

### Scenarios*
- jeg er ikke helt sikker på om jeg helt skjønner use-caset, annet enn det jo er "kjekt å ha" .  blir f.eks veldig sticky-sessions med websockets :simple_smile:
- RIA's med push notification, push content
- Vi bruker websocket som kanal for å sende events fra "backend" til Javascript på klientsiden. èn websocket-kanal per nettleser.
- Jeg hadde en ide om at man autentiserte siden/funksjonen klienten skal bruke på vanlig måte og at auth-tingene dermed ikke er noe spesielt for websocket.

Det er i praksis ikke så mye som whydah skal pushe til klienter...  da whydah skal mest svare på forespørsler

- Men javascript må nok sende meg token når man oppretter websocket-forbindelsen.
    - Nei, det er backend som spør etter token, når det har fått token id.
    - Det jeg tenker på, er at en brukre autentiserer seg. Push av events starter fra provider. Når token timer ut, så skal provider tvinges til å stoppe strøm'en.
    - Ellers vi provider fortsette å sende etter at bruker har forlatt sesjonen/browseren eller til og med logget seg av. 
- jeg kan se at nede i **app-2-app** protokollen kan nyttiggjøres snetralisert koordinering av nøkkelbytter og slikt dog

### Session-heartbeat?
...fordeler og ulemper...
