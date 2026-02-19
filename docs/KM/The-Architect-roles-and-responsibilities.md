# The Architect - roles and responsibilities - Cantara Community Wiki

|  |  |
| --- | --- |
| **Motivation:** Architecture is balance, but sometimes you need to pinpoint key issues (even if we acknowledge that your mileage will wary)  We use **Organizational Architect** to classify software architects which are responsible for the organizational context, i.e. across projects and products. These architects are commonly called *Chief Architects, Enterprise Architects, Solution Architect, System Architects, Integration Architects* or *Infrastructure Architects*.  We use **Project Architect** to classify architects who work on a specific project and *within* a project scope. These architects are commonly called *Solution architects, Software architects* or *Tech leads*.  We use **Product Architect** to classify architects who work on a specific product and *whithin* the product lifeline scope. Commonly used names for such architects are: Chief Product Architect, Product Architect, System Architect, Sub-system Architect, Build Architect or *Tech leads*. | *The Architect* from Matrix:Reloaded, picture borrowed from [davidlouisedelman.com](http://www.davidlouisedelman.com/fantasy/whatta-fiasco-glossary/) . |

|

###### Chief Architect and Enterprise Architect

> The enterprise architect handles business-related software decisions that frequently can involve multiple software systems within an organization, spanning several projects teams, and often at more than one site. The Enterprise Architect may seldom see or interact with source code.

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

Same as [Hardware architect](http://en.wikipedia.org/wiki/Hardware_architect)  ?

###### Solution Architect

Synonyms: System Architect (singular), Systems Architect (plural)

> which may refer to a person directly involved in advancing a particular business solution needing interactions between multiple applications.

Source: [Wikipedia](http://en.wikipedia.org/wiki/Software_Architect#Types_of_software_architects)

Solution architect is responsible for mapping functional requirements to technical solution. Often responsible for the domain and the business objects, which should perhaps be in the organization scope.

- - Feedback and evaluation is often missing.

###### Application architect

creates an application from the architecture drafts made by the solution architect.

###### Coordinating architect

- coordinate tech leads.
- evaluated at FAT, Sprint review, CRs
- Should *sit* close to the teams (in an open landscape?).
- Participate (as chicken) on different stand-up meetings.

###### Tech lead

- Tech-lead is evaluated daily.
  - Especially important to assign this role to *one* person in an agile team.

1. Responsibility and authority within a limited context.
2. Can and should challenge rules and policies which the team feel are wrong.
3. Developer can/should challenge the architect with controversial rules. Architect is responsible for screening these questions and take valid challenges back to the PAB.

###### Separate role for QA

- Separate Competence Manager with responsibility for QA.
  - An option to help match people and responsibility.

## TODO

PAB - [Policy Advisory Board (PAB)](/web/20090624212537/http://wiki.cantara.no/display/KM/Policy+Advisory+Board+%28PAB%29 "Policy Advisory Board (PAB)")

80% communication, 20% technical work

- Organization scope
  - Chief Architect
  - Enterprise Architect
  - Solution/system Architect
  - Integration Architect
  - Infrastructure Architect

- Project scope
  - Solution architect
  - Software architect
  - Tech lead

**Product scope**

Technical architect

#### Dimensions

- One team, across multiple teams, entire organization

- One application, one subsystem, entire system

- x % communication vs y % technical work

|  |
