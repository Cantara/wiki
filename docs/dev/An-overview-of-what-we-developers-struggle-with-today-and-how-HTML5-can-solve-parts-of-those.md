# An overview of what we developers struggle with today and how HTML5 can solve parts of those.

I et input interface vi har i dag endel utfordringer vi i dag kan begynne å håndtere på en skikkelig måte.

La oss ta et enkelt eksempel som et blog interface f.eks. journalister jobber i. Tenk deg følgende:

- Journalisten sitter å skriver en halvtimes tid uten å lagre i et blog interface. Han går bort til en annen side og den siden får journalistens browser til å krasje. Alt han da har skrevet er da mistet. Dette kan vi nå f.eks. løse med å introdusere local storage funksjoner som lagrer på gitt intervaller i browseren.

- I samme input interfacet har vi i dag også  mulighet for å laste opp filer. I dag er det å laste opp filer en tidskonsumerende prosess der man må velge en og en fil i et input felt. Lager journalisten da f.eks. en bildeserie på 30+ bilder er dette en ting som spiser tid. Med Drag and Drop API'et og File API'et er det nå mulig å lage funksjoner slik at journalisten kan dra x antall filer direkte fra desktop'en og inn i browseren.

- I et input interface har vi også ønsker om å kunne presentere forskjellige inputfelter. F.eks i et blog interface vil man kanskje ha en "date picker" for å sette publiserings dato. I dag må en utvikler bruke ganske mye tid og resurser på å implementere dette via JavaScript. I HTML5 har vi nå fått en ny andel med nye typer, som f.eks en date picker. Vi har også fått native form validering i browseren. Dette sparer oss for mye implementering.

I et slikt type input interface er det mange slike ting som kan gjør hverdagen enklere både for journalist og utvikler.
