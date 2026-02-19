# Messaging on BEA Weblogic

**[Diagram: Messaging](../Diagram/Messaging.md)**

### Challenges
- Where is Current Status located?
    - Customer
    - Subscription
    - ... it is floating in the message between the Client, MW services and back-office systems.
- Requires a lot of manual testing.
- Test Data are incorrect all the time.

### Lesson learned
- Did they not see the consequence when "misusing" the EJB technique for supporting "status is in the message"?
- High TCO, due to lack of support for automatic testing.
