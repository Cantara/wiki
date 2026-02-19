# Verify patterns and principles - Cantara Community Wiki

When selecting the principles and patterns that you plan to use in a release you need to verify these carefully.

## Check strengths and weaknesses

Carefully examine the strengths and weaknesses of the patterns being evaluated. Small changes in a project can render a promising pattern useless.

## User groups

When defining a MDE strategy in a project make sure to test it against all user groups. A strategy can look promising until you see that it will not work for one user group.

## Temporal problems

Temporal problems are often missed. A strategy that looks promising can fall apart when you look at what will happen in the weeks and months after the release. As an example, think about a system that has customers making payments based on invoices for products they order. If some of these products are migrated to a new system you will have to handle situations where a customer goes into arrears on a payment in one system. The customer needs to be blocked in both systems or you will risk losing more money on bad customers.
