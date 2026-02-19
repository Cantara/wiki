# Security

### Introduction

We strive very hard to make Whydah a very secure collection of software services. We do regular penetration tests against Whydah installations, and use tools like the OWASP security suite automatically in our continuous integration setup. We invite all to do penetration tests and code reviews to help us ensure that the software stay on top of the ever more fast-moving security race.

### The mile high perspective of the software stack security

**DOS/DDOS attack**

- Low risk - the Whydah stack is continously running tough load-test to observe any instabilities to high-load attacks. We do have one feature which by its design is somewhat prone to DoS attack, and that is the request new password process. The consequence is that attackers might succeed in blocking a user from initiating a new session. Existing user sessions will not be affected. **Consequence: low**

**Injection (xss/javascript/sql/ldap/json/xml)**

- Low risk - We know of no such issues. And by leveraging polyglot persistence strategies on two levels, it is very unlikely that attackers will succeed on this kind of attack vectors. We are continuously running modern penetration tests to verify this claim. **Consequence: low**

**Backdoors**

- Low risk - as open source, the customer are free to read all the source-code and build their own components.

### Some key security mechanisms Whydah provide which you will not find at most other alternatives

- ApplicationAuthentication
- SecurityLevel in the UserTokens
- Threat level (DEFCON) awareness

**ApplicationAuthentication**

Only authenticated applications are allowed to gain any access of the data from Whydah. The application have active sessions against Whydah, which can be terminated at any point, actively blocking ill-behaved or compromised applications to gain data and access further into your systems. The application-authentication scheme is planned to be expanded in future releases with rolling and upgrading security mechanisms run-time.

**SecurityLevel**

The Whydah [UserToken](/web/20210624224255/https://wiki.cantara.no/display/whydah/UserToken "UserToken") exposes the level of thrust the Whydah system has in the user authentication. (Level 0-5) For sensitive applications, you will in future releases be able to indicate the minimum level of thrust needed, and thus force the user to upgrade hes/her authentication with additional data like 2-factor authentication, Bank-system authentication, code chips, bio-metrics and more.

**ThreatLevel**

From Whydah 2.0, we have started to implement a built-in security awareness inspired from the military [DEFCON](/web/20210624224255/https://wiki.cantara.no/display/whydah/DEFCON+-+System+threat+mechanisms "DEFCON - System threat mechanisms") method. At normal operations (level 5) Whydah operates normally, but if the system is under attack or compromised we plan to limit the ability to create or continue user and application sessions, and we are discussing wether and how to limit data loss by i.e. invalidating all password, wiping user token values. On less threat levels, we plan start spoofing attackers by supplying confusing header data and actively collecting forensic data of the attack.
