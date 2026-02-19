# ValueReporter

Hvem: Bård Lind

- [JavaZone Abstract](/web/20200921031659/https://wiki.cantara.no/pages/viewpage.action?pageId=38437660 "Blås i smidige team, jeg vil ha smidige applikasjoner!")

Kildekode:

- <https://github.com/Cantara/Valuereporter>
- <https://github.com/Cantara/Valuereporter-Agent>

- Hva er?
- Hvorfor?
- Hvilke alternativer?
  - Google Analytics?
    - Passer ikke for å måle backend-tjenester?
  - Munin
  - [https://mixpanel.com](https://mixpanel.com/)

- Stories
  - Hvilken funksjonalitet er i bruk?
  - Hvor ofte er x i bruk?
  - Hvor lang tid tar feature x?
  - Hvilken feature er ikke i bruk?

- SOAP - ekkelt å måle

- Features

- Architecture
  - Skille måling og rapportering.
  - Gjøre minst mulig når man måler.
  - Statistikk og aggregering gjøres etterpå i en annen tråd.

- Inspirert av AppDynamics
  - Kjøre i prod bestandig, ikke av og til som man gjør med vanlige profileringsverktøy.

- Java agent API-et.

- Er det før eller etter responsen sendes?
