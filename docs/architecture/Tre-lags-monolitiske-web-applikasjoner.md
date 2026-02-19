# Tre-lags monolitiske web-applikasjoner

Tre-lags monolitiske web-applikasjoner lider ofte under en rekke velkjente plager. I hjerte av det hele finner vi en relasjonsdatabase med en komplisert, spesialtilpasset og normalisert datamodell. Tross gode intensjoner, kryper det inn tette koblinger både i datamodellen og i hele kildekodebasen med "gjenbruk" som alibi. På lang sikt viser det seg at denne type arkitektur skalerer dårlig i alle akser.

- Koden er vanskelig å forstå, ofte med mange rotete hack fordi "man kan".
- Nesten umulig å skalere opp til store datamenger og svært høy last.
- Stadig dyrere og legge til funksjoner, siden alt henger så tett sammen.
- Ofte bare én eller to personer som kjenner applikasjonen godt nok til å kunne ta viktige avgjørelser og utføre dem i kodebasen med lav nok risiko.
- Nye funksjoner som legges til er bundet til gammel teknologi.
- Rapporteringsmodul integrert direkte med databasen gjør endringer på datamodell svært dyre.
- Front-end utvikling nært knyttet til back-end gjør det vanskelig å benytte spesialkompetanse på front-end.
- Umulig å teste alt som er viktig.
- Funksjonene applikasjonen tilbyr blir aldri skikkelig stabile fordi nye funksjoner og endringer påvirker eksisterende funksjonalitet.

Argumentet med god/dårlig disiplin holder ikke i lengden, siden de som programmerer og tar avgjørelser byttes ut over tid. Den eneste måten å unngå alle disse problemene er en radikalt annerledes arkitektur hvor disse problemene ikke kan oppstå, eller har betydelig mindre omfang.
