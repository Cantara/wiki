# No request-response architecture

Vanlig tjenesteorientert arkitektur fører til at man får sterke avhengigheter mellom de ulike tjenestene: Ordretjenesten må hente data fra kundetjenesten som skal sende en melding videre til pakketjenesten, og alt må være i en stor distribuert transaksjon for å sikre konsistens. Det skalerer dårlig og er vanskelig å vedlikeholde, men er fortsatt den mest nærliggende måten å tenke på kommunikasjon i et distribuert system. Hva gjør vi arkitekter for å hindre at vi bygger flere slike systemer?
