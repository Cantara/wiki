# Ferris' notes to Rickard's talk

Arrived 12:30, in the middle of Rickard's presentation/discussion.

Huge discussion follows.

Mixins/behaviour/roles to add your object:

Examples:
- ACL
- Versionable
- Referancable

...

- Why not use a property and dynamic properties, and bind in behaviour at runtime?

JCR and Topic maps are interesting models, cause they do it this way.

Rickard continous through his presentation, talking about DDD concepts.

Refactoring, 

90% of Rickards application is static, but drop-in plugins.

Mentioned using DSLs for expressing problem domains. RSpec mentioned. Moving on.

Rickard continues with Refactoring.

Explains the old Class => Mixins part.

What about good old composition (over ineritance)? They say the old Composite pattern is hard to get right. 

Disucssion dwelves into code generation. Johannes mentions reflection. Hibernate is uses reflection to get persistance going. Qi4J does the same but is more generic (not only for persistance).

More discussion on the model and code generation. 

Everyone agrees that code generation is possible, and perhaps doable if we keep our fingers out of the generated code. The roundtrip has to work.

Totto stops the discussiom sliding off.

Rickard continues on properties.

Qi4J seperates itself from the too dynamic proxies by being as static as possible.

I asked about why not just stay dynamic. Rickard says you really don't want to be runtime-dynamic.

I want discussion later on Context-Specific Behaviour (like validation).

Big discussion on properties...

Presentation on generic mixins.

It looks kind of tricky so Kaare brings up the old "write your own language".

Rickard: Refactoring needs good tools.

Wouldn't a better language make the requirement go away?

Kaare says he hates Ruby/Rails piles of shit.

Erik mentions libraries. If you're still on the JVM they would still work. But Johannes say the interfaces might not look that nice.

Rickard goes back to saying: These things are faaar fetched already. New language would even alienate the slow-adopters.

We finally go into closures. Totto says that if COP gets successful, it will evolve into its own language. Rickard agrees. Qi4J is just a bridge.

Anders Norås has told me (not direct quote) getting his magic stuff to work in Java requires alot more work than it is in C#.  Would Rickard perfer any feature into Java 7 that would make Qi4J better? Didn't get to discuss that.

Continues on Qi4J. Concerns. Orders. Groups concerns by using Interfaces? 

You can use extensions. 

I'm worried about it will get too complex, and people will mis<sub>~use. Refactoring a concern</sub>~stack will be hard. But we can improve the "Find Usage" 

Ronnie asks: What do we miss from AOP? Like logging? Rickard says: Put the behaviour in the system. Logging would be sub<sub>~system, and then you want a calll</sub>~tracing concern. You would have a my application composite. And add the tracer concern there.

The logging example is funny, Kaare says. Everyone agrees. 

More AOP vs Qi4J discussion.

Qi4J massages the stacktrace and removes the proxies. If it ever there's a bug in it, we'll kill somebody! If the exception thrown is in Qi4J, the stack trace is not manipulated, Rickard says.

A bit more talk on concerns. "Concerns should never depend on eachother", that never possible Rickard says, so we make order really simple. 

It's not possible to remove concern-stacks in. They decided not to go with this because the human brain is not good to think in negatives. Also breaks Liskovs Subst Principle.

Kaare is worried about order and extension. Rickard thinks it's first is 

1. first all the generic concerns
1. infrastructure-concerns
1. domain-concerns. But shouldn't these be first?

Totto says both are wrong. Neither is 100% correct

This needs more thinking. We should go with the 90% case, and have that as a default.

We're still discussing the order. Is this difference in input/output? And using stacks, eating down and up?

What about inheritance of concerns?

We could composite them together into annotations.

Post/pre-conditions.

In WebWork we always create a solid, universal stack that everyone has to comply with. The stack has an in/out principle, and each interceptor has a before/after method with conditions.

Looong discussion on composing concern stacks.

The syntax should change. We'll figure out some great syntax tonight!

SiteVision code: 75% of the code is concerns..

Would be cool to see an example where an existing project is refactored into using Qi4J.

Rickard goes on to describe constraints. Some discussion on conversion and/or validation.

SideEffects.

SideEffects and Concerns can not have any state. If they need to use state they have to cooperate with a Mixin. They are effeciently statics.

Composites..

Entities/Messages, Aggregates, these things are on their way into Qi4J..

UnitOfWork..

Interesting question would be to see how will this absorb into the industry. Both software<sub>~wize and people</sub>~wize.

Dependency injection: Modules. Visibility and scopes decide what gets injected where.

Very nice for us who have been fighting with huge application-contexts. 

We also have layers, where we can define as many as we want.

We specify these things programatically with Assemblers.

And we're through.
