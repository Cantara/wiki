# Online betaling deltakelse

For å teste, gå først til <https://developer.paypal.com/> og logg inn med simen.fure.jorgensen@iterate.no/12345678

1. Potensiell Deltager kommer inn på nettsidene
2. Potensiell Deltager ser stor, fet meld-på link (nå "registrer")
3. Potensiell Deltager skriver inn sine detaljer
   - Varianter: velger med eller uten middag
4. Nå blir Potensiell Deltager en faktisk deltager (User med Registration)
5. Ubetalt Deltager blir rutet inn på PayPal og betaler. (Bruk buyer\_1243711234\_per@iterate.no/12345678 for å teste betaling)
   - Paypal-betalingen går ikke i orden (noe deltager vil være klar
   - PayPal-betalingen går i orden, men fordi en som egentlig ikke kan  
     Ruby har kodet det hele blir den ikke registrert på en god måte
     1. Sint Deltager sender mail til smidig-listen
     2. noen herfra går inn i PayPal og sjekker at det faktisk har blitt betalt
     3. går så inn i applikasjonen og registrerer en betaling manuelt
     4. Sender så mail om at det har blitt rettet opp til Blidgjort Deltager. over).
     5. Ubetalt Deltager kan da gå inn på sin side og finne igjen betalingslinken, klikke på den og betale som over.
6. Betalt Deltager har nå en login, men deltagelsen er ikke nødvendigvis registrert som betalt (bekreftelsen fra PayPal er asynkron)
7. Når bekreftelse fra PayPal kommer registreres betalingen (Payment Notification) mot Registration
8. Om Betalt Deltager eltager nå går inn på sin side ser han at det  
   har blitt registrert (kanskje kommer det en mail, ikke implementert)
9. Betalt Deltager kan nå registrere bidrag, stemme og oppdatere sine egne detaljer (passord, firma, osv)

---

### TODO

- ~~Norsk tekst users/new og users/edit~~
- ~~Norsk feilmeldinger users/new og users/edit~~
- ~~Telefonnummer på users/edit~~
- ~~user\_sessions/new skal gi mulighet til å registrere seg som ny bruker~~
- ~~Saklig utseende ved manglende betaling på users/edit~~
- ~~Styling av users/new (spesielt: ved feil)~~
- ~~Parametrisere paypal-informasjon~~
- Logout må virke
- Sende mail ved registrering
