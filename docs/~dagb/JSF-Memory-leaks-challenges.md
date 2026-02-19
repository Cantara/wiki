# JSF Memory leaks & challenges

Currently I am focusing on severe abnormous memory consumption and leaks in a JSF application running on Websphere 6.1.0.23

Technologies that seems to be involved so far in the analisys is:
- MyFaces 1.1.6. 
    - Components are stored in Http session, and consumes about 2/3 of total heap of 1.5 GB. Session timeout is 8 hrs, which of course is problematic.
    - Models is stored on session scope, so as the user navigates through screens more and more memory will be consumed.

- Axis2 1.4.1
    - A suspicious amount of 65 MB of AxisConfiguration objects resides on the heap. Has not been able to reproduce on Sun JVM / JBoss and unit tests. Axis2 is used both for providing and consumption of webservices.

I am aware of that JSF is known to consume a lot of memory, and it is planned to replace MyFaces 1.1.6 with JSF 1.2 RI and Facelets. This is not an option on a very short term, so any quick wins would be appreciated.

We are currently considering these measures:
1. Reducing session timeout
1. Looking for managing model beans on a conversational scope. How can this be introduced smoothly? Orchestra? Spring Webflow?
1. Persisting idle sessions to Websphere session database. 
1. Putting up more appserver instances
