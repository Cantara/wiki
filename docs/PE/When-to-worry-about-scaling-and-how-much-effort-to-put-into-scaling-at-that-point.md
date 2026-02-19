# When to worry about scaling and how much effort to put into scaling at that point.

The slides for the talk can be found [here](theme1-pdf.md). Some links for gossip as mentioned in my talk:

[Fighting Fire With Fire: Using Randomized Gossip To Combat Stochastic Scalability Limits](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.5.4000)

[Epidemic Computing at Cornell](http://www.allthingsdistributed.com/historical/archives/000456.html)

### Intro from Dans blog...

**Some notes on areas of software development where obsession with perfection can be costly.**

**Standards** - where everything is standardised, up front so as to avoid unnecessary diversity or cost. Standards like design and code are based on assumptions about the environment in which they will be used. Thus to be sure that a standard is appropriate, one must have experience in the environment. Without the experience, selection or formation of a standard is to a reasonable degree guesswork. Asserting a standard up front often leads organisations into incurring significant costs (e.g. manpower, slow release cycles) as they twist what they do to fit some standard they've selected instead of recognising that the standard is inappropriate for a given situation. Standardisation should be done after a period of diversity/investigation to identify what is or is not applicable.

**Estimates** - where an organisation engages in grand analyses to deliver up accurate estimates for all pieces of work required so that resources can be correctly determined, budgets set and timelines agreed prior to the start of the implementation phase with the assumption that nothing will change. The futility of these efforts can be found in a dictionary:

_"es- ti- mate (st-mt)_

tr.v. es- ti- mat- ed, es- ti- mat- ing, es- ti- mates

#. To calculate approximately (the amount, extent, magnitude, position, or value of something).
#. To form an opinion about; evaluate: "While an author is yet living we estimate his powers by his worst performance" Samuel Johnson.

n. (-mt)

#. The act of evaluating or appraising.
#. A tentative evaluation or rough calculation, as of worth, quantity, or size.
#. A statement of the approximate cost of work to be done, such as a building project or car repairs.
#. A judgment based on one's impressions; an opinion."

Estimates are implicitly guess-work, they can only ever be made accurate in hindsight. Agile is one way to get realistic about estimates.

**Architecture** - where organisations and individuals engage in the illusion that one can design an endlessly flexible architecture that copes with all possible unknown future demands. Just as with estimates, symptoms include grand, long<sub>~running rituals to examine every detail, verify that the architecture is sound and that nothing has been forgotten. Businesses change their processes, unexpected integrations are undertaken, products are dropped and new ones are dreamt up, hosting options change and operational challenges appear unexpectedly. The weapons for dealing with this challenge are not do</sub>~it-all containers or grand architectures, rather they are things like:

    * Principles and guidelines for keeping an architecture adaptable: loose coupling, no broken windows, cohesion and coupling, isolation etc.
    * Validation metrics: to indicate when an architectural assumption has been breached and needs re-addressing.

**Implementation** - where developers engage in the writing of complex, brittle, difficult to maintain and debug code to address challenging problems that can be better dealt with via process or architectural approach. Hot-update of configuration is one such example. At least in the Java world, many a developer will be tempted to tackle this problem with:

    * Clever thread management and barriers to pause work whilst configuration changes are made
    * A remote admin interface to permit lodging of configuration changes
    * Event listeners to respond to the configuration change and patch up various bits of state
    * Sundry bits of classloader magic

From an architectural perspective however, one realises that:

   1. Configuration is most easily done when a process boots, there's minimal state to patch and no active workload to manage.
   2. At least in the case of a website, one must have failure handling mechanisms to cope with lost boxes, broken networks and failing processes.
   3. Hot re-configuration actually means provision of service without disruption to the user.

Thus hot re<sub>~configuration becomes much simpler: kill process, change configuration, re</sub>~start process.

**Hardware** - where expensive kit never fails, making software easier to write but ultimately compromised when it comes to availability as customer usage grows. Hardware does fail, in fact once an organisation accrues enough hardware there will be failures daily and it's not cost-effective to pay for operational staff to run around trying to keep all this hardware running all the time (and it increases the chance of human error, another key contributor to availability problems). In the early days of a system, use of redundant hardware solutions is acceptable it's more important to get things up and running but it pays to:

   #. Monitor service availability.
   #. Track hardware failure patterns.
   #. For each outage, maintain an estimate of cost in both operational and revenue terms.
   #. Track user behaviour after an outage: do they return and if so, how quickly?

These sorts of metrics allow an organisation to determine when to start shifting failure tolerance into the software layers. Marcus and Stern provide a good treatment of systems availability practices.
