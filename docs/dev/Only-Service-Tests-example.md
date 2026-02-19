# Only Service Tests example

TODO: Geir

## Key words: 

- Almost all functionality is CRUD in the DA-layer. Really thin service layer and no gui. 
- Services exposed with SOAP 
- A test for the service has almost 100% overlapping with a test of the DA-functionality.
- It does not make sense to test the same things twice. 
- Service tests are important, since the APIs of the services are publicly exposed. 
- Service tests trumphs DA<sub>~tests and the DA</sub>~tests are thus skipped. 

I tilfellet at det ikke lenger er 100% overlapp mellom ACS<sub>~test og DA</sub><sub>funksjonaliteten, så vil jeg foreslå flytte mest mulig av det som Geir tidligere testet med en ACS</sub><sub>test ned til en DA</sub><sub>test. DA</sub><sub>testen kan da teste enkel CRUD, mens ACS</sub>~testen kan teste transaksjoner, at API-et er stabilt, mm.
