# Code organization to support easy removal

Jeg organiserer ofte rekkefølgen på kode i en klasse etter to prinsipper:
1. (hovedprinsipp): det metodene som man mest sannsynlig er interessert i å lese øverst. Dvs. de metodene med mest logikk som er synlige utenfor klassen. 

2. Legger metoder som kalles fra "viktige" metoder rett under de viktige metodene.
Pkt2. gjør at når man tar vekk en funksjon, så ligger som oftest koden som er tett koblet/relatert rett under og blir da stort sett alltid med ved sletting.

Dette gjør gir oss den som utvikler feedback om hva som er fornuftig oppdeling i metoder, synlighet og kobling til tester. 

TODO: Kan godt utdype og beskrive dette mye bedre hvis noen interessert. Bare spør ErikD. :)
