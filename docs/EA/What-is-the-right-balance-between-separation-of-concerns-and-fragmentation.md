# What is the right balance between separation of concerns and fragmentation?

When we construct our domain, we want to make sure that things that ought to be kept separate are kept separate. At the same time, splitting logic between different files can make the code harder to understand and make the structure more complex.

From Spring, my experience is that we tend to split up things too much. I'm afraid COP will make it worse (but not as bad as AOP, luckily)

At some level the WTFs/minute approach a critical threshold.
