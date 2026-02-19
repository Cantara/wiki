# Multi-module project with inheritance

#### About modularization 

Modularization is about how you structure code. Structure makes it easier to understand and maneuver around in the project and makes it easier for a team to work in parallel. Steps that can be made to modularize are:

1. Grouping of classes, interfaces and packages
    - Easy, underneath the scope of this wiki-page (but still underused - read Effective Java!)
1. Separate packages into their own module
    - Some work, team-members need to made aware of the new module
    - Enforces one-way dependencies and negates circular references
1. Move modules into their own separate project 
    - Removing the module from the reactor will decrease build time
    - Decouples the module entirely so it can be re-used by other projects
    - Requires dedicated release management
    - Snapshot<sub>~dependence will require a separate build</sub>~step and deployment done by CI server
    - Domain classes, message classes/formats and [helpers](../architecture/Helper<sub>~code</sub><sub>as</sub><sub>separate</sub>~projects.md) are good candidates for separate projects. 

#### Module as a modularization concept 

This project type it what most be refer to as a "normal" multi-module Maven project. That is, all modules have the same release cycle and they share configuration from the Parent POM. The relationship between the POMs are thus that the modules are referenced from the parent with the _module_ element AND the modules reference the parent with the _parent_ element. So what is the purpose of this project setup? 

Like any modularization concept the module makes it easier to adhere to the principle of [_high cohesion, low coupling_](http://c2.com/cgi/wiki?CouplingAndCohesion). With Java packages an _import_ is required to use code from another package. With Maven modules it is necessary to explicitly add a dependency to the other module to be able to use code from it, just like a dependency to any other Maven artifact. This makes the coupling between modules explicit, and the build will break if you create circular dependencies. 

A additional - positive - side<sub>~effect is that modules make it easier to identify code blocks that can be reused. Code that should be shared between projects with different release cycles need to be refactoring into a standalone Maven project, and it is easier to set up a separate project if the code is located in a cohesive module. See more reasons in the [FAQ](http://wiki.community.objectware.no/display/smidigtonull/Maven+FAQ#MavenFAQ</sub>~Ireally%2Creallywanttohaveasingleprojectforeverything.Whyisthatabadidea%3F).

> ℹ️ h6. A word of caution
> ℹ️ Be wary of over<sub>~engineering by creating too many modules. Code with good structure is easier to re</sub>~use, but sometimes re-use is not on the agenda (YAGNI). Remember also that trying to enforce larger moves can result in project friction. You should always take into account the culture and skill set of your project team. Educate your team on how and why modularization is done. 

That be said, it is more common to have too few modules than too many. To quote from the guidelines: _When in doubt, separate!_

#### Examples 

- [Build C (plusplus) code for multiple platforms with Maven](Build<sub>~C</sub><sub>plusplus</sub><sub>code</sub><sub>for</sub><sub>multiple</sub><sub>platforms</sub><sub>with</sub>~Maven.md)
