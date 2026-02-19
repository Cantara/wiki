# Thoughts on architecture when using HTTP endpoints

Dvs. gui<sub>~server</sub>~side blir proxy mot en bakenforliggende tjeneste. Husker du om vi dokumenterte noe om dette i cantarawiki?
Poengene/læringen jeg kommer på i farten:
1. Billigere, enklere og raskere å bygge funksjonalitet i java enn i javascript
1. CORS virker, men gir egentlig ikke noe særlig verdi. Delvis pg.a 1.
    1. CORS er et brudd på standard javascript sikkerhetsmekanisme! 
1. Trenger "proxy" i gui<sub>~server</sub>~side for a) sikkerhet og b) mulighet for aggregering og behandlet av innkommende data. 

To alternativer:
a. Hvis app gjør IAM på vegne av Javascript så trenger man proxy.

b. Hvis javascript gjør IAM selv, så kan man gå direkte. 

I en kontekst hvor man eier alle tjenestene og alle endepunktene og skal ha tilgangskontroll, så er kontekst ganske anderledes enn WWW. 

 Konklusjon er at jeg må skrive lenkene som kommer fra bakenforliggende tjeneste slik at alt går via proxy.
