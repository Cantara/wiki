# whydah -sso arbeide

...så det er ikke pri... pri 1)  se at redirect fra NetIQ kommer til whydah... og at det trigger opprettelsen av en whydah bruker
[13:36:29](../13/36-29.md) Thor Henning Hetland: pri 2)  frontend... legge til den knappen som brukeren skal trykke på for Altran-eurpoe auth
[13:37:45](../13/37-45.md) Thor Henning Hetland: pri 3) sjekke/verifisere at vi ikke  ister redirect-URL som kommer i URL på redirect fra ACS...  når vi videreformidler auth via NetIQ  (event ta vare på den eksplisitt)
[13:38:28](../13/38-28.md) Thor Henning Hetland: pri 4)  justere UserToken default rolle-hierarki til ACS fra (to be written) ACS rolledefinisjoner
[13:39:23](../13/39-23.md) Thor Henning Hetland: ..av disse, så er det 1 som er mest fiklearbeid, og som kan forvente å produsere noen bugs/hull i whydah
