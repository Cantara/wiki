# Migrate on demand - Cantara Community Wiki

## Problem/Context

In a [Replacement project](/web/20090930074325/http://wiki.cantara.no/display/ARS/Replacement+project "Replacement project") where the existing system is based on a database. Large amounts of data, but most of it is inactive at any one time. This pattern is easiest to use when the business can accept a delay from the time a record is requested before it becomes available in the new system.

## Solution

Migrate data on a just in time basis. When a record is requested, it (and all related data) is migrated.

## Strengths

- Makes migration an ongoing process instead of a big bang effort

## Weaknesses

## Examples
