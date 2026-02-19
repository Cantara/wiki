# Synchronized database

|  |  |
| --- | --- |
| [Full Size](/web/20090930074330/http://wiki.cantara.no/spaces/gliffy/viewlargediagram.action?name=SynchronizedDatabase&ceoid=3146905&key=ARS&pageId=3146905)  |  | |

This pattern has many similarities with the [Shared database](/web/20090930074330/http://wiki.cantara.no/display/ARS/Shared+database "Shared database") pattern.

## Problem/Context

## Solution

Set up a new database and use synchronization mechanisms to move data between the existing and new database. The pattern assumes that data in the new database will be migrated back to the existing database. A variation of this pattern only replicates from existing data to new: [Replicated database](/web/20090930074330/http://wiki.cantara.no/display/ARS/Replicated+database "Replicated database"). The synchronized database pattern can be used to synchronize all or just some data between databases.

## Strengths

- reduced [MDE](/web/20090930074330/http://wiki.cantara.no/display/ARS/MDE "MDE")
- new features early
- partial replacement possible
- new database can be on a different platform and have a different structure than existing db.
- less need for migration

## Weaknesses

- can be brittle
- corrupt data
- testing

## Examples
