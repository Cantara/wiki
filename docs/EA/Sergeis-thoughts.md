# Sergeis thoughts

Concerns in Qi4j apply to specific scopes which are defined by means of annotations. If I want to change scope for a concern I have to change my Java code and redefine annotations hierarchies and/or to apply concern annotations at different places. It seams to me that this approach is more intrusive/challenging then modifying a pointcut expression in a AOP system. AOP is much more flexible in how it allows to insert concerns.

I totally agree that domain specific concerns should be expressed with annotations as much as possible and I've talked about this in my presentation 'Domain Driven pointcut design'. When it comes to infrastructure concerns (I hate mentioning logging) it might be a better idea not to use annotations and to have more granular control such as specific type names, package names, etc.

It was stressed several times that a Qi4j concern is not necessary crosscutting. Who said that AOP concern has to be it?
