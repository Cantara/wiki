# Testprotokoll

### Teste registrering av foredrag når bruker er registrert

1. Åpne en ny browser uten cookies mot Smidig 2009
2. Gå til forsiden
3. Velg "Foreslå lyntale"
4. Legg inn informasjon for "admin@smidig.no" med passord "feilpassord". La info om foredrag være tom
5. Sjekk at du får en feilmelding om at email er tatt eller passord er feil
6. Endre passord til "passord". La resten av informasjonen om bruker være tom. La info om foredrag være tom
7. Sjekk at brukerregistreringsdialogen blir borte og at du får feilmelding om foredraget
8. Legg inn foredraget.
9. Sjekk at du ikke får feilmelding og at foredraget blir registrert i riktig kategori

### Teste registrering av foredrag når bruker ikke er registrert

1. Åpne en ny browser uten cookies mot Smidig 2009
2. Gå til forsiden
3. Velg "Foreslå lyntale"
4. Legg inn informasjon med en ny email (NB: <brukernavn>+<whatever>@gmail.com kan brukes for å få unike brukernavn). Utelat navn, telefonnummer, påstand, argumentasjon, "jeg kjenner til retningslinjer", godta creative commons.
5. Sjekk at du får riktige feilmeldinger og at relevante felter blir røde.
6. Legg inn all informasjon og trykk "registrer"
7. Sjekk at du ikke får feilmelding og at foredraget blir registret i riktig kategori

### Teste registrering påmelding av bruker uten foredrag

1. Åpne en ny browser uten cookies mot Smidig 2009
2. Gå til forsiden
3. Trykk "Påmelding"
4. Utelat all informasjon og trykk "Gå videre til betaling"
5. Sjekk feilmeldinger og at felter blir røde
6. Legg inn all informasjon (NB: <brukernavn>+<whatever>@gmail.com kan brukes for å få unike brukernavn)
   - ~~NB: Her sluttet plutselig denne versjonen av siten å fungere for meg. Ikke et varig problem. (Johannes, 2009-06-17)~~
7. Sjekk at du sendes videre til PayPal
8. Før du betaler: Åpne en ny browser og se på brukerens detaljer. Sjekk at det står at vi venter på PayPal
9. Gjennomfør betaling
10. Sjekk at brukerens detaljer nå angir at han har betalt.
