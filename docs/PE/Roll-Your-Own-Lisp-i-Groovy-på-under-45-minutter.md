# Roll Your Own Lisp, i Groovy, på under 45 minutter

## All koden er tilgjenglig her: [http://www.rollyourowncode.com/](http://www.rollyourowncode.com/)

# Lær Lisp, Groovy, og hvordan interpretere virker ... på under en skoletime.

Vi bruker forskjellige programmeringsspråk hver dag. Mange av oss er innom Java og JavaScript, 
kanskje php, eller Clojure, eller Groovy eller Ruby... og vi tar disse språkene egentlig for gitt.

Men jeg har begynt å lure på... Hvordan er de laget? Hvilke bevegelige biter har de? Hva gjør de 
forskjellige bitene? Hvordan kan jeg lage mitt eget programmeringsspråk, om jeg vil?

Den store hemmeligheten er at **dette egentlig ikke er så vanskelig**. Hvis vi bare bruker litt 
**tid** på hver bit, for seg selv, og **peprer den med tester**, forsvinner magien, og bare kode står 
igjen.

Deilig, deilig kode. 

(PS. Du trenger ikke kunne Groovy for å følge med her, jeg har valgt Groovy nettopp fordi 
konseptene blir så klare, språket står ikke i veien.) 

(PPS. Du trenger absolutt heller ikke kunne lisp. Igjen har jeg valgt språket fordi konseptene 
blir enkle å forklare.)

# Så hvorfor er det nyttig? Hvorfor skal du bruke tid på dette?
       Jo: Her er noen overfladiske grunner først:

       Hvis du noen sinne trenger å skrive kode som har med kode å gjøre. Hvis du vil lage en syntax highlighter. Eller
       hvis du trenger å formatere din gamle kode til å ha et nytt format. Eller snakke direkte med routere eller annen
       hardware som har sitt eget instruksjonssett.

       Eller hvis du trenger å behandle andre data som har en syntaks: Hvis du vil gjøre bilde-behandling, eller gjøre
       noe med naturlige språk.

       Alle disse er gode nok grunner for å lære seg om interpretere og compilere. Men alle disse grunnene er også bare
       taktiske grunner.

       La meg forklare: Hvis det eneste du ønsker deg er å være en helt-greit flink programmerer som har lønn til å
       betale regningene sine, og har råd til mat på bordet og en øl i hånda, ja da er dette kjekke nok grunner.

       Men hvis du har høyere mål enn å være Java-sertifisert, hvis du vil forstå, og leke med datamaskiner, hvis du vil
       kunne bruke dem på nye og uventede måter -- ja, hvis du vil bli en skikkelig god programmerer som har det mer
       moro, ja da MÅ du kunne dette.

       La oss tenke strategi. Som programmerere har vi evnen til å endre verden. Tenk på kontrollsystemene som må til
       for å skyte rakketter vellykket opp i verdensrommet. Tenk på Internett. Tenk på iPhone. Hvis du ønsker å strekke
       deg mot å gjøre verden til et bedre sted, så bra som du kan gjøre det med dine evner, så må du kunne det vi skal
       gå igjennom i dette foredraget.

       Når du er ferdig med dette foredraget, kan du snart ha din egen lisp oppe og gå. Du kommer til å forstå hvordan
       en interpreter virker -- du kan selv skrive alle bitene som skal til: din egen tokenizer, din egen parser, din
       egen evaluator, og du kommer til å kunne lage dine egne språk om du har lyst til det.

       Dette er grunnlaget for å kunne løse en mengde oppgaver, og det er fundamentet du trenger for å kunne trenge enda
       dypere inn i materien senere.

       **Også er det skikkelig moro.**
