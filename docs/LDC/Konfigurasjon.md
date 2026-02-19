# Konfigurasjon

# Konfigurasjon ved PropertyPlaceholderConfigurer

Web<sub>~applikasjonen benytter en properties</sub><sub>fil og Springs PropertyPlaceholderConfigurer til å sette opp miljøavhengig konfigurasjon. Konfigurasjon leses inn fra properties</sub><sub>filen ldapclient.properties. Valg av properties</sub>~fil gjøres ved å sette variabelen LDAPCLIENT_CONFIG til å peke til katalogen hvor ldapclient.properties ligger. 

# Git

Properties<sub>~filer for ulike miljøer er kan hentes ut fra git</sub>~repoet: git clone ssh://<username>@git.retrade.webstep.no/mnt/sdf/retrade/repository/ldapclient-config.git

# Oppstart

Ved oppstart av applikasjonen må LDAPCLIENT_CONFIG settes til å peke til katalogen hvor ldapclient.properties ligger. 

F.eks: mvn jetty:run -DLDAPCLIENT_CONFIG=<path>
