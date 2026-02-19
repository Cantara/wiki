# Security requirements for distributed systems

1. All network communication must be encrypted. (Loopback is excluded.)
2. Authenticate and authorize user.
3. Authenticate and authorize application.
4. Audit logging for everything money related or dangerous.
5. Applications run without root/administrator privileges.
6. Firewalls/security groups are nice, but can never be the only protection.
7. Use principle of *need-to-know* for data access. I.e. applications shall not have access to data they don't need.
8. Use several levels of security. Users can be compromised. Applications can be compromised. Users make mistakes. Developers make mistakes. Operations make mistakes. You get the point.
