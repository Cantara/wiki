# Environment versioning

A **baseline** is a set of **software services with fixed versions** and their **configuration** in a known **Operating System environment** on known **hardware**.

In other words;

- [Software versioning](http://www.reference.com/search?r=13&q=Versioning)  can be implemented with maven-release-plugin
- Configuration versioning
- known Operation System environment is achieved by
  - controlled access to privileged operations (minimize root-access)
  - have documentation/script for setting up a basic system
  - have documentation/script that explains the changes from the basic system to the setup needed by the application

When the above is in place we have a known **baseline**. Each axis/dimension can be changed in isolation, but we shouldn't "accept" a new baseline without evaluating if the new baseline is better 1 than the previous one.

1 Better is determined by an comparison of new and old baseline according to a chosen set of drivers.
