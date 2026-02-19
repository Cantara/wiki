# Partition the workflow

This pattern is usually used in combination with the [Workflow by workflow](Workflow-by-workflow.md) pattern. The [New orders](New-orders.md) pattern is also often relevant.

## Problem/Context
The system being built contains one or more important workflows. A special case of this pattern is when the workflow plays out over a long time frame making it possible for releases to follow the workflow from start to finish.

## Solution
Develop features that support one of the steps in one workflow. Expand to other steps in subsequent releases. 

## Strengths
- Greatly reduced [MRP](MRP.md)
- Relatively easy for users to deduce which system a particular workflow item is being handled by.
- If a follow the workflow approach is used features are developed in a just in time manner.

## Weaknesses
- Integration between new and old system can be tricky.
- Release dates tend to harden with a follow the workflow approach. Once the first release is in production subsequent releases must keep pace with the workflow. 

## Examples
Systems that handle applications for funding (research applications, grants, scholarships). See the  [Research application system](Research-application-system.md) case study.
