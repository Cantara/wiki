# Replicated database

This pattern has many similarities with the [Synchronized database](/web/20090930020615/http://wiki.cantara.no/display/ARS/Synchronized+database "Synchronized database") pattern.

## Problem/Context

## Solution

Create migration scripts that at regular intervals retrieve data from the existing database and populate the new database. Any changes to the new database will be lost at this point in time.

The pattern is a good place to start, as it provides very little risk. As the project progresses, it might become necessary to evolve into a [Synchronized database](/web/20090930020615/http://wiki.cantara.no/display/ARS/Synchronized+database "Synchronized database") strategy instead.

## Strengths

- reduced [MDE](/web/20090930020615/http://wiki.cantara.no/display/ARS/MDE "MDE")
- no risk of corrupting existing production data
- the replication scripts will become the migration scripts when the new database is first put into production. With this approach, the migration script will be well tested before you come to depend on it
- the new database can be on a different platform and have a different structure than existing db.

## Weaknesses

- one can only release functionality that doesn't modify the replicated parts of the new database
- risks exposing confidential data to unauthorized users

## Examples
