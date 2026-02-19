# New business

## Problem/Context

In a [Replacement project](/web/20090930020713/http://wiki.cantara.no/display/ARS/Replacement+project "Replacement project") or [Enhancement project](/web/20090930020713/http://wiki.cantara.no/display/ARS/Enhancement+project "Enhancement project") the existing system has a steady stream of new business.

## Solution

Develop enough features in the new system to support new business of the simplest type. Add a gateway that directs new business of the appropriate type to the new system. This pattern can be used together with the [Synchronized database](/web/20090930020713/http://wiki.cantara.no/display/ARS/Synchronized+database "Synchronized database") or [Replicated database](/web/20090930020713/http://wiki.cantara.no/display/ARS/Replicated+database "Replicated database") patterns in order to make base data available to the new system.

## Strengths

- Greatly reduced [MDE](/web/20090930020713/http://wiki.cantara.no/display/ARS/MDE "MDE") in some situations
- Migration of data is postponed and possibly reduced since the new system can operate more or less independently of the old system.

## Weaknesses

- If there are strong interdependencies between new business and existing business it will be difficult to achieve a real reduction in [MDE](/web/20090930020713/http://wiki.cantara.no/display/ARS/MDE "MDE") with this pattern.

## Examples

- An internet shop could funnel purchases that are to be invoiced to the new system while letting the existing system handle credit card purchases.

- This pattern was evaluated in the [Book club system](/web/20090930020713/http://wiki.cantara.no/display/ARS/Book+club+system "Book club system").
