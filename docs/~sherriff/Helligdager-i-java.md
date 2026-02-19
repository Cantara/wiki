# Helligdager i java

Noen ressurser

###### Hente røde dager 

- webcal feed for å hente røde dager: webcal://ical.mac.com/ical/Norwegian32Holidays.ics 
- [ical4j](http://ical4j.sourceforge.net/) kan brukes for å lese feed'en

###### Støtte for håndtering av røde dager 
 
1. [datecalc<sub>~joda](http://objectlabkit.sourceforge.net/datecalc</sub>~joda/index.html) - algoritmer for å håndtere hva som skal skje når en beregnet dato havner på en "rød dag". Hvilke dager som faktisk er røde må hentes fra et annet sted. 
- Gjøre det selv: http://boss.bekk.no/nocommons/xref/boss/nocommons/date/NorwegianDateUtil.html
- http://www.tondering.dk/claus/calendar.html
- http://www.java.no/forum/posts/list/10615.page beskriver hvordan andre har løst dette. 

Mao. så burde dette kunne løses rent teknisk ved å bruke: [datecalc<sub>~joda](http://objectlabkit.sourceforge.net/datecalc</sub>~joda/index.html) + [ical4j](http://ical4j.sourceforge.net/) + webcal://ical.mac.com/ical/Norwegian32Holidays.ics
