# MRP

## Minimal Releasable Product

A MRP is the smallest set of features that must be developed before a release can be deployed into production. To count as being "deployed to production" the system must be used by at least one user set to perform real tasks within a particular workflow or set of operations.

MRP is similar but not identical to **Minimal Marketable Feature (MMF)** as defined in the book **Software by Numbers**. The primary difference is that while MMF focuses on maximizing the creation of business value over time, MRP is also focused on deployment strategy and feedback. On a meta level the difference between MRP and MMF is in the definition of business value. MMF focuses on the value of developed functionality while MRP takes a broader view and includes the value of early feedback and risk reduction. By reducing the risk of failure, MRP helps assure that real business value is delivered.

There is also a relation between MRP and a **Minimal Viable Product (MVP)**. Both are focused on getting a release deployed as soon as possible. The primary difference is that a Minimal Viable Product is only concerned with the development of completely new products. The idea of MRP originally came from [Replacement project](/web/20210511172737/https://wiki.cantara.no/display/ARS/Replacement+project "Replacement project")s.

### Balancing business value and MRP

A project that is able to release every three months or more often can prioritize solely based on business value. In practice though, many projects find it difficult to release every three months. This is especially true for the first release and even more so for [Replacement project](/web/20210511172737/https://wiki.cantara.no/display/ARS/Replacement+project "Replacement project")s. The [Patterns](/web/20210511172737/https://wiki.cantara.no/display/ARS/Patterns "Patterns") described in this wiki help reduce the length of a release but they do so by reducing the business value of the release. This is the core trade-off that can be very difficult to handle.

The figure below is an illustration of how focus should shift from maximizing business value to reducing release length as a function of the release length of a project. Project A has a relatively short release length while Project B has a very long one. Project B should be working much harder than Project A on reducing release length. Project B should in many cases choose a strategy that provides lower business value if this strategy reduces release length. Project A should try to reduce release length but it should seldom sacrifice business value to achieve this.
