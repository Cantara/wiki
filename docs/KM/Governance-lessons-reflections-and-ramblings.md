# Governance - lessons, reflections and ramblings

### Executive summary

Governance has been on top of Gartners Hype-Cycle for some time now, and people still seem very confused on the topic.
This is why I'll try to explain some of my experiences and thoughts on the subject... ([Why should I care about Governance](Why<sub>~should</sub><sub>I</sub><sub>care</sub>~about-Governance.md))

**Governance 911 - warm-up**

- we fail in most attempts to govern IT projects
- the most certain fact in IT projects is that we do not know enough
- we need the right size and complexity of our pawns 
- governance is not a technical challenge, it is mainly people and organization

The main reasons for failure in IT Governance projects can be put into two simple categories: a) [Cover your own ass](Cover<sub>~Your</sub><sub>Ass</sub><sub>Governance.md)  b) The idea of control via processes in IT projects. The first is a well known strategy, while the latter might need som explanation. As most organization processes fail to include "the fourth estate, aka people via media" we usually do not get feedback when the rules fail to meet the expectations of the people. What we see happen then is that the projects in an ever</sub>~increasing degree work against and around the rules resulting in the idea of the rule being in-place/followed when it is actually completely ignored or bypassed.  

**So what does this mean..**
    
- decisions have consequences, make sure to keep the feedback loop active and open    
- the only thing we know for sure is that we do not know... work and plan with it, not against it
- never expect less failures than others, plan for more, and build learning and knowledge from failure

### We know only one thing -> "We do not know it all, yet"

- Plan and embrace this fact, you need to learn.
- Try and fail - and embrace failure. That's very important in learning.
- Keep predictions of future failings. Ensure that they fail early rather than later.

The key point here is to plan for things to fail. This is how you can control the consequences, and keep the cost of failures low. We know from experience that we do not know everything. By failing to embrace this fact you are only prolonging the time before failure. Then the cost will increase exponentially, and you effectively prevent learning. Since failure is so expensive, we move from a positive and embraced learning experience to a cover your ass blame-game.

> 💡 How many times have you not seen a new feature request, estimated to 16 hours of work run through a change-process which costs 5+ days of work. Most times it would be way better and cheaper and self learning to just implement the feature and potentially kill it if it was a failure.

**Ensure that you never break the feedback-circle**

> 💡 * Empower and lead
> 💡 * Build a [learning culture and organization](http://wiki.cantara.no/display/KM/Thou+shalt+strive+to+build+a+learning+organization+and+culture)

### What to govern

**Bigger pieces is more difficult to handle**
- [clear and consistent responsibility power all great architectures](../architecture/Clear<sub>~and</sub><sub>consistent</sub><sub>responsibility</sub><sub>power</sub><sub>all</sub>~great-architectures.md)
- [skyscrapers do not scale](http://97<sub>~things.near</sub><sub>time.net/wiki/talk</sub><sub>about</sub><sub>the</sub><sub>arch</sub><sub>but</sub><sub>see</sub><sub>the</sub><sub>scaffolding</sub>~beneath-it)
- smaller pieces are easier extended/exchanged

**Good candidates for governance**
- business data/object and data hierarchies
    - responsible data-owner is vital
    - always measure value/[KPI](KPI.md)/correctness
        - you really, really do not want split ownership?
- contexts (legal boundaries/dept boundaries/product boundaries/channel boundaries)
    - [responsible owner is vital](responsible<sub>~owner</sub>~is-vital.md)
    - keep a sharp eye on the mappings
    - always measure value proposition/[KPI](KPI.md)/correctness
        - is this context creating real value? if not, kill it!
- domain group of activities/function/services  
    - owner
    - value/[KPI](KPI.md)/correctness

**Decide how you will measure value up-front** 
- never start any projects without measurable KPI implemented
- if measurement is too expensive, you are using the wrong "hammer"/tool

> 📝 A special focus is needed from a governance to the following challenges
> 📝 * decision processes (see [how to make better decisions](http://wiki.cantara.no/download/attachments/394270/goOpen4.pdf))
> 📝 * [silver bullets](http://wiki.cantara.no/display/KM/Thou+shalt+never+default+to+silver+bullets+or+magic)
> 📝 * defenses of earlier investments
> 📝 * technology upgrades/[technology hypes](technology-hypes.md)

**The hard thing to govern is the non-technical side**
- products/product life cycle
- market hype
- sales hypes
- strategic argumentation
    - No implementable KPI/value gauges - no project
    - revisit the values created, and kill "bad products"
    - only one "forced" initiative from each department at anyone time. And failed initiatives must be removed before any new initiative from that department is started

### Balance of power....

If technology is vital to your business, so is the decision of the chief architect
- do you let the hosting contractor dictate the platform, but ignore your own chief architect?
- for every time the chief architect is shortcut, your technical, architectural and training debt doubles..
    - can you afford that?

[a small note on Governance and cost..](a<sub>~small</sub><sub>note</sub><sub>on</sub><sub>Governance</sub><sub>and</sub>~cost.md)

### End note

**Governance is an organization challenge, if you can't govern, you probably have a non-optimal organization. It might be smart to see if you can help yourself by reorganizing...**

- divide & conquer
- sub-service providers (as departments)...  easier to extend, remove, offshore, outsource
- make sure that you ALWAYS kill products/offerings which has negative value
    - they will drag the rest of the company with you

### Contributors
- [Totto](http://wiki.cantara.no/pages/viewpage.action?pageId=393226) - initial author
- [Stein Grimstad](http://wiki.cantara.no/display/~steingr@simula.no), Simula
- [Andre Wiik](http://wiki.cantara.no/display/~awiik/Home), WebStep
- [Erik Drolshammer](http://wiki.cantara.no/display/~sherriff/Home), Objectware
- [Bård Lind](http://wiki.cantara.no/display/~baard.lind/Home), Objectware/Telenor Mobil
