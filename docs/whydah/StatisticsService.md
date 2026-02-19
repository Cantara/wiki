# StatisticsService

# Whydah StatisticsService

**Some *live* urls to see som datasets**

| Type | URL | Comments |
| --- | --- | --- |
| whydahdev - graph | <https://whydahdev.cantara.no/reporter/gui/whydah/usersession> |  |
| whydah graph | <http://whydah.cantara.no/reporter/gui/whydah/usersession?prefix=initial> |  |
| whydag - jsopndata | <https://whydah.cantara.no/reporter/observe/statistics/initial/usersession> |  |

# Architecture

*Diagram: Whydah Statistics Service Architecture*

---

# StatisticsService Whydah configuration properties

|  | Remember to ensure that port 4901 is open from SecurityTokenService to StatisticsService |

# Identify and document 3 important use-cases.

### #1 Number of active users pr xx period:

- what data is needed
  - userid, "logon"
- where are these data collected from
  - UAS
- how is these data collected
  - Report every user validation. -> Statistics Service

### #2 Number of active users for an application pr xx period:

- what data is needed
  - userid, applicationid,methodName?/"getRoles static"
- where are these data collected from
  - UAS
- how is these data collected
  - Report every call for getRoles from Application. -> Statistics Service

### #3 My Whydah auth/application activities

- what data is needed
  - userid, applicationid, method
- where are these data collected from
  - UAS, STS?
- how is these data collected

# More usecases to be covered

### #4 New users for a period/appication

### #5 Application revoked per time/application
