# Application Authentication

- UIB is master for applicationId and applicationSecret (or other credentials).

- STS is master for application session.

---

#### Spørsmål

- Hvordan kan STS være master for autentisering av en applikasjon?
  - Hva skjer hvis applicationSecret endres i UIB? STS får ikke vite om det før cachen timer ut.
    - Det er mange scenarier her... auth er initiering av en applikajsonssesjon... deretter så er det diverse scenarier for forlengelse av sesjoner eller økning av sikkerhetsnivå på sesjonen... appsecret er bare nødvendig botstrap-mekanisme... public key er et naturlig skritt videre osv...
    - STS hånterer sesjonsinitiering og sesjons lifecycle.. UserIB er ikke en naturlig master for applikasjonsauth... og den er ikke master for user-auth i alle tilfeller heller.. som i 3-parts auth/token a-la Facebook eller MFA/2-faktor auth, hvor neste faktor er per sesjon

- Hvilke roller trenger man for å kontrollere tilgang til funksjonalitet i UIB?
  - Roller i UAW:
  - Roller som applikasjoner som bruker UAS trenger:
    - ACL delen av Application er ment for å brukes for styring av applikasjonstilgang til "admin" funksjonalitet i Whydah 2.\* og er foreløpig på formen (appid,API path,granted right) se ApplicationACL i SDK

**Et annet perspektiv er skalering... UIB er ikke bygget for det volumet av trafikk som sesjonsauth/kontroll krever**
