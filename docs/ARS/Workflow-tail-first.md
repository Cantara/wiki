# Workflow tail first

This is a variant of the [Follow the workflow](/web/20090930074340/http://wiki.cantara.no/display/ARS/Follow+the+workflow "Follow the workflow") pattern.

## Problem/Context

The system being built contains a central workflow.

## Solution

Develop features that support the last steps in the workflow. When tasks in the existing system reach the last steps of the workflow they are migrated to the new system. Expand the new system to earlier steps of the workflow in subsequent releases.

## Strengths

- Greatly reduced [MDE](/web/20090930074340/http://wiki.cantara.no/display/ARS/MDE "MDE")

## Weaknesses

- Migration can become expensive since it may have to be modified in every release.

## Examples
