# Environment

The environment of web applications is a crucial factor when considering security. It wouldn't help much to create an application with all available security measures made with best practices, using top security consultants if the application was deployed on an application container with known exploitable weaknesses or a vulnerable OS. In both cases the attacker would attack the environment and get complete control without the time consuming task of penetrating the web application.

## What can be done about the environment?

- First of all, keep software updated, and make sure it is automated (or else it will not be done).
- Make sure you use the principle of least privilege when defining access for containers and datasources. (E.g. Web server runs in unprivileged user mode, deny access to everything, then give access to what should be accessable, etc.)
TODO: More typical ways of hardening the environment.
