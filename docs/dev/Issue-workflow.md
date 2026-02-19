# Issue workflow

#### Workflow 

Many issue life-cycles can be used. As a general rule start with a few, well-defined states and add steps only if they add any real customer value. 
Statuses are modelled as a state machine in Jira and it is possible to have different state machines for different projects. (Possibly also for different issue types within a project?) 
Note that management of these state machines is cumbersome, so try to limit the number of state machines and the complexity of each one. 

![issue-workflow](../images/gliffy/29491730-issue-workflow.png)

A suggested starting point

**Open** 
Issue is open for grabs. ToDo: click on Start progress and Assign to me. New status is **In progress**

**In progress**
Someone is assigned and working on this issue. There should be a limit on how many issues are allowed to be in progress pr assignee and per team.
Work on issue until DoD (Definition of Done) is reached. Then describe how issue is solved and documented and click on Resolved. Select reason for resolved (Fix, Won’t fix, Duplicate, Cannot reproduce). New status is **Resolved**.

**Impeded**
You cannot continue work on issue right now, work is impeded. State clearly why work is impeded and who in your opinion is the right person to help remove the impediment. Document work that is done to remove impediment. This should only be used for short term impediments and to signal to others that this issue is currently impeeded. You are still responsible for solving the issue. If it is clear that the work will be impeded longer than sprint or you are not capable of identifying how it could be resolved, assign issue to scrum master.
 
**Resolved** 
The resolved state indicates that there are no more work to be done on this issue and it is therefor either rejected or ready for production. In other words, it is done according to DoD, "it is made the right way".

In the resolved state the issue is assigned to a person with knowledge of the business case for the issue in order to confirm that this issue solves "the right thing". If this can be confirmed the issue is closed. If it is not confirmed that the issue goals are met the issue is reopened and assigned to the person working on it. 

**Closed**
An issue that is closed is either ready for production or rejected. A closed issue should always describe why it is closed and which decision maker has confirmed that this issue is closed. 

If for some reason, there is a QA department that has to be taken into the flow, use this workflow:
1. Open - up for grabs, no work has been done 
1. In progress - issue should be assigned, somebody has taken responsibility for completing this issue. Developer test is included in this state. "If it is not tested, it is assumed to not work." 
1. Ready for QA - assignee should comment on what should be done before resolving or closing the issue 
1. Resolved - issue has been fixed in the eyes of the assignee, but the reporter (or somebody else) must verify the chosen solution. 
1. Won't fix - suggested change has been rejected, useful with a comment with the reason for rejecting the issue. 
1. Closed - Done! Ready to be deployed to production. 
1. Impeded - issue is blocked, a good practice to add a comment about why the issue is impeded 

#### Relationships between issues
- Specify dependencies - some workA must be performed before workB can be started. 

- Subtasks 
    - Start with a single issue, add subtasks as the issue becomes more clearly defined, "promote" subtasks to regular tasks (remember to add some link to the related issues) when not whole tasks can be implemented in one sprint. 
    - Put estimates on subtasks only, the sum of the estimates will be shown as the estimate for the parent task. 

- Relate issues to each other

- Keeps a historic record of what actually happened and why. Possible to reuse context. 

- Jira should not be used as documentation of the system. 
Anything worth documenting should be moved to Confluence. 
Adding links from Jira to Confluence is OK, but preferable not the other way around (unless using the Jira issues macro to present a list of solved issues). 

- Remember to use separate spaces for project management and product/system/service documentation.
