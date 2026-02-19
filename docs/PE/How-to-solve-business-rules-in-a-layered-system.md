# How to solve business rules in a layered system

## Service

Laaaang diskusjon om hvordan man skal implementere forretningsregler på forskjellige lag.

Såvidt vi kan forstå er det tre alternativer her:

1) **Duplisere logikken** på alle lag (industristandard :~~) \~~ DRY - store muligheter for feil og inkonsistes mellom de forskjellige beregningene.
2) **Mobil kode** - Kjøre forretningsreglene på klientside og serverside. Vanskelig å få til - kan løses med rike klientobjekter med det liker vi ikke. XML og XSLT kan løse dette. Mangler rammeverk.
3) **Sentralisering** Finkornete tjenester som utfører operasjonene. Medfører "chatty" api - skalerer dårlig.

**Løsningen på problemet er alt 2.** Minst pain er duplisering. Men det blir et _helvete_ å holde regler i sync. Enterprise DNA, statiske regler, blokkerer forretningsverdi.
