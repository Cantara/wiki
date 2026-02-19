# Whydah deployment alternatives

#### Evaluate, learn and integrate setups

| What | Purpose | Status | Comment |
| --- | --- | --- | --- |
| [All in one Docker image](https://github.com/Cantara/Whydah) | Evaluate and learn about Whydah. Use test-webs to experiment with protocol. |  | simplest possible setup |
| Integration environment on developer laptop using java -jar | allow basic integration testing during development. Only SSOLWA and STS needed. Can experiment with tokens and roles based on username with stub overrides |  | useful on Windows, prefer Docker on Linux environments |
| Integration environment on developer laptop using Docker (one image per application) | allow basic integration testing during development easier than running all applications from jar or IDE |  |  |

---

#### Complete Environment installation

| What | Purpose | Status | Comment |
| --- | --- | --- | --- |
| Production installation using [Ansible scripts](https://github.com/Cantara/Whydah-Provisioning) | Production HA setup |  | STS in HA mode (HazelCast), mostly used for AWS EC2 deployments   external database and LDAP for UIB  need to review and decide Docker or Ansible for LDAP server installation   automation of webproxy installation with https needs more testing |
| Production installation using [Ansible scripts](https://github.com/Cantara/Whydah-Provisioning) | Production setup |  | external database and LDAP for UIB  need to review and decide Docker or Ansible for LDAP server installation   automation of webproxy installation with https needs more testing |
| Devtest installation using [Ansible scripts](https://github.com/Cantara/Whydah-Provisioning) | Devtest environment |  | HSQLDB and in-mem ApacheDS for UIB |
| Production installation using Docker (one image per application) | Production setup |  | Basic setup is ready, but must use data volume containers, so few advantages so far over ansible based installation. Do every application need a data volume container? Need to select a SDN strategy/framework for elastic wiring of the modules on a set of dockerhosts |

---

#### Development setups

| What | Purpose | Status | Comment |
| --- | --- | --- | --- |
| [Developer quick-start](https://github.com/Cantara/Whydah/tree/master/dev-quickstart) | Bootstrapping a full development environment |  | [getSource.sh](https://github.com/Cantara/Whydah/blob/master/getSource.sh)   [buildFullWhydah.sh](https://github.com/Cantara/Whydah/blob/master/buildFullWhydah.sh)   [pullRebaseFullWhydah.sh](https://github.com/Cantara/Whydah/blob/master/pullRebaseFullWhydah.sh)   [startFullWhydah.sh](https://github.com/Cantara/Whydah/blob/master/startFullWhydah.sh) |
| Integration environment on developer laptop using java -jar | allow basic integration testing during development |  | can also run in IDE |
| Integration environment on developer laptop using Docker (one image per application) |  |  | Basic setup is ready, but not sure if this setup gives any advantage over java -jar and IDE alternatives. |
| Run one application with stubbed external dependencies | Simplify development |  | Not sure if the mocks/stubs parts still work or are still useful. |

---

#### Configuration tags

- **Production**
  - UIB: no tags, *useridentitybackend\_override.properties* file in same folder as jar file
  - UAS: no tags, *useradminservice\_override.properties* file in same folder as jar file
  - STS: -DIAM\_MODE=PROD -Dhazelcast.config=hazelcast.xml -DIAM\_CONFIG=/home/sts/securitytokenservice.PROD.properties
  - SSOLoginWebApp: -DIAM\_MODE=PROD -DIAM\_CONFIG=/home/ssologin/ssologinservice.PROD.properties

- **Devtest**
  - UIB: -DCONSTRETTO\_TAGS=dev, *useridentitybackend\_override.properties* file in same folder as jar file
  - UAS: -DCONSTRETTO\_TAGS=dev, *useradminservice\_override.properties* file in same folder as jar file
  - STS: -DIAM\_MODE=PROD -Dhazelcast.config=hazelcast.xml -DIAM\_CONFIG=/home/sts/securitytokenservice.PROD.properties
  - SSOLoginWebApp: -DIAM\_MODE=PROD -DIAM\_CONFIG=/home/ssologin/ssologinservice.PROD.properties

All applications has flexible configuration options to support the many variants described above.   
As a general principle the default configuration should have production settings and not development settings.   
This means for example testpage=disabled and sslverification=enabled. However, since the actual domain names, ports and TLS certificates will be different from environment to environment, the default configuration use http, default ports and some popular options like email and hazelcast for high availability are disabled. The config override file for each application should be used to turn on and off the different options.

###### UIB

| Tag | What |
| --- | --- |
| dev | embedded HSQLDB, embedded ApacheDS, delete and import testdata |
| noSecurityFilter | disable SecurityFilter |

To enable dev mode, set VM options:

Unknown macro: {code}

-DCONSTRETTO\_TAGS=dev

Configuration use <http://constretto.github.io/>.

###### UAS

| Tag | What |
| --- | --- |
| dev | sslverification=disabled |

To enable dev mode, set VM options:

Unknown macro: {code}

-DCONSTRETTO\_TAGS=dev

Configuration use <http://constretto.github.io/>.

###### STS

Configuration use [AppConfig.java](https://github.com/Cantara/Whydah-SecurityTokenService/blob/master/src/main/java/net/whydah/token/config/AppConfig.java)

Currently DEV, TEST, TEST\_LOCALHOST and PROD.

|  | New configuration tag strategy - not implemented yet |

If we set default config to work on localhost, testpage=disabled and sslverification=enabled, then we only need a single tag for *dev*.   
Suggest to switch to constretto.

Should be:

| Tag | What |
| --- | --- |
| dev | testpage=enabled, sslverification=disabled |
| ha | properties for hazelcast |

###### SSOLoginWebapp

Configuration use [AppConfig.java](https://github.com/Cantara/Whydah-SSOLoginWebApp/blob/master/src/main/java/net/whydah/sso/config/AppConfig.java), suggest to switch to constretto.

Currently DEV, TEST, TEST\_LOCALHOST and PROD.   
If we set default config to work on localhost, testpage=disabled, sslverification=enabled and signupEnabled=false, then we only need a single tag for *dev*.

Should be:

| Tag | What |
| --- | --- |
| dev | testpage=enabled, sslverification=disabled, signupEnabled=true |

TODO:   
Add examples for how to configure multiple login alternatives.
