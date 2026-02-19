# Organizational Architect

See [architecture:Laws for Organization Architects](../architecture/Laws<sub>~for</sub>~Organization-Architects.md)

and 

[EA:](../EA/.md)

###### Chief Architect and Enterprise Architect

The enterprise architect handles business-related software decisions that frequently can involve multiple software systems within an organization, spanning several projects teams, and often at more than one site. The Enterprise Architect may seldom see or interact with source code.
 Source: [Wikipedia](http://en.wikipedia.org/wiki/Chief_Software_Architect#Types_of_software_architects)

Works primarily with Enterprise Architecture (EA):
- [EA (Wikipedia)](http://en.wikipedia.org/wiki/Enterprise_Architecture) 
- [Enterprise Design and Architecture (Objectware Community Wiki)](http://wiki.community.objectware.no/display/EA/Enterprise+Design+and+Architecture)

Chief architect and enterprise architect have the same responsibilities, but chief architects are paid more. Both are evaluated in the budget process the following year. 

Enterprise Architects are also known as Systems Architects (plural). 

###### Integration architect

Integration architect - evaluated every quarter 

- Identifisere funksjonelle krav. Koden skal ikke skrives hvis den ikke kan forsvares av krav. Denne jobben må begynnes lenger før utviklinger startes for må fortsette hele tiden.

- Være veldig tydelig på ansvarsområder til forskjellige systemer. Vanlig tabbe er å la integrasjonsplatformen gjøre jobben som må egentlig gjøres andre steder.

- Identifisere dataeiere. Basis for EDA.
- Kontrakter, kontrakter, kontrakter. All kommuniksjon må baseres på kontrakter. Retningslinjer for hva skal gjøres når kontrakter brytes.

- Minimalisere koblinger mellom systemer (ikke bare mellom interne og eksterne, men også mellom interne). Være veldig forsiktig med Common Information Models.

- Øke gjenbruk av funksjonalitet. (Riktig plassering av funksjonalitet, Implementasjon må være uavhengig av kontakt, Kontrakt må være uavhengig av protokoll)

- Definere overordnet design beslutninger før kodingen starter. De kan være abstrakte (uten implementasjonsdetaljer) men presise.

        Eksempler: feilhåndtering og versjonering. Disse tingene må være konsekvente på tvers av hele prosjektetet.
- Retnigslinjer for tester. Spesielt integrasjonstester.
- Definere standarde måter å løse integrasjonsproblemer problemer på:
        Retningslinjer for MEX (melding exchange patterns) Synkron vs. asynkron, exceptions. Topics vs. queues. Når forskjellige protokoller skal brukers.

        Retningslinjer for orkestrering. F.eks: når BPEL skal bruker og når BPEL ikke skal brukers. XA transactions vs. compensations.

###### Infrastructure architect

Infrastructure architect - evaluated every quarter 

Same as [Hardware architect](http://en.wikipedia.org/wiki/Hardware_architect) ?
