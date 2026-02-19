# Legge ut applikasjonen på smidig2009

1. Deployment-script er laget. For å støtte ikke-innsjekket konfig:
    1. tmp/database.yml overstyrer config/database.yml
    1. tmp/environment.rb kjøres før config/environment.rb. Denne setter RAILS_ENV
1. Det deployes til $HOME/apps/smidig2009/staging/smidig2009, som vises på staging.smidig2009.no.
1. Alt ser ut til å fungere nå
1. Når CSS er fikset legges den ut på smidig istedet for bare staging.
