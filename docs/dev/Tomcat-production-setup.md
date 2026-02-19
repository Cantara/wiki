# Tomcat production setup

Når det gjelder tomcat er sikkerhetsfeilene det refereres til lokalisert i applikasjonene som leveres med tomcat. Aldri, aldri bruke de applikasjonene, folkens! De som er interesserte i dette kan lese bugtraq.

Tomcat i en produksjonsrigg skal være strippet for alt annet enn tomcat, defaultbrukerne (tomcat<sub>~users.xml med venner) skal fjernes, og default</sub>~konfigurasjonene skal strippes ned slik at de er et par skjermfuller lange i stedet for 25KB, monitorering må slås på, autostartskript må lages og autodeploy/redeploy skal være slått av. En god driftsorganisasjon gjør dette for deg, inntil de er gode alle sammen må vi gjøre det for de som ikke er helt på ballen.

Det er forskjell på en distribusjon som er til for at utviklere skal komme i gang fort og noe man bruker i produksjon. Jeg har oppskrift/skript for ombygging av en tomcat 5.5 fra tomcat.apache.org til noe man kan bruke i produksjon, om noen er interesserte.
