# Helper code as separate projects

#### [The Cost of reuse versus duplication](The-Cost-of-reuse-versus-duplication.md) 

See [The Cost of reuse versus duplication](The-Cost-of-reuse-versus-duplication.md) for details of how and when to aim for reuse.

#### Enterprise Maven Infrastructure to facilitate reuse 

There will always be overhead with additional projects that have their own release cycles, but this overhead can be minimized with [dev:Enterprise Maven Infrastructure](../dev/Enterprise-Maven-Infrastructure.md). When set up, releasing an extra project is trivial, and working with multiple projects becomes manageable/easy enough. 

The problem with 3 and 4 is that effort is put in _+before+_ we know if it is actually needed. And, worse, if it is not needed at all, we have wasted valuable resources. If we could defer the work we _might_ need until we actually need it done, the last two costs would be minimized. 

So why don't we? As a long as we follow good practices and write maintainable code, we are not forced to do more QA or write the code more generic than we need at the moment. If we _should_ is another matter which will be discussed elsewhere. 

#### What is a helper project? 

We use the term **helper project** to denote code that is non-trivial and which is not part of the primary responsibility of a component. Typical examples are support for transport (JMS, JMX-RPC, Webservice) or storage (SQL, File). The keywords here being _non_trivial_ and _support_. We want to encapsulate such complexity in separate components. Encapsulation makes them easier to write and easier to test. It also makes them easier to reuse, but this is a bonus, because the other benefits alone makes separation worth while. 

Another reason why these helper projects are valuable is that they are a means to centralize functionality. Often the problem is not too _little_ use, but too much. That is, the same functionality is written many, many times, instead of reused. 

TODO: Are descriptions of the responsibilities of such helpers necessary to understand the concept?
