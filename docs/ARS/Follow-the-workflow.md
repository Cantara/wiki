# Follow the workflow - Cantara Community Wiki

It is usually used in combination with the [Workflow by workflow](/web/20090930021907/http://wiki.cantara.no/display/ARS/Workflow+by+workflow "Workflow by workflow") and the [New business](/web/20090930021907/http://wiki.cantara.no/display/ARS/New+business "New business") patterns.

## Problem/Context

The system being built contains a workflow that has a very long duration.

## Solution

Develop features that support the first steps in one workflow. Expand to later steps in subsequent releases.

## Strengths

- Greatly reduced [MDE](/web/20090930021907/http://wiki.cantara.no/display/ARS/MDE "MDE")
- Features are developed in a just in time manner which gives immediate feedback.

## Weaknesses

- Release dates tend to harden. Once the first release is in production subsequent releases must keep pace with the workflow.

## Examples

Systems that handle applications for funding (research applications, grants, scholarships).
