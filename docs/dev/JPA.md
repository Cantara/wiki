# JPA

# Schemas

Using a schema different than the users default schema should be avoided (especially if the schema is not a constant), since configuring different schemas in JPA can be tricky. However, in some scenarios JPA must take Schemas into consideration. When using schemas to seperate between different configurations, we must be able to set the schema outside the @Table annotation.

There exists several possible solutions to the problem.

1. Configure the JDBC connection to use a specified schema TODO: examples of how to do so with differenct databases

2. Using environment spesific orm.xml files with different default schemas

3. Adding a property to the JPA-implementation. For OpenJPA, a property named openjpa.jdbc.Schema can be set.
