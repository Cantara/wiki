# How your choice of middleware product affects your testability

### Do you allow your developers to mess up the message?
- Exploring three different technologies in message driven architecture. 
- Based on three "strong" brand Glassfish ESB, BEA Weblogic and OSWorkflow/Active Mq Combo.

### How do you avoid that future development diverges from the design you intended?
- Ensure that the natural choice is the right choice.
- Ensure that you spend your time on development, not on "hancking" testabillity.

### Example of moving from "untestable" to automatic testing of Glassfish ESB.
1. Stub your endpoints
1. Script your unit tests, automatic on CI server.
1. Dissect Glassfish ESB libs. Find bare minmum code needed for running test out of container.
1. Finally: Unit test Workflow and Sub-flows.

### Presentation
{viewppt:name=How your choice of middleware product affects your testability.ppt}
