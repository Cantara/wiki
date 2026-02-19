# Statistics Collector Service-Interfaces

### Responsibillity

1. Receive events from Whydah Components
2. Forward selected events to StatisticsService-Reporting
3. Serve live data on selected events.
   - Logons last 15 minutes.
   - Failed logons last 15 minutes.

### Out of Scope

1. Aggregate data for reporting?

### Interfaces used from UserAdminService

| Resource | Method | Expect | Description |
| --- | --- | --- | --- |
| **User(s)** |
| **Logons** |
| **RoleRequests** |
| "users/ |
| "user/uid | GET | Json |  |
| "user/uid | PUT | Json |  |
| "user/uid | DELETE | Json |  |
| "user/ | POST | Json |  |
| **Role** |
| TODO "user/"uid"/roles" | GET | Json |  |
| TODO "user/"uid"/roles" | POST | Json |  |
| TODO "user/"uid"/role/"+roleId | DELETE | Json |  |
| TODO "user/"uid"/role/"+roleId | PUT | Json |  |
| **Password** |
| TODO "password/" + apptokenid +"/reset/username/" + username | POST | Json |  |
| **Applications** |
| TODO "applications" | GET | Json |  |

### Tech Stack

**Time Series Analysis**

- [RRD Tool](http://oss.oetiker.ch/rrdtool/index.en.html)
- [RRD Tool 4 Java](https://github.com/rrd4j/rrd4j)? - License: Apace 2, create PNG's
- <http://opentsdb.net/> - License: LGPL

**Graphite/Ganglia**

- Monitoring tools @Monitoring support

**ValueReporter**

- Agent and GUI

**Home Brew**

- Stoage??
- Presentation via HighChart - "Live JavaScript"
- Backend:
  - RDD database?

**Backend**

- HBase?? <https://hbase.apache.org/>
