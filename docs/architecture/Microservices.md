# Microservices

http://martinfowler.com/articles/microservices.html (Lewis og Fowler) er én måte å definere en Micro Service-arkitektur på;

1. Componentization via Services
2. (Team) Organized around Business Capabilities
3. Products not Projects
4. Smart endpoints and dumb pipes
5. Decentralized Governance
6. Decentralized Data Management
7. Infrastructure Automation
8. Design for failure
9. Evolutionary Design  

Legg merke til at _størrelse_ ikke er et veldig sentralt tema. Minner også ganske mye om GuerillaSOA og OWSOA for de som husker de begrepene... 

En beskrivelse av arkitekturen til Whydah som passer godt inn denne kategoriseringen finnes her:
https://wiki.cantara.no/download/attachments/40206963/whydah_micro_service_architecture.pdf

#### Angles 

###### Remote vs in-process deployment 

- [Pattern: Monolithic Architecture](http://microservices.io/patterns/monolithic.html)

- [dev:Package by feature](../dev/Package<sub>~by</sub>~feature.md)

- Remote vs in-process deployment 
    - Remoting: Klient => Endepunkt(MicroService) vs   
    - Embeded: Klient(MicroService(=> koordinering)
        - Many calls embedded services for _libraries_

- En tjeneste => null, et eller flere endepunkter

###### Size and responsibility 

- Størrelse og ansvar for en tjeneste 
    - Når er den liten nok til å kalles "micro"? (SRP - Service manifest - Tjenestekategorisering)
    - Når er den for liten?  (Hvilke premisser trigger de minste)
    - [architecture:Clear and consistent responsibility power all great architectures](../architecture/Clear<sub>~and</sub><sub>consistent</sub><sub>responsibility</sub><sub>power</sub><sub>all</sub>~great-architectures.md)
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

- [OWSOA:The Laws of SOA](../OWSOA/The<sub>~Laws</sub>~of-SOA.md) - hva gir mest verdi herfra? 
    - (OW) SOA vs REST vs xx [https://wiki.cantara.no/display/OWSOA/Service+Oriented+Architecture+FAQ](https://wiki.cantara.no/display/OWSOA/Service+Oriented+Architecture+FAQ)

- [WSA:SOA Service Categories](../WSA/SOA<sub>~Service</sub>~Categories.md) - hva gir mest verdi herfra? 

#### Read more 

- [Microservices](http://martinfowler.com/articles/microservices.html), James Lewis and Martin Fowler

- [Building_Microservice_Architectures(Neal_Ford).pdf](http://nealford.com/downloads/Building_Microservice_Architectures%28Neal_Ford%29.pdf)

- [Pattern: Microservices Architecture](http://microservices.io/patterns/microservices.html)

- http://radar.oreilly.com/2015/04/4<sub>~reasons</sub><sub>why</sub><sub>microservices</sub>~resonate.html

- http://blog.arungupta.me/microservices<sub>~monoliths</sub>~noops/
