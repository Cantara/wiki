# Introducing JigZaw in your organization

#### Introduce this material step by step
You and your fellow developers need time to understand these consepts. 
Experiences we have made sugest to follow an approach something simmilar to this:

#### Phase #0 Introduce basic tools and infrastructure to support automated testing 

- Version Control System 
- Build tool
- Basic unit test framework 

#### Phase #1 Gjøre de enkle tingene først, det er bedre å gjøre litt, putt resten på en liste, og glem det.
- Gameldagse prinsipper, gameldagse verktøy. ref Clean Code.

> ℹ️ **Comment** 
> ℹ️ Phase #1: Introduce principle that all bug fixes require test(s) to be written 
> ℹ️ Gjøre de enkle tingene først, det er bedre å gjøre litt, putt resten på en liste, og glem det.
> ℹ️ Gameldagse prinsipper, gameldagse verktøy. ref Clean Code.
> ℹ️ 
> ℹ️ Apply object<sub>~oriented practice and refactor/restructure code to make the code easier to test. See [Clean Code: A Handbook of Agile Software Craftsmanship](http://www.amazon.com/Clean</sub><sub>Code</sub><sub>Handbook</sub>~Software-Craftsmanship/dp/0132350882). 
> ℹ️ Make a list over problems that are difficult to test and move on. That is accept that not everything related to te bug can be tested by an automated test in this phase. 
> ℹ️ 
> ℹ️ Focus: Single bugs fixed. Root causes not improved.
> ℹ️ 
> ℹ️ **Tools**
> ℹ️ * Continous, iterativ process for improved quality.
> ℹ️ * TODO Screencast/tutorial: From Procedural to Object Oriented functionality, and made testable. 

###### Principles
- Write test whenever functionality is added or modified
- [Maximize value of testing](Maximize<sub>~value</sub>~of-testing.md)
- [Divide and conquer](Divide<sub>~and</sub>~conquer.md)

###### Tools
- Refactor and rewrite towards [Clean code](Clean-code.md)
- Select your IDE with care - must support method Refactoring TODO: Erik D
    - E.g. the _extract method_ support is essential, but works differently in different IDEs. 

#### Phase #2 Regresjonstesting av user-stories.

> ℹ️ «Det som virket før skal fortsatt virke selv om vi gjør endringer.» 

Fokus på vertikal, fokus på user-story. Focus on the simple cases.

- Kundedrevet. Agregering av feil. Denne funksjonen feiler alltid. denne user<sub>~storien er for dårlig testet. Functionallity miss</sub>~behaves. Ustabil... reintroduserer feil.

Focus: Ensure that the service/user story/functionallity works as expected, every time.
Implement regression tests. Nivå " det er dette kunden betaler for ". Se på hva som skal leveres, ikke lete etter bugs.

###### Principles
- [Verify expected behavior instead of looking for bugs](Verify<sub>~expected</sub><sub>behavior</sub><sub>instead</sub><sub>of</sub><sub>looking</sub>~for-bugs.md)
- [Divide and conquer](Divide<sub>~and</sub>~conquer.md)

###### Tools
- [Enterprise Maven Infrastructure](Enterprise<sub>~Maven</sub>~Infrastructure.md)

#### Phase #3 Control State

###### Principles
- [JigZaw Multidimensional Test Categorization](JigZaw<sub>~Multidimensional</sub>~Test-Categorization.md)
- [Control state](Control-state.md)

###### Tools

- [JMS Testing according to JigZaw](JMS<sub>~Testing</sub><sub>according</sub><sub>to</sub>~JigZaw.md)
- [RestoreDefaultState - Oracle database](RestoreDefaultState<sub>~Oracle</sub>~database.md) 
- [RDBMS testing according to JigZaw](RDBMS<sub>~testing</sub><sub>according</sub><sub>to</sub>~JigZaw.md)

#### Phase #4 Timeline, hva skal testes når?

- Det tar for lang tid å kjøre testene.
- Utvider Test Kategorisering.

###### Principles
- [Timeline](Timeline.md)

###### Tools

#### Phase #5 Ikke funksjonelle krav
- Performance

###### Principles

###### Tools
