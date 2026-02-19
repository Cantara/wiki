# Open space - Tilbake til klient-server?

(Ove Jordbakke)

Problemet med tykke kliener?
Dataintegritet
Transaksjoner
   sesjonshåndtering
Trafikk/kommuniksajon

Fordeler med state på klienten?
    Bedre for brukere og utviklere

Bruksmønstre og krav er ulike mellom ulke typer applikasjoner

Hvor fet er en moderne 'fet' applikasjon?

Er fete applikasjoner ille? jnlp og widgets kan automatisk sjekke for siste versjon
Versjonering av tjenester og klienter kan være vanskelig (mange tjenester)

Hvordan velger man hvor fet klienten skal være? HVa slags funksjonalitet og data skal ligge hhv i klient eller server?

Hibernate med lazy loading helt til klient. Skal alt dette til klient?

Deling av state (f.eks google docs/cacher) er bedre mulig i dag
Problem: mobiler (hastighet på komm. + sikkerhet)

Transaksjonsstyring må håndteres på samme måte som ved tynne klienter.

Forbrukerkravet er at applikasjoner skal være interaktive og skal abonnere på state-change.
