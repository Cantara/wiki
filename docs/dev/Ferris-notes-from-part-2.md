# Ferris' notes from part 2

Neo4J

Emil talks about semantic web, web 2.0. Graphs of information. RDF.

The problem of relational database. oesn't scale with information complexity. Sparse tables, and increasing number joins.

So the solution is a graph database.

Instead of having relationships as properties, it's an explicit part of the model. BECAUSE the relationships can have properties as well! That's very important for the model to work.

Only primitives can be stored. Just like in JCR.

Alot like the JCR except the relationship. Emil says exactly what I suspected, the JCR will have performance issues, which is what they experienced in infoq.

Traversal.

I really like the API!

Johannes points at a thread-safety issue in the traversal. Emil is aware of this, and Johannes is the first guy who's ever pointed this out :)

They don't support any query languages like SQL or XPath. But they do support sparql (RDF query languge.

But still, very primitive stuff.  

Transcations. It's designed for short-lived transactions. It's not a big problem for us OpenSessionInView people, but could be very handy. For long lived transaction you would probably use Qi4J UnitOfWork stuff.

Export/import: They have RDF features.

Lots of interesting thoughts about distributed storage. Not easy, but good principles. CAP theorem. 

Quick discussion on licenses... Interesting.

Neo4J will be the most kick-ass persistance strategy for Qi4J. They use an "Apache friendly" license. 

=====

Totto's presentation.

Now we have to participate!

We're going to get some results.

We've all joined a cruise about Enterprise POJOs.

Does anyone know what it is?
 * Enterprise java beans :)
 * A contradiction in terms
 * More suggestions.
 
Truth be told, it's a term defined for this cruise. It doesn't exist in the litterature. You have to define it for yourself.
 
There are several reasons why Totto is presenting this term.  

First we have to clarify a few things within the group, looking at the discussion.

The term is very imprecice.

What are the characteristics with what we define an Enterprise POJO, and how can we find a common viewpoint (in the next half-hour)?

First: Define enterprise!

It's a noun. Enterprise application.

 * Johannes: Commercial, business
 * Emil: Uptime
 * Michael: Maintainability
 * Does it mean important? 
 * Johannes: We're talking about business critical. 
 * Erik: Long-lived, sustainable
 * Cheap? Expensive? :)
 * Johannes: Often re-incarnated. Legacy systems.
 * Ferris: lots of dependees
 
Totto: Do they really do this stuff?

Rickard: There's a big difference between what these applications should do, and what they actually do today.

Totto: Big difference between needs and reality.

Kaare: An application has to suit some needs. The enterprise application has to suit needs for suits.

Johannes: The user is not the customer. People who pay for the system are not the same people as the ones who will use the system. And often they get it wrong.

The real user is not taken into account.

Why do enterprise applications end up being a problem?

Kaare & Rickard: It's a methodology problem. 

Kaare: Why do we create crappy software between 9 and 17.

Could it be because we're not responsible/accountable.

Michael: Responsibility diffusion. Too many people, responsibility disappears.

Rickard: Too many people working on a project. 

Ferris: Why is there so many people working?

Rickard: Cause they're working with RDBS'es :D

Kaare: They can't be fired :)

Johannes: It's easier to kill them in Norway :)

**Totto's summary**

- Unclear / split ownership 
 ** responsibility of 
 ** too many people
- Lots of dependees/re-invention
- Interact (?) of legacy systems
- Business critical

Erik: The goals of enterprise applications. Kaare says the goal aren't clear. The enterpise vs the normal POJO discussion is not interesting on this geek cruise.

Long discussion on what enterprise follows. 

Some of these are so critical that we can't mess around anymore. Some people work on places like nuclear power plants. 

Kaare: Enterprise applications are where money is involved.

Johannes: Cockburn ususally segregates critically into different layers. But risk of life is beyond that.

Totto: OK, what do these systems need to be like to surprise in the enterprise?

Michael: References Book Review: Implementation Patterns on InfoQ

1. Understandability
1. Simplicity
1. Flexitibily

So, what defines these things again?

We should not add complexity to the problem!

Why not spend more time increasing skill?

Easy to learn and easy to use.

Ferris: We tried to lower the complexity of AOP by introducing Qi4J. 
Rickard: Yeah, that's true.

Totto: We have seen this for a long time. With Java and JEE.

Johannes: The decoupling we're talking about with this kind of programming is harder for alot of people. We should rather do duplication than fragmentation. Undestandability. Give us enough information so we can see what's going on.

Totto: Save re-use for tomorrow.

For whom complex tools 
Michael: Know your audiences. The humans after you are your audience

Erik: Belives that some of the understandibility can be solved with encapsulation. Use the magicHappensHere.

Kaare disagrees. If you're looking at a big tree it will have lots of subtrees. Navigating around that when you have a bug is terrible.

Is Qi4J debuggable? Yup.

**Simplicity**

Should do what I expect it to do. 

Rickard: If you have an object composed of a 100 pieces. Each piece is super simpel, but that does not mean the object is simple.

OC: We max at 7 items. Preferably fewer.

Johannes talks alot about different stuff, but I fell off.

Totto: I've done alot of Smalltalk, but lack of tools.

We all talk about that we will get these tools, but we never get them.

Sergej: Abstraction is a tricky thing. It makes it simpler to see what happens at a higher level. The same with Qi4J and what Uncle Bob says. The problem first arises when you want to find out what are going on in the details. You want both abstractions and details.

Michael: Put complexity in one place?.. (didn't get it all)

Johannes: how to avoid the gigantic interceptor/mixin?

Kaare: This is my problem: You can't tell programmers what to do.

Totto: Talks about how it was to get a team developer doing JavaSpaces...

Discussion ensues! Too much beer and talk to follow discussion :)
