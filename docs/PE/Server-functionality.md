# Server functionality

Under skisserer vi den "normale" oppfatningen av stateless/statefull:

| State category | Data style | Sub data style | Technology |
| --- | --- | --- | --- |
| Statefull | Domain Model strategy | [Full Domain model](Full<sub>~Domain</sub>~model.md) | [DM EJB](DM-EJB.md) |
|  |  |  | [DM WS](DM-WS.md) |
|  |  |  | [DM RMI](DM-RMI.md) |
|  |  | [Edit bubles](Edit-bubles.md) / partitioned domain model approach | [EB EJB](EB-EJB.md) |  |
|  |  |  | [EB Rest](EB-Rest.md) |  |
|  |  |  | [EB WS](EB-WS.md) |  |
|  |  |  | [EB RMI](EB-RMI.md) |  |
|  |  |  | [EB SOA](EB-SOA.md) |  |
|  | Mobile Code | [Master worker](Master-worker.md) | [MW JINI](MW-JINI.md)/JavaSpace Tuplespaces. |  |
|  |  | [Mobile Services](Mobile-Services.md) | [MS JINI](MS-JINI.md)/JavaSpaces Tuplespaces. |  |
|  |  |  | [MS SOA](MS-SOA.md)SOA |  |
|  | [Shared state](Shared-state.md) |  | [Dist Cache](Dist-Cache.md) |  |
|  |  |  | [BB EJB](BB-EJB.md) |  |
|  |  |  | [BB RMI](BB-RMI.md) |  |
| Stateless | [State til klient](State<sub>~til</sub>~klient.md) |  | [CS Servlet](CS-Servlet.md) |  |
|  |  |  | [CS REST](CS-REST.md) |  |
|  |  |  | [CS JMS](CS-JMS.md) |  |
|  |  |  | [CS Spring](CS-Spring.md) |  |
|  |  |  | [CS WS](CS-WS.md) |  |
|  |  |  | [CS SOA](CS-SOA.md) |  |
|  | [State til base](State<sub>~til</sub>~base.md) |  | [SS Servlet](SS-Servlet.md) |  |
|  |  |  | [SS JMS](SS-JMS.md) |  |
|  |  |  | [SS Spring](SS-Spring.md) |  |
|  |  |  | [SS WS](SS-WS.md) |  |
|  |  |  | [SS SOA](SS-SOA.md) |  |
|  | "Ekte" [No state](No-state.md) |  | [NS Servlet](NS-Servlet.md) |  |
|  |  |  | [NS JMS](NS-JMS.md) |  |
|  |  |  | [NS Spring](NS-Spring.md) |  |
|  |  |  | [NS WS](NS-WS.md) |  |
|  |  |  | [EDA](EDA.md) |  |

---

**state**

De aller fleste tjenester har state. Det vi ofte kaller stateless er statefull - bare at state holdes clientside eller i basen.

**Stateful**

**Stateless**
To grunner til å bruke "stateless":
- Lettere å debugge
- MS har fortalt oss at det skalerer dårligere.

True stateless: du har ikke state. 2+2 tjenesten. Få av disse.
