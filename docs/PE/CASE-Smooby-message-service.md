# CASE - Smooby message service

| Title | Smooby abstrakt |
| Presenter | Leif Auke |

**Smooby message service**

**Funksjon**
Sender datameldinger mellom 2 noder hvor begge noder befinner seg bak et NAT, som for eks. en mobiltelefon og en (normal) hjemmepc.  Meldingstransporten er for meldingskonsumentene online og såkalt push, dvs meldinger kan sendes og mottas forløpende.
Metoden som benyttes er såkalt longpolling via en agent med http / https. Longpolling gjør at det simuleres push med beskjeden netttrafikk. Se http://smooby.net

**Protokoll og kryptering**
Smooby har en protokoll som er basert på en ytre konvolutt med et minimum av metainformasjon mellom node og agent, og en indre konvolutt for metainformasjon mellom nodene. Den indre konvolutten inneholder en kopi av adressering, brukerinformasjon og informasjon meldingstyper og dataformater sammen med selve dataene. Informasjon i den indre konvolutten sendes ubehandlet mellom nodene. Det betyr at det er mulig å kryptere meldinger node til node.
Addresseringog meldingsdata
Adressering er er gitt med et domenebegrep og noder innenfor domenet, for eks en PC og 2 mobiler i ett felles domene. Hver node kan kommuniserer inngående og utgående med de andre noder i domenet og tjenester innenfor et domenet på en eller flere noder er adressert som servicetyper. . Datameldingene og format på disse implementeres i tjener og konsumentapplikasjonene. Det er ingen formatmessig begrensning på meldingstørrelser men typisk maks er 5-10mb avhengig av oppsettet på agenten.

**Teknologi**
.Net eller java.  Et sett av basisklasser i smooby library håndterer meldingstransport og adressering og (kommer snart) kryptering av datameldingene, og kan integrere handler objekter via et handlerinterface for ulike servicetyper.
Tjenere og konsumenter.
Konsumenter og tjenere kan utvikles på .net eller an Java, eller så langt android baserte mobiltelefoner. Planlagt neste er iphone og object  C library.
Smooby er eventdrevet og lagrer ikke meldinger i en ekstern inngående eller utgående kø, men programlogikken programmeres i handlerklasser.  Handlere kan evente på sending og mottak av request og response meldinger på ulike definerte meldingstyper og data. En typisk handler implementer en gitt service og servicen definerer et sett av meldingstyper og funksjoner.
Markedsvurdering
Se applikasjoner, men vi vurderer enten å tilby smooby.net som en fast tjeneste

**Applikasjoner**
Smooby home connect
Vi har under utvikling en tjeneste for å browse og laste ned filer mellom PC og Android telefoner.  Applikasjonen består av an App med katalogbrowser og nedlastning, og en PC tjenerservice. Funksjonen er at man på PC eksponerer en eller flere kataloger som en eller flere mobiler gies tilgang til. (ftp like)
Applikasjonen er i tidlig beta, men er planlagt ferdig og introdusert i Google appstore i løpet av september. 
Smooby ”hvor er du”
Vi planlegger en App som utnytter push teknikken i smooby og posisjonering på mobilene og som skal virke på følgende måte.
A spør på sin mobil hvor B er og B sin mobil svarer med posisjonsangivelse.  Det gjøres med en request melding ifra A til B og B en response med posisjon fra B. 
Bruksmønster. B får beskjed om at A har spurt via et notat. B kan angi oppløsningen på sin posisjon.  B kan velge å forhåndsgodkjenne spørsmål eller godkjenne hvert spørsmål for seg. 
Vi tror det kan være en typisk ”rosa” app 
