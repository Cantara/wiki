# Observation from OC

A question that constantly swirls in my mind is "Does Qi4j simplify DDD - or does it introduce too much WTF?". You have to battle alot to implement DDD in Java. Whereas static typing is nice, and tool support important, I do not find Java to be a very purposeful language for implementing this kind of "dynamic programming". By design it does not support multiple inheritance and I find the exploded pattern for circumventing this I find hard to grasp.

The complexity in Qi4j _is_ high no matter how you put it - but i find most of the problem to be syntactical limitations of java (diamond-inheritance-related). IMHO Ruby, Groovy or even Duby would all be better fits for implementing the glue for _composites_ -- the dynamic objects (constraints, fragments, etc). However; I find Qi4j's deterministic (typing) architecture very purposeful for gluing together the composites in the application (across the module- and layer-abstractions). Is it possible to consider a combination of languages rather than doing it all in Java?

So in my mind the conceptual implementation is the most interesting.

Another aspect of Qi4j I find interesting to learn more about is it's testability. I would like to know more about how Qi4j can support mocking of layers, services, modules, as well as testing of _context-aware_ composites.
