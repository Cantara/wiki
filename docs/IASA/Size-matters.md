# Size matters

|  |  |
| --- | --- |
| Tittel | Why size matters? Det ER størrelsen det kommer an på! |
| Foredragsholder | Hein Kristiansen (og Erik Drolshammer?) |
| Tid og sted | 15. juni kl17:00 @ Teknologihuset 3.etg |
| Format | Presentasjon, 45 eller 60min? |
| Forventet publikum | Utviklere, tekniske arkitekter |
| Stikkord (labels/tags) |  |
| Om foredragsholder |  |

## Abstract

Et innblikk i hvorfor størrelsen på leveranseenheter (deployment units) er viktig og hvordan denne metrikken påvirker kostnadseffektivitet, sikkerhet og arbeidsorganisering innen utvikling. Vi ser på hvordan leveranseenheter har utviklet seg over tid og hvordan de sannsynlig vil forandre seg fremover. Fokus vil være på effektene som oppnås ved kontinuerlig arbeid for å redusere størrelsen på leveranseenhetene og hvordan dette iterativt påvirker arkitekturmålbildet.

Praktiske teknologier og tilnærminger som vil bli omtalt vil være Java, Docker, ECS, Microservices, Function as a Service (“Serverless”), Alpine Linux og Unikernels.

#### Notater

I dette foredraget ønsker vi å ta med tilhørerne på en reise...

Teoretisk tilnærming - bygge generell kompetanse, ikke hipster

uansett.. desto mindre deployment unit, desto bedre!   
= mer elastisitet (oppstartstid, hvor fort kan man skalere opp og ned)   
= TTM   
= enda lettere å håndtere nedetid

- mindre kode, mindre angrepsflate => høyere sikkerhet

## Struktur på foredraget (outline)

|  |  |  |  |
| --- | --- | --- | --- |
| 1. Sette kontekst - todo: hvordan?  - <https://www.thoughtworks.com/insights/blog/cxo-guide-microservices>  - Microservices er kommet for å bli. - Hvor stor/liten er hver tjeneste kan diskuteres, men overhead/total footprint er uansett et poeng.  2. Gjennomgang av tilnærminger  1. Deploye war til pre-installert web server/servlet container 2. Single, executable jar med embedded web server    1. Executable jar som deployment enhet    2. Pull-basert strategi implementert med script (bash, bat), nedlasting fra artifact repo. 3. Jar som deployment-enhet + Docker    1. Docker som embedder OS-oppsett og JVM       1. redusere fingerfeil i prod       2. Trenger et fungrende miljø, som dermed blir ganske stort.       3. Ubuntu som Docker-os, 188MB    2. [Docker Compose](https://docs.docker.com/compose/)       1. Forklare hvorfor [Docker Compose](https://docs.docker.com/compose/) er et skritt i feil retning. En applikasjon består av flere containere, mao. er de tett koblet og dette ønsker man ikke. Dette kan gi mening for silo-applikasjoner, men strider imot microservices-tankegangen. 4. Docker som deployment-enhet    1. Liten linux-distro, alpinelinux, 5MB, <https://www.brianchristner.io/docker-image-base-os-size-comparison/>, [alpine-zulu-jdk8](https://hub.docker.com/r/cantara/alpine-zulu-jdk8/)    2. Docker-orkestrering, helst SaaS, [Zero downtime deployment with ECS](/web/20200921035200/https://wiki.cantara.no/display/dev/Zero+downtime+deployment+with+ECS "Zero downtime deployment with ECS")    3. Infrastruktur tilpasset continouus delivery med Docker som deployment-enhet: DNS, LB, nettverk 5. Docker som deployment-enhet + JDK9 [Jigsaw](http://openjdk.java.net/projects/jigsaw/)    1. Show, don't tell - teste ut om JigSaw faktisk leverer og hvordan størrelsen blir. **TODO** Teste med en reell applikasjon.    2. Flytte dette punktet til seksjon 3 hvis man ikke har fått testet dette før presentasjonen. 6. Infrastructure as code - ([AWS CodeCommit](https://aws.amazon.com/codecommit/)), [AWS CodePipeline](https://aws.amazon.com/documentation/codepipeline/), [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 7. Future: en annen retning (unikernels?) Erlang? - maks 3min  3. Hvilke fordeler og utfordringer gir mange små?  - jo mindre - jo flere dependencies - hvordan spiller dette inn   - se neste sub-bullets - the cost of exploding number of moving parts   - end-to-end verification scenarios   - debugging of issues in production - mindre kode -> mindre angrepsflate, men også mindre framework protection  4. Hva har vi lært nå? (Why go small?)  - Hva har vi lært nå? - Hvorfor er dette viktige valg? - Hva er riktig for deg? - Hvilken forretningsverdi kan man oppnå?  1. Kostnadseffektivitet 2. Sikkerhet 3. Kan deploye kode så ofte man vil. Dette gir TTM og reell smidig utvikling. 4. Smidig arkitektur - kan legge til, bytte ut og fjerne services på en billigere og tryggere måte. 5. DevOps -> NoOps | |  |  | | --- | --- | | [Full Size](/web/20200921035200/https://wiki.cantara.no/plugins/gliffy/viewlargediagram.action?name=java deployment unit&ceoid=44663756&key=IASA&pageId=44663756)  |  | | |

## Mulige tillegg

#### Hvorfor/hvorfor ikke SpringBoot og DropWizard?

- [SpringBoot](https://projects.spring.io/spring-boot/) og [DropWizard](http://www.dropwizard.io/1.0.5/docs/)
  - Fordeler og ulemper
  - Når passer dette?
  - Innlegg fra Finn? Helge?

#### SDN, Infrastructure as Code - foreslår dette som eget foredrag

Docker og networking... IaaS og SDN... how far are we from working infrastructure as code (and do can we trust the quality aspects of todays IaaS?

#### Unikernel

unikernel-strategier er neste steg derfra..

[Omega: flexible, scalable schedulers for large compute clusters](https://research.google.com/pubs/pub41684.html)
