# Product by product

## Problem/Context

In a [Replacement project](/web/20090930020728/http://wiki.cantara.no/display/ARS/Replacement+project "Replacement project") or [Enhancement project](/web/20090930020728/http://wiki.cantara.no/display/ARS/Enhancement+project "Enhancement project") where the existing system handles products of different types.

## Solution

Create enough features in the first release to make it possible to migrate one product from the existing system to the new one.

## Strengths

- If there is a large variation in features that are needed for different products this pattern reduces [MDE](/web/20090930020728/http://wiki.cantara.no/display/ARS/MDE "MDE") significantly
- Internal users will often be organized around products. That makes it easier to achieve a situation where few users have to work with both systems in parallel.

## Weaknesses

- This pattern does not work well if there are strong interdependencies between products. This is the case if one customer typically interacts with products of more than one type

## Examples

- In a book club system one product is a particular type of book club.
- In an insurance system every type of insurance is one product.
- In a research application system one type of research program is a product
