# Only Service Tests example

TODO: Geir

## Key words: 

- Almost all functionality is CRUD in the DA-layer. Really thin service layer and no gui. 
- Services exposed with SOAP 
- A test for the service has almost 100% overlapping with a test of the DA-functionality.
- It does not make sense to test the same things twice. 
- Service tests are important, since the APIs of the services are publicly exposed. 
- Service tests trumphs DA-tests and the DA-tests are thus skipped. 

I tilfellet at det ikke lenger er 100% overlapp mellom ACS-test og DA-funksjonaliteten, så vil jeg foreslå flytte mest mulig av det som Geir tidligere testet med en ACS-test ned til en DA-test. DA-testen kan da teste enkel CRUD, mens ACS-testen kan teste transaksjoner, at API-et er stabilt, mm.
