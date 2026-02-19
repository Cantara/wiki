# Statistics Reporting Service-Interfaces

### Responsibility

1. Receive events from Statistics Collector Service
2. Persist and Aggregate data for later retreival.
   - Logons pr Application last day/week/month.
   - Lost users pr Application last day/week/month.

### Out of Scope

1. Live Data Feed

### Interfaces used from Statistics Collector Service

TODO

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

### Datastore

- <http://druid.io/>

### GUI tools

- <https://github.com/mistercrunch/panoramix>
- <https://github.com/implydata/pivot>

### MonetDb install

<http://rogerhosto.com/installing-monetdb-on-centosredhat/>

### Cassandra install

<http://adamhutson.com/2014/10/24/simple-cassandra-instance-in-aws-ec2/>
