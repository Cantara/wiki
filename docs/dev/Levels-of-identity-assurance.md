# Levels of identity assurance

When using Whydah to log into a secure application or a protected system, one must first be assured that you are really who you say you are before you are granted access (doh..). 
Identity assurance is the process that verifies the identities of computer users.

Using whydah, there are 3 levels of identity assurance. 
The one appropriate for your data should be used when you are attempting to set up access.

### L1 Standard level
Logging into most systems (such as collaboration sites or knowledge systems) would require a standard level of identity assurance.

| Identity source | Implemeted |
| --- | --- |
| Username and password in whydah | (/) |
| From other IdP's (NetIQ, ADFS, FB, Google etc.) | (/) |

### L2 Enhanced Identity Assurance
Logging into certain computer systems which need a higher level of security requires enhanced identity assurance. 
Before allowing you to proceed to these systems, Whydah would require that you use:

| Identity source | Implemeted |
| --- | --- |
| Multi Factor token (i.e. Google Auth) | (x) (Designed) |
| Electronic ID | (x) (Designed) |

for L2, encrypted user tokens are needed, so that a certificate will also need to be established.

### L3 High-Level Identity Assurance
Logging into systems with highly sensitive data requires a high level of identity assurance. 
Before allowing you to proceed to these systems, you must provide secure two-factor authentication:
- Use a hardware identity device (Identity Token), and
- Know of the password for the device.

| Identity source | Implemeted |
| --- | --- |
| BankID | (x) (Designed) |
