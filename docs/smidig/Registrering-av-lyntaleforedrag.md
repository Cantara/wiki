# Registrering av lyntaleforedrag

### Scenario: Bruker er allerede påmeldt og logget inn

1. Bruker går inn på programmet (brukeren kan allerede ha betalt)
2. Bruker velger et tema
3. Bruker velger "foreslå ny lyntale"
4. Bruker fyller ut informasjonen og trykker "Publisert mitt forslag"
5. Brukeren kommer til listen over foredrag om temaet
6. Brukeren kan se sitt forslag på listen

### Scenario: Bruker er ikke påmeldt

1. Bruker går inn på programmet (brukeren kan allerede ha betalt)
2. Bruker velger et tema
3. Bruker velger "foreslå ny lyntale"
4. Brukeren fyller ut informasjon både om foredraget og om seg selv (navn, firma, epost (påkrevd), telefon (påkrevd))
   1. Avvik: Epostadressen er allerede i bruk
      1. Brukeren får feilmelding og brukerinfo-feltene blir erstattet med "epost" (preutfylt) og "passord", slik at brukeren kan logge inn (får ikke endre navn, firma, telefon)
5. Brukeren kommer til listen over foredrag om temaet
6. Brukeren kan se sitt forslag på listen

### Scenario: Bruker går ikke via topics siden

1. Bruker går inn på informasjonen om lyntaler (pages/lyntale)
2. Bruker klikker på linken "Foreslå en lyntale"
3. Bruker får opp skjema (som over), men en dropdownliste for å velge tema.

---

### TODO:

- ~~Norsk tekst på topics/index~~
- ~~Norsk tekst på topics/show~~
- Norsk tekst på talks/new
- Norsk tekst på feilmeldinger for talks/new
- ~~"x votes" og "login to vote" etc skal være i en unfinished blokk~~
- ~~Skjul "slideshare" link på talks/new.~~
- Validering på talk.rb for påstand og argumentasjon
- talks/new må funke selv om man ikke har valgt tema
- talks/new må støtte at man ikke er logget inn
