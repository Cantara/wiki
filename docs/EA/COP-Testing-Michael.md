# COP Testing (Michael)

Replace existing Mixin implementations with Stubs or Mocks (of existing MockingFrameworks) when testing QI4J modules and applications.

- Use the existing metaInfo facilities
- use ServiceDeclaration.providedBy to provide a alternative configured ServiceFactoryInstance
- use a MockAssembl delegating to a normal Assembler but being able to be configured to return alternative implementations for Mixins, Concerns, SideEffects
