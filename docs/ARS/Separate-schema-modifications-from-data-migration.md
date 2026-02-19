# Separate schema modifications from data migration

## Problem/Context
A new release includes changes to a database.

## Solution
Script changes to database in three general steps:
1. Schema modifications
1. Data modifications
1. Schema modifications

## Strengths
- By having separate steps for schema modifications and data modifications it becomes much easier to recover from errors. The primary source of errors is typically in the data modification stage.
- Some databases do not support schema modifications as part of transactions.

 
## Weaknesses

## Examples
