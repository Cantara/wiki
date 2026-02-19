# Gradle vs Maven - Incremental build shootout

Dersom du har jobbet på et multiprosjekt har du sikkert ønsket deg inkrementell bygging.  
Når du sjekker ut siste endringer fra VCS har du bare lyst til å bygge de prosjektene som faktisk trenger å bygges på nytt.  
Når du endrer noen filer i et subprosjekt, ønsker du bare at dette prosjektet og de som avhenger av det skal bygges.  
Bygging av et subprosjekt består av flere steg (kompilere, samle sammen ressurser, lage jar/war/zip e.l, kompilere tester, teste osv).  
Hadde det ikke vært smart dersom bare de stegene som behøver å kjøre ble kjørt, basert på de endringer som er gjort siden sist du bygde ?

Dersom din oftest brukte byggekommando inkluderer stegene "clean install" har du antageligvis gitt opp drømmen om inkrementell bygging.  
Men sånn skal det jo ikke å være !

I dette foredraget møtes **Gradle** og **Maven** til shootout i inkrementell bygging.
