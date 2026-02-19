# Whydah development environment installation

### Whydah development Express-route for linux and osx/mac

|  | Pre-requisites: JDK 8, maven 3 and wget installed |

1. run bootstrapAndRunWhydah.sh (wget <https://raw.githubusercontent.com/Cantara/Whydah/master/dev-quickstart/bootstrapAndRunWhydah.sh>) which will do the following
   1. clone all main Whydah repositories
   2. build all modules on local machine
   3. start all built modules in a TEST\_LOCALHOST configuration
2. verify that it is working before starting to code (<http://localhost:9997/sso/welcome> u:useradmin pw:useradmin567)
