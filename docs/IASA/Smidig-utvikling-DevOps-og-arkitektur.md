# Smidig utvikling, DevOps og arkitektur

|  | **Tema** Husker du vi snakket litt om prosessmennesker, DevOps (tools) og koblingen eller mangelen på kobling til arkitektur....? Prosessmenneskene ser CD med sine øyne.   DevOps-gjengen ser bare verktøy.   Arkitekturen er "stebarn" i begge leire.  Mange konservative arkitekter vet ikke igang hva de hvilke valg som gjør CD umulig hos seg. (uklar setning - please rephrase)  Mulige formater for å adressere dette:   - workshop? - foredrag? - annet?   Denne siden brukes til tankemyldring om og kommentarer til dette temaet og ideene som allerede er avdekket. |

# Problemstillinger

- [Smidig og arkitektur](#Smidigutvikling%2CDevOpsogarkitektur-Smidigogarkitektur)
- [DevOps og arkitektur](#Smidigutvikling%2CDevOpsogarkitektur-DevOpsogarkitektur)

- [Er kontinuerlig *produksjon* alltid målet? Eller er CD i mange tilfeller "bedre"?](#Smidigutvikling%2CDevOpsogarkitektur-Erkontinuerligproduksjonalltidm%C3%A5let%3FEllererCDimangetilfeller%22bedre%22%3F)
- [DevOps og sikkerhet](#Smidigutvikling%2CDevOpsogarkitektur-DevOpsogsikkerhet)

## Smidig og arkitektur

Med smidig-øyne er deler av utfordringen å finne måter å få arkitektur-arbeid med inn i prosessen heller enn å la den være en eksternt regulerende instans.  
I og med et ønske om organisering i tverrfaglige team er det interessant å diskutere hva dette innebærer for

- arkitekter (rolle)
- arkitektur (aktivitet)
- arkitektur (resultat)

Et ønske om at teamet skal være selvorganiserende utelukker ikke behovet for teknisk styring (les: governance), og funksjonelle kravstillere fra forr.siden kan ikke forventes å ta ansvar for at tekniske krav ivaretas.

Gir mening å vurdere om måten vi jobber på er mer eller mindre effektiv enn alternativene.  
***Spesialist* vs *generalist***

En debatt knyttet til dette er absolutt på sin plass, er det egentlig der de største problemene er begravet?  
Det er litt for vanlig å lese for mye 'generalist' inn i smidigpostulatet om **delt kodebase**, for eksempel. Og **tverrfaglig team**.  
Egentlig kan et 5-manns jazz-ensemble være en vel så god modell på et godt fungerende tverrfaglig team. Og der er det liten fare for at bassisten skal forsøke å gjøre pianoets jobb.

Kravet om tverrfaglighet innebærer at all nødvendig kompetanse skal være representert i teamet, ikke at alle i teamet skal beherske alt.  
De må bare ikke være avhengig av ekstern kompetanse for å gjøre *sin* jobb.

På bakgrunn av dette ligger det til rette for en spennende debatt om hvor arkitekter og arkitektur skal høre hjemme i en slik modell.  
Og her bør vi passe på å holde rolle og aktivitet og resultat fra hverandre (se over).

## DevOps og arkitektur

En observasjon/påstand: **CD krever smidig done right.**  
Det ekskluderer fossefall og ivory tower-arkitekter.  
Og medfører at nødvendig arkitekt og driftskompetanse må være tilgjengelig i/for teamet.

### Er kontinuerlig *produksjon* alltid målet? Eller er CD i mange tilfeller "bedre"?

Batche endringer som prodsettes eller flytte enhver endring ut i prod?   
@Erik: Sikter du her til forskjellen mellom 'continuous delivery' og 'continuous deployment'? Eller misforstår jeg spørsmålet?

### DevOps og sikkerhet

Muligens innenfor scope:  
Hvordan sikrer man at sikkerhetshensyn ivaretas tilfredsstillende i et smidig/devops-apparat?  
Et konkret eksempel er at en skremmende høy andel av docker-image i offisielle repositories har kjente sårbarheter.
