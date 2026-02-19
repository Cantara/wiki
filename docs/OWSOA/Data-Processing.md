# Data Processing

## Systembeskrivelse

En gang per døgn produseres det store mengder data. Disse dataene hentes fra en JMS-Queue og skal *valideres* og *persisteres*. Deretter (en eller annen gang i fremtiden) så kan det komme en forespørsel etter data. Denne forespørselen er kundespesifikk, så det er naturlig med en form for et *kundeadapter* som transformerer data fra et fellesformat og til det formatet som kunden etterspør.

På alle "lag/nivåer" skaleres det i bredden, slik at det som regel vil være mer enn en produsent og mer enn en konsument av data.

Det er *ikke* kritisk om enkelte verdier forsvinner, siden man kan hente inn igjen denne verdien neste natt. Dvs. man prøver ikke å korrigere verdier som ikke validerer, disse verdiene bare kastes. Det betyr at hvis en verdi/jobb lagt på JMS kø ikke blir persistert korrekt, så er ikke dette krise, så lenge dette bare gjelder et lite antall.

## Beskrivelse i hht. kategoriseringsmodell
