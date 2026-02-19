# Internal authentication and authorization in Whydah

### Authentication

Users and applications are authenticated with their respective sessions.

### API authorization matrix in UIB

|  | Whydah application session | External application (was: Third-party application session) | Whydah Administration session (internal) |
| --- | --- | --- | --- |
| user session | session control | myApp.contains()+myRole.contains() ?? Forsto ikke denne. |  |
| no user session | login,sign-up, reset password, (app auth) | on-behalf of | on-behalf of, 3rd party tokens(SSOLWA) |

---

### API authorization matrix in UAS

|  | Roletype | Whydah application session | External application (was: Third-party application session) | Whydah Administration session (internal) |
| --- | --- | --- | --- | --- |
| user session with elevated roles |  |  |  |  |
| user session |  |  |  |  |
| no user session | any | login,sign-up, reset password, (app auth) | on-behalf of | on-behalf of, 3rd party tokens(SSOLWA) |

---

Some background

- [Endpoint design](https://wiki.altrancloud.com/display/whydah/UIB+services+%28API%29)
