# Workflow by workflow

## Problem/Context

The system being built contains more than one workflow.

## Solution

Identify and implement one workflow. Users will start to use the system when performing this workflow. This pattern can sometimes be used together with the [Follow the workflow](/web/20090930020641/http://wiki.cantara.no/display/ARS/Follow+the+workflow "Follow the workflow") pattern.

## Strengths

- If the workflow that is developed first is relatively simple the [MDE](/web/20090930020641/http://wiki.cantara.no/display/ARS/MDE "MDE") is reduced.

## Weaknesses

- A complex workflow will lead to a oversized [MDE](/web/20090930020641/http://wiki.cantara.no/display/ARS/MDE "MDE") if this pattern is not combined with other patterns.
- If there are strong interdependencies between workflows this pattern risks adding complexity to the project
