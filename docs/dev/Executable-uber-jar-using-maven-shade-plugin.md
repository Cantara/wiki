# Executable uber-jar using maven-shade-plugin

## Executable uber-jar using maven-shade-plugin

## How to solve common cases of overlapping classes

### spring-jcl overlaps with slf4j

To use slf4j instead of spring-jcl when using Spring 4, simply exclude spring-jcl from spring-core's dependencies.
<https://jira.spring.io/browse/SPR-16062>
