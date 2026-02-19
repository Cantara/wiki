# Micro services

<http://martinfowler.com/articles/microservices.html> (Lewis og Fowler) er én måte å definere en Micro Service-arkitektur på;

1. Componentization via Services  
2. (Team) Organized around Business Capabilities  
3. Products not Projects  
4. Smart endpoints and dumb pipes  
5. Decentralized Governance  
6. Decentralized Data Management  
7. Infrastructure Automation  
8. Design for failure  
9. Evolutionary Design

Legg merke til at *størrelse* ikke er et veldig sentralt tema. Minner også ganske mye om GuerillaSOA og OWSOA for de som husker de begrepene...

En beskrivelse av arkitekturen til Whydah som passer godt inn denne kategoriseringen finnes her:
<https://wiki.cantara.no/download/attachments/40206963/whydah_micro_service_architecture.pdf>

#### Angles

###### Remote vs in-process deployment

- [Pattern: Monolithic Architecture](http://microservices.io/patterns/monolithic.html)

- [Package by feature](/web/20220817073543/https://wiki.cantara.no/display/dev/Package+by+feature "Package by feature")

- Remote vs in-process deployment
  - Remoting: Klient => Endepunkt(MicroService) vs
  - Embeded: Klient(MicroService(=> koordinering)
    - Many calls embedded services for *libraries*

- En tjeneste => null, et eller flere endepunkter

###### Size and responsibility

- Størrelse og ansvar for en tjeneste
  - Når er den liten nok til å kalles "micro"? (SRP - Service manifest - Tjenestekategorisering)
  - Når er den for liten? (Hvilke premisser trigger de minste)
  - [Clear and consistent responsibility power all great architectures](/web/20220817073543/https://wiki.cantara.no/display/architecture/Clear+and+consistent+responsibility+power+all+great+architectures "Clear and consistent responsibility power all great architectures")
  - [Single responsibility principle](http://en.wikipedia.org/wiki/Single_responsibility_principle)

###### Deployment and infrastructure

- Behov for infrastruktur MicroServices - Embedded microservices
  - EMI
  - Discovery - **TODO**: Hva trenger man av discovery?
- Behov for infrastruktur MicroServices - Remote microservices
  - EMI
  - Discovery - **TODO**: Hvor mange/hvor stort må systemet være før man åpenbart ikke klarer seg uten discovery?
  - Automatisering av deployment
    - Automatiserte oppgradering, Oppgraderinger uten nedetid
    - Automatiske oppgraderinger (Kontinuerlig produksjon)

###### TODO

- Pitfalls
  - drift
  - utvikling
  - design
  - versjonering
  - hva med "kontroll"
    - tilgang
    - bruk
    - last

- [The Laws of SOA](/web/20220817073543/https://wiki.cantara.no/display/OWSOA/The+Laws+of+SOA "The Laws of SOA") - hva gir mest verdi herfra?
  - (OW) SOA vs REST vs xx [https://wiki.cantara.no/display/OWSOA/Service+Oriented+Architecture+FAQ](../OWSOA/Service-Oriented-Architecture-FAQ.md)

- [WSA:SOA Service Categories] - hva gir mest verdi herfra?

#### Read more

- [Microservices](http://martinfowler.com/articles/microservices.html), James Lewis and Martin Fowler

- [Building Microservices](https://www.amazon.com/Building-Microservices-Sam-Newman/dp/1491950358/ref=sr_1_1?ie=UTF8&qid=1467900597&sr=8-1&keywords=micro+services) by Sam Newman

- <http://microservices-book.com/primer.html>

- [Building\_Microservice\_Architectures(Neal\_Ford).pdf](http://nealford.com/downloads/Building_Microservice_Architectures%28Neal_Ford%29.pdf)

- [Pattern: Microservices Architecture](http://microservices.io/patterns/microservices.html)

- <http://radar.oreilly.com/2015/04/4-reasons-why-microservices-resonate.html>

- <http://blog.arungupta.me/microservices-monoliths-noops/>
