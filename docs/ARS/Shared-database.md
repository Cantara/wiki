# Shared database

|  |  |
| --- | --- |
| [Full Size](/web/20090930020625/http://wiki.cantara.no/spaces/gliffy/viewlargediagram.action?name=SharedDatabase&ceoid=3146872&key=ARS&pageId=3146872)  |  | |

This pattern is unique in that it combines very powerful strengths and weaknesses. In many contexts the weaknesses will outweigh the strengths so make a thorough analysis before using a shared database. This pattern is similar to the [Synchronized database](/web/20090930020625/http://wiki.cantara.no/display/ARS/Synchronized+database "Synchronized database") pattern.

## Problem/Context\*

A [replacement](/web/20090930020625/http://wiki.cantara.no/display/ARS/Replacement+project "Replacement project") or [Enhancement project](/web/20090930020625/http://wiki.cantara.no/display/ARS/Enhancement+project "Enhancement project") where the existing system is based around a database. The database typically contains large amounts of data. The project wants to minimize the [MDE](/web/20090930020625/http://wiki.cantara.no/display/ARS/MDE "MDE") of the first release. Examples of systems where this pattern can be considered are administrative applications of many types (banking, insurance, application processing).

## Solution

Use the existing database as the base for both the existing and the new system. The new system writes to the database in such a way as to not break the existing system. Over time more and more features are added to the new system while parts of the existing system are phased out. The database can be augmented with new tables and in some cases with new columns on existing tables. Depending on the task being performed users will interact with the existing or the new system. Once the new system is complete the existing system is terminated.

## Strengths

- The primary gain with this pattern is that [MDE](/web/20090930020625/http://wiki.cantara.no/display/ARS/MDE "MDE") is dramatically reduced.
- new features early
- partial replacement possible
- no migration

## Weaknesses

- The most obvious drawback of this pattern is that you have to accept the existing database design and platform. You can add new tables (and in some cases columns) but you cannot change anything until the legacy system is retired. By that time the new system will have grown to the point where it will be difficult to make major changes to the database.
- Difficult to make fundamental process changes
- Even if the structure of the existing database is reasonably good, the documentation often is not. It can be very resource consuming to figure out all the implicit rules that the legacy system has in its interaction with the database. See the [CustomerAddress](#Shareddatabase-CustomerAddress) example below.
- Testing will also be much more complicated since you need to test both systems. The existing system probably does not have automated tests or even an updated set of manual tests
- There is also the risk that the database has corrupt data. This can add greatly to the complexity of the project.
- On a different level some user sets may be forced to split their work on two systems. This can be very confusing and lead to errors.
- It can be difficult to phase out parts of the old system leading to redundant functionality

## Examples

This pattern was used successfully in the [Research application system](/web/20090930020625/http://wiki.cantara.no/display/ARS/Research+application+system "Research application system").

### Customer/Address example of hidden semantics

In a legacy business application the database stored information about customers in a Customer table and an Address table. Each Address stored the id of the corresponding Customer (foreign key in database terminology). When the new application created a new Customer and Address by adding these to the database the legacy system was not able to read the customer. The reason the legacy system failed was that it required every Customer to have exactly two Address records even if only one was used. This kind of rule will seldom be documented in a database. In proactice the only way to find these rules is by trial and error.
