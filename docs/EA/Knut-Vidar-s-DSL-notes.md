# Knut Vidar's DSL notes

## DSL -- "Raising of abstractions continued"

(There is rarely _one_ ubiquitious language for the problem domain)
(Information is lost in translation)
- DSLs allow for problem expression and sometimes problem solving.
- Problem expression can itself be worth the investment.
- Internal DSLs often introduce sentence-like semantics of language statements and usually executed directly.
- External DSLs usually build a model and reason on the model (powerful)
- Several DSL language features are included in .NET
- Closures will make it easier to create DSLs in Java, which as of now, is cumbersome.
- Clean language support is better. Since Java lacks language support, Qi4J is a work-around. 
What new language features would have helped Qi4j?
Mixins, more reflection capabilities, literal methods would help Qi4j

Is UML a DSL?
Can more easily do modifications on the model. Meta, meta, meta. **What was the answer?**

Problem: no semantics in SQL query strings alone. Enter JEQUEL.

## [JEQUEL](http://jequel.de)
 
- Internal Java DSL
- Code generation from DB schema
- Type safety on table names
- Resource bundles structures translation
- Support deprecation for refactoring purposes
- Find usages of tables/columns in Java code(!)
- Compile-time assertion on schema-Java code mismatch
- Type information available in the query (No illegal comparisons)
- Documentation generation from schema
- Can combine DSL with Java structures such as loops, Classes etc
- Can do rendering to other languages, HQL, JPAQL etc.
- Semantic checking

JEQUEL brings type safety, code completion, documentation for SQL statements in Java.

## Discussion

### Quaree
Project fell asleep early spring 2008

### Specification pattern observations?

### DML
Not in jequel, but would not be a problem.
