# Basic error handling

---

#### Immediate Caller

A method foo calls method bar which detects an error. The possible errors detected by bar should be documented and foo may be able to recover or ignore some of them, based on the specific kind of error. If it can't, it ll pass the failure upwards. 

- **You may need to document specific errors and supply additional information to the immediate caller.**

_It should be noted that in only the minority of cases Immediate Caller can do something useful_

Examples:

---
#### Upper Layer

Subroutine baz gets the error passed up by foo. It no longer knows about bar, so any documentation or specific error information produced by bar is no longer useful. 

- **The error information must support generic handling strategies, like a blind retry.**
- **Low-level exceptions should not be remapped by upper layers.**

Examples:

- `// do nothing, exception propagates - this is actually fine :P`
- `catch(X e) { throw new Y() } // non-nesting, hides original exception  - remapping and very **BAD**`
- `catch(X e) { throw new Y(x) } // nesting, original included in stack trace  - remapping, adding some value, but rarely useful.`

---
 
#### Human

![http://damienkatz.net/pics/crash_1a.gif](http://damienkatz.net/pics/crash_1a.gif)

The error cannot be corrected by the program, but must be corrected by a human. Since the error was detected by bar, bar has the most specific knowledge of the error and must describe it. 

- **The routine detecting an error is responsible for describing it in terms _understandable to a human_, often the user.**

It is not always the user who can fix the error, but sometimes it is a system administrator or even the programmer. 

- **The system must be able to tell the user if they should contact another human.**

Now the user is told ''Contact your system administrator'' . The error description given by the low-level routine is not shown to the user, but must be forwarded to the administrator instead. If this is the case, we should **automatically and immediately** inform the system adminisator from the system.

- **The system must produce different messages for consumption by different humans.**

Examples:

Reference: [http://mikie.iki.fi/wordpress/?p=5](http://mikie.iki.fi/wordpress/?p=5)

---
