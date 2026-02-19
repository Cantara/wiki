# 2011-05-05 - Architecture Support for Testing

#### Praktisk

- Tid: kl 18:00
- Sted: Scotsman, 2. etg.
- Påmelding: <http://www.meetup.com/Oslo-Software-Architecture/events/17230908/>
- Trådløst nett
  - SID: *kontor*
  - Passord: blir opplyst på møtet

#### Ideer for lyntaler og open spaces

IASA møter er avhengige på brukerinnhold. Bidra med et forslag for et [lyntale](http://en.wikipedia.org/wiki/Lightning_Talk) (10-20 min) eller et tema for en [open space](http://en.wikipedia.org/wiki/Open-space_meeting) diskusjon. Snakk kan være om problemer du møter, suksesser du har hatt, eller ideer du har hørt om at du ønsker andre å diskutere.

Hvis du er innlogget, kan du redigere siden for å legge til forslaget listen (nedover). Ellers ganske enkelt [sende den rett til IASA team](mailto:iasa-styret@iasa.no)

#### Motivation

One of the new initiatives of the Software Engineering Institute ([SEI](http://www.sei.cmu.edu/)) is to explore the practice of [Architecture support for Testing](http://saturnnetwork.wordpress.com/tag/AST-project/).

That is, using the system’s architecture to inform and guide the system’s testing activities. While there has been substantial work devoted to this topic in the research community, not much of that research seems to have filtered into communities of practitioners. Hence, the promise of architecture-based testingto use architecture to reduce the time and expense of testing and to increase its effectivenessremains unfulfilled.

It would be useful to collect experiences and ideas from IASA.no members around this topic and feed them into the project.  
Similarly it would be useful to get ideas already collected by the SEI from other practitioners out to our community.

#### Agenda

| lyntale eller space | Tittel | Beskrivelse | Forslått av |
| --- | --- | --- | --- |
| lyntale | [Summary of SEI's Architecture Support for Testing Initiative](/web/20221205143214/https://wiki.cantara.no/display/IASA/Oppsummering+av+Architecture+Support+for+Testing "Oppsummering av Architecture Support for Testing") | oppsummering av arbeidet så langt fra SEI initiativet | [Jason Baragry](/web/20221205143214/https://wiki.cantara.no/display/~baragry) |
| Foredrag - 30min | [How your choice of middleware product affects your testability](/web/20221205143214/https://wiki.cantara.no/display/IASA/How+your+choice+of+middleware+product+affects+your+testability "How your choice of middleware product affects your testability") |  | [Bård Lind](/web/20221205143214/https://wiki.cantara.no/display/~baard.lind) |
| lyntale | [Enklere testing med arkitektur?](/web/20221205143214/https://wiki.cantara.no/pages/viewpage.action?pageId=23298318 "Enklere testing med arkitektur?") | En kjapp gjennomgang av noen vanlige løsninger og hvordan det påvirker testbarhet. | [Anders Sveen](/web/20221205143214/https://wiki.cantara.no/display/~anders@f12.no) |

Blir diskusjon/openspace/spørsmål enten rett etter hvert foredrag eller etter at alle tre er ferdig.

#### Notes:

- testing consequences of middleware
- arch and testing ideas from Anders
- strong experience with Agile and continuous build, test
- arch support for automatic testing during dev process
- mye focus on automatic testing because of agile focus in norway.
- e.g., hard to test middleware that can't play nice automatic testing
- identifying bounded contexts to help define test boundaries
- sometimes easier to test req-resp because you don't need to test JMS / DB separately
- the arch tendancy to modiarise and distribute without thinking through assumptions for them can be dangerous for testing. Esp for synch comms testing
- important to be able to isolate components for testing. This can be hard with ESBs that try to do eveything. Hard to include these types of middleware in automatic testing.
- can you include all arch qualities in an auto test system. E.g., specflow, cucumber. Which qualities can you test without a full test environment. E.g., perhaps msg-level security but not performance.
- difference between check (auto) and test (manual) in how you consider testing.
- how to get DBs and MQs into a certain state at the start of a test suite?
- difficult to get infrastructure into a start state to do proper auto testing
  - DB, webserver, appserver, etc.
- how do you affect the procurement process to influence technology choice based on middleware testability?
- where does testing separate from monitoring?
  - - E.g., ESBs are very good for monitoring the infrastructure so you can see what has actually happened. But they are not good for testing during dev
- testers should be better educated about monitoring possibilities. E.g., use a http sniffer
  - - - google test blog
    - devOps -> devTesters

#### Forslag

| lyntale eller space | Tittel | Beskrivelse | Forslått av |
| --- | --- | --- | --- |
| Lyntale og/eller openspace | [Integration architecture and testability](/web/20221205143214/https://wiki.cantara.no/display/IASA/Integration+architecture+and+testability "Integration architecture and testability") |  | [Erik Drolshammer](/web/20221205143214/https://wiki.cantara.no/display/~sherriff) |
|  | [The architect-test manager interface](/web/20221205143214/https://wiki.cantara.no/display/IASA/The+architect-test+manager+interface "The architect-test manager interface") | Hvilke forventninger/ønsker/krav har testleder? | [Ingvild Meyer Pedersen](/web/20221205143214/https://wiki.cantara.no/display/~olavsdatter@gmail.com) (ikke anledning til å snakke om dette) |
|  |  |  |  |
