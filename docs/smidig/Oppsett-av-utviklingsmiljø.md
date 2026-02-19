# Oppsett av utviklingsmiljø

Software:
- SubVersion - http://subversion.tigris.org/
- Ruby - http://www.ruby-lang.org/en/downloads/
- SqlLite DLL - http://www.sqlite.org/sqlitedll-3_6_13.zip

# Setup
- Installer SubVersion og Ruby
- Pakk ut SqlLite DLL til et sted på PATH

Sjekk ut kode:
```
> svn co http://svn.smidig.no/smidig2009/smidig2009
```

```
gem update --system
```

Hvis du får problemer over kan det være problemer med gems-update. Forsøk å følge oppskriften som står i teksten.

```
gem install -v=2.3.2 rails
gem install net-ssh
gem install net-scp
gem install RedCloth
rake gems:install
```

# Initialisering av applikasjonen
```
rake db:migrate
rake db:populate
rake db:migrate RAILS_ENV=test
rake db:populate RAILS_ENV=test
rake test
```

# Kjør serveren
```
ruby script\server
```
