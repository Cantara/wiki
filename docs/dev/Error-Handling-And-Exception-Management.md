# Error Handling And Exception Management

## Excecutive Summary

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| |  | **Software Reliability** The bigger problem in software reliability is not how we communicate errors, it's the state we are in when the error happens. So often the **errors are things we can't really do anything about**, we can't force the network connection to work, or somehow create more disk space or memory if we run out. | | |  | **Error Handling Nirvana** Sorry but the truth is, there is **no one best way to communicate error conditions**. "It depends" is the only honest answer. | |

## Table of contents

- [Excecutive Summary](#ErrorHandlingAndExceptionManagement-ExcecutiveSummary)
- [Table of contents](#ErrorHandlingAndExceptionManagement-Tableofcontents)
- [Basics](#ErrorHandlingAndExceptionManagement-Basics)

- [Immediate Caller](#ErrorHandlingAndExceptionManagement-ImmediateCaller)
- [Upper Layer](#ErrorHandlingAndExceptionManagement-UpperLayer)
- [Human](#ErrorHandlingAndExceptionManagement-Human)

- [Java Exception Management](#ErrorHandlingAndExceptionManagement-JavaExceptionManagement)

- [Rules for Developing Robust Programs with Java Exceptions](#ErrorHandlingAndExceptionManagement-RulesforDevelopingRobustProgramswithJavaExceptions)
- [**Checked vs. Unchecked Exceptions**](#ErrorHandlingAndExceptionManagement-Checkedvs.UncheckedExceptions)
- [**Exception Design**](#ErrorHandlingAndExceptionManagement-ExceptionDesign)

- [Developers - Error handling concerns in service or component systems](#ErrorHandlingAndExceptionManagement-DevelopersErrorhandlingconcernsinserviceorcomponentsystems)

- [Distributed Systems and remoting](#ErrorHandlingAndExceptionManagement-DistributedSystemsandremoting)
- [**Error message definition**](#ErrorHandlingAndExceptionManagement-Errormessagedefinition)
- [**Error communication behaviour definition**](#ErrorHandlingAndExceptionManagement-Errorcommunicationbehaviourdefinition)
- [**Projecting exception types from the domain language onto error types from the communication language**](#ErrorHandlingAndExceptionManagement-Projectingexceptiontypesfromthedomainlanguageontoerrortypesfromthecommunicationlanguage)
- [**Maintaining component independence**](#ErrorHandlingAndExceptionManagement-Maintainingcomponentindependence)

- [Implementing the solution](#ErrorHandlingAndExceptionManagement-Implementingthesolution)
- [References](#ErrorHandlingAndExceptionManagement-References)
- [Conclusions](#ErrorHandlingAndExceptionManagement-Conclusions)

## Basics

---

#### Immediate Caller

A method foo calls method bar which detects an error. The possible errors detected by bar should be documented and foo may be able to recover or ignore some of them, based on the specific kind of error. If it can't, it ll pass the failure upwards.

- **You may need to document specific errors and supply additional information to the immediate caller.**

*It should be noted that in only the minority of cases Immediate Caller can do something useful*

Examples:

---

#### Upper Layer

Subroutine baz gets the error passed up by foo. It no longer knows about bar, so any documentation or specific error information produced by bar is no longer useful.

- **The error information must support generic handling strategies, like a blind retry.**
- **Low-level exceptions should not be remapped by upper layers.**

Examples:

- Unknown macro: {code}

  // do nothing, exception propagates - this is actually fine
- Unknown macro: {code}

  catch(X e)

  Unknown macro: { throw new Y() }

  // non-nesting, hides original exception - remapping and very **BAD**
- Unknown macro: {code}

  catch(X e)

  Unknown macro: { throw new Y(x) }

  // nesting, original included in stack trace - remapping, adding some value, but rarely useful.

---

#### Human

The error cannot be corrected by the program, but must be corrected by a human. Since the error was detected by bar, bar has the most specific knowledge of the error and must describe it.

- **The routine detecting an error is responsible for describing it in terms *understandable to a human*, often the user.**

It is not always the user who can fix the error, but sometimes it is a system administrator or even the programmer.

- **The system must be able to tell the user if they should contact another human.**

Now the user is told ''Contact your system administrator'' . The error description given by the low-level routine is not shown to the user, but must be forwarded to the administrator instead. If this is the case, we should **automatically and immediately** inform the system adminisator from the system.

- **The system must produce different messages for consumption by different humans.**

Examples:

Reference: <http://mikie.iki.fi/wordpress/?p=5>

---

## Java Exception Management

#### Rules for Developing Robust Programs with Java Exceptions

|  | **Use exceptions in exceptional situations.** Exceptions are designed for exceptional situations.  - Control of flow must be handled programmaticaly, prohibit your exceptions this luxury. |

**Possible emergencies**

- For each module, identify possible emergencies.
- Define how each module should respond to an undesired event.

**Generic exception handling**

- Do not catch the generic exceptions.
  - Let your framework do this for you. Though create nice pages that show good messages to the end user.
- Do not throw the generic exceptions.

**Spesific exception handling**

- Do not use exceptions for control flow.
- Use exceptions in exceptional situations.
- Ensure the object is in a stable state after throwing an exception.
- Create abstract superclasses for related sets of exceptions.
- Do not leave a catch clause empty.
- Use separate try blocks for statements that throw the same exceptions.

**Runtime vs checked expeptions**

- Use runtime exceptions to indicate programming errors.
- Use checked exceptions for recoverable conditions.

- Be careful when returning from a try clause with finally.

\*Standard vs custom exceptions

- When available, and suitable, use standard exceptions provided by Java. Do not design you own.
- Use custom exceptions when you have a intended purpose with this exception.

- Do not propagate implementation specific exceptions.
- Use exception chaining when translating an exception.
- Use exceptions when a constructor fails.
- Document the exceptions well.

- References
  - *Rules for developing robust programs with java exceptions* by Hoa Dang Nguyen and Magnar Sveen
  - [Best Practice within Java Web Application Development page 60.](http://org.ntnu.no/feta/report.pdf) by Henning Jensen and Erik Drolshammer

#### **Checked vs. Unchecked Exceptions**

- [java.sun.com: Unchecked Exceptions ? The Controversy](http://java.sun.com/docs/books/tutorial/essential/exceptions/runtime.html)
- [Checked vs. Unchecked Exceptions - Never Ending Debate](http://suravarapu.blogspot.com/2005/08/checked-vs-unchecked-exceptions-never.html)
- [Does Java need Checked Exceptions?](http://www.mindview.net/Etc/Discussions/CheckedExceptions)

#### **Exception Design**

- [Subbu Allamaraju on "Exception Design and Usability"](http://www.theserverside.com/news/thread.tss?thread_id=35586)

## Developers - Error handling concerns in service or component systems

The fact that error handling is often the lowest-priority concern is doubly weird if you consider that **cross-component error handling is the same concern as core functionality messaging**. In both cases there are the same sets of concerns, both with regards to communication with external components and interaction between the component's internal implementation and the communication layer. Some typical concerns that development teams have to deal with are:

#### Distributed Systems and remoting

**Integration Points**

- - Every integration point will eventually fail in some way, you need to be prepared
  - Integration point failures take many forms, e.g.:
    - Network error
    - Sematic error
    - Protocol violation
    - Slow response
    - Direct hang
  - Program defensively to avoid cascading failures
  - Integration points without timeouts is a surefire way to create cascading failures
  - Safe resource pools always limit the time a thread can wait to check out a resource

#### **Error message definition**

Just as SOA components require clear definitions of the messages that will be exchanged with client components for mainline communication, **clear definitions** must also be given of messages that carry error information.

#### **Error communication behaviour definition**

Just as mainline communication behaviour between SOA components must be clearly and formally defined, so must similar definitions be given for when a component can send an error message in response to a request for operation.

See [Error Categorization example](/web/20230531234620/https://wiki.cantara.no/display/dev/Error+Categorization+example "Error Categorization example")

#### **Projecting exception types from the domain language onto error types from the communication language**

In the case of error handling, this is one half of a problem that also exists for mainline communication. In mainline communication request messages must be projected onto domain model types and domain model types must be projected onto communication language types when the component returns a response. In the case of error handling of course there is no concept of request projection since nobody requests an error; however, the analog with projecting a domain model type onto a response communication message remains.

#### **Maintaining component independence**

This concern actually affects a component more as a consumer of other services than as a publisher of services. Maintaining component independence is related to avoiding domain models leaking over into foreign components (as Eric Evans puts it). In the case of messaging it means not building your domain model so that it is a mere copy of a foreign component's communication model. In the more specific case of error handling it relates to not linking error handling too closely to the definition of errors used by foreign components. Instead, as with mainline messages, **foreign component-generated errors should be projected onto the local domain**

Reference: [SOA component design: thinking about error handling](http://www.gridshore.nl/2008/07/26/soa-component-design-thinking-about-error-handling/)

---

## Implementing the solution

|  | **Building a deck** Aggregate some good wisdom from *Building a Deck*  see <http://damienkatz.net/2006/04/error_code_vs_e.html> |

---

## References

- [Getting it Right: Error Handling and Exception Management](http://www.softwaremag.com/L.cfm?doc=1026-3/2007)
- [SOA component design: thinking about error handling](http://www.gridshore.nl/2008/07/26/soa-component-design-thinking-about-error-handling/)
- [Error codes or Exceptions? Why is Reliable Software so Hard?](http://damienkatz.net/2006/04/error_code_vs_e.html)

---

## Conclusions

|  | The much bigger problem in software reliability is not how we communicate errors, it's the state we are in when the error happens. So often the errors are things we can't really do anything about, we can't force the network connection to work, or somehow create more disk space or memory if we run out. |
