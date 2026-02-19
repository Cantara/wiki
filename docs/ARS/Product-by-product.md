# Product by product

## Problem/Context

In a [Replacement project](/web/20210127094843/https://wiki.cantara.no/display/ARS/Replacement+project "Replacement project") or [Enhancement project](/web/20210127094843/https://wiki.cantara.no/display/ARS/Enhancement+project "Enhancement project") where the existing system handles products of different types.

## Solution

Create enough features in the first release to make it possible to migrate one product from the existing system to the new one. Later releases then grow the number of products that can be migrated.

## Strengths

- If there is a large variation in features that are needed for different products this pattern reduces [MRP](/web/20210127094843/https://wiki.cantara.no/display/ARS/MRP "MRP") significantly
- Internal users will often be organized around products. That makes it easier to achieve a situation where few users have to work with both systems in parallel.

## Weaknesses

- This pattern does not work well if there are strong interdependencies between products. This is the case if one customer typically interacts with products of more than one type
- Users will be annoyed if they have to look for a product in both systems. This can be mitigated by using the [Umbrella](/web/20210127094843/https://wiki.cantara.no/display/ARS/Umbrella "Umbrella") pattern or the [Facilitate switching](/web/20210127094843/https://wiki.cantara.no/display/ARS/Facilitate+switching "Facilitate switching") principle.
- If migration of one product is complex, [MRP](/web/20210127094843/https://wiki.cantara.no/display/ARS/MRP "MRP") can become too large.

## Examples

- In a [Book club system](/web/20210127094843/https://wiki.cantara.no/display/ARS/Book+club+system "Book club system") one product is a particular type of book club.
- In an insurance system every type of insurance is one product.
- In a [Research application system](/web/20210127094843/https://wiki.cantara.no/display/ARS/Research+application+system "Research application system") one type of research application is a product
