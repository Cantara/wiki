# User by user

## Problem/Context

The system has multiple user sets that require different sets of features.

## Solution

Create enough features in a release to support the essential requirements of one user set.

## Strengths

- If there is a large variation in features that are needed for different user sets this pattern reduces [MDE](/web/20090930020653/http://wiki.cantara.no/display/ARS/MDE "MDE") significantly

## Weaknesses

- This pattern does not work well if there are strong interdependencies between user sets.

## Examples

- In an administrative application one release could be focused on the needs of customer support. The release would only contain features that allowed customer support to do look ups of customer data.
