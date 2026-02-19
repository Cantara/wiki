# gilb-exercise

Integrasjon.interoperability 
Ambition: Enkel og selvforklarende integrasjon 
Includes: flexibility, interoperability, compatibility, readability, integrity, maintainability,
Scale: number of \[endpoints/formats\](endpoints-formats.md) supported 
Past:		1 
Tolerable: 	2
Goal: 		4

Integrasjon.maintainability
Ambition: Enkel og selvforklarende integrasjon 
Includes: flexibility, interoperability, compatibility, readability, integrity, maintainability,
Scale: 	consumers per endpoint
	(# endpoints)
	
Past:		400/30 = 13.3 
Tolerable: 	450/15 = 30 
Goal: 		600/8 = 75 

**Integrasjon.readability**
Ambition: Enkel og selvforklarende integrasjon 
Includes: flexibility, interoperability, compatibility, readability, integrity, maintainability,
Scale: 	# supporthenvendelser relatert til lesbarhet / måned 
	true/false: Alle \[Termer\](Termer.md) er entydig definert i \[Glossary / Ubiquitous Language\](Glossary-Ubiquitous-Language.md)
Past:		\[2011, Oslo\](2011-Oslo.md) 60 +- 10 ?	<- <kilde>
Tolerable: 	\[2012-06, Oslo\](2012-06-Oslo.md) 40 +- 8	
Goal: 		\[Q1 2013, NORGE\](Q1-2013-NORGE.md) 4 +- 3

###### 5.1 Design, architecture
Design tag: Forbedre _andre_ supportkanaler 
Design summary: Sette opp issue tracker og gi veldig god service for alt som rapporteres her. 
Design detail: 

Design tag: Åpne, tekstlige formater
Design summary: Velge kjent teknologi 
Design detail: XML, sterk typing, bruke \[TERMER\](TERMER.md), dok i schema

Notat: anti-smidig, lite fleksibel, krever mye versjonering. 

Design tag: Lage "How to integrate"-dokument 
Design summary: Trinnvis (teknisk) beskrivelser av integrasjon
Design detail: Sette opp wiki for partnere, gi partnere tilgang til kildekoderepo hvor testene er eksempler. 
D0: (Prerequisite) Sette opp wiki og tilganger for partnere. 
D0 + D1: Java
D0 + D3. .NET
D0 + D2: c++

Constraint: Contract - first 
Constraint: Alle \[Termer\](Termer.md) er entydig definert i \[Glossary / Ubiquitous Language\](Glossary-Ubiquitous-Language.md)
 

###### 6.1 Design impact, 6.2 Evidence 

Endepunktet finnes allerede. 

**Fulfillmen**t: 98% +- 15% 

**Evidence impact**: 
- Eat your own dog food - det er slik vi ville hatt det hadde vi vært partner)
- Spurte de 5 partnerne med flest integrasjoner. 
- Credibility: 0.7

**Investment cost**: 8dv +- 3 (basert på tidligere kostnad for tilsvarende arbeid)

**Evidence cost**: Basert på erfaring og historikk - Statistikk fra kundeservice sortert på kategorier. \[url til excel-fil\](url-til-excel-fil.md)
- Credibility: 0.8

D0 + D1: Java - 50% +- 10% 
D0 + D3. .NET - 40% +- 10% 
D0 + D2: c++ - 10% +- 10%   

---

Group consumers 

A2A service per group 

Core service
