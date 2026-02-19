# UserAdminService Interfaces

### Used from UserAdminWebApp

| Resource | Method | Expect | Description |
| --- | --- | --- | --- |
| **User(s)** |
|  | GET | Json |  |
| "user/uid | GET | Json |  |
| "user/uid | PUT | Json |  |
| "user/uid | DELETE | Json |  |
| "user/ | POST | Json |  |
| **Role** |
| "user/"uid"/roles" | GET | Json |  |
| "user/"uid"/roles" | POST | Json |  |
| "user/"uid"/role/"+roleId | DELETE | Json |  |
| "user/"uid"/role/"+roleId | PUT | Json |  |
| **Password** |
| "password/" + apptokenid +"/reset/username/" + username | POST | Json |  |
| **Applications** |
| "applications" | GET | Json |  |

### Used from 3.party apps

| Resource | Method | Expect | Description |
| --- | --- | --- | --- |
| **User(s)** |
|  | GET | XML |  |
| "user/uid | GET | XML |  |
| "user/uid | PUT | XML |  |
| "user/uid | DELETE | XML |  |
| "user/ | POST | XML |  |
| **Role** |
| "user/"uid"/roles" | GET | XML |  |
| "user/"uid"/roles" | POST | XML |  |
| "user/"uid"/role/"+roleId | DELETE | XML |  |
| "user/"uid"/role/"+roleId | PUT | XML |  |
| **Password** |
| "password/" + apptokenid +"/reset/username/" + username | POST | XML |  |
| **Applications** |
| "applications" | GET | XML |  |

....
