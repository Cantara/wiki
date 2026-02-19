# BCT TODO

# Todo

### Admin 

| Completed | Priority | Locked | CreatedDate | CompletedDate | Assignee | Name |
| --- | --- | --- | --- | --- | --- | --- |
| T | M | F |  | 1212614987736 | sherriff | * Add BCC as an open source project at java.net or codehaus. |
| T | M | F |  | 1212614991042 | sherriff | * Set up SVN repo and proper backup. |

### QA

- Improve Plexus wiring
- Improve JPOX handling 
- Write proper unit and integration tests for the existing code 

### Support for updates
The set of derived projects must be updated whenever the input list or the dependencies
of the original project are changed. Otherwise the projects would have to be deleted and
re-added to Continuum whenever any of these changes occurred.

We anticipated the need for updates, so the updateDerivedProjects() method in Default-
DerivedProjectManager already support adding new derived projects according to the list
of dependencies that is sent as parameter. updateDerivedProjects() should also remove
derived projects that are no longer relevant. This method can then be used to update the
project list whenever the input list is changed. The steps needed are thus;

- Extend updateDerivedProjects() to remove derived projects that no longer are
relevant.

- Call updateDerivedProjects() every time the input list is changed.

### Configuration in a separate xml file 

- Input list 

- All combinations or just dependencies with newer version that the original dependency 

### Improve usability

- Tactics to improve navigation and make the relationship between original project
and its derived variants more explicit:
    - Use a tree structure on the project summary page, where each original project
is a top-level node, with its derived projects are children.
    - Add a link to the original project in each of the derived projects and a list of
links to the derived projects to the original project.
    - Add a link to the original dependency in the derived dependencies. 

### Improve performance

Bulding and integration are performance intensive activities. This indicate that it can be
beneficial to evaluate tactics that make the implementation more efficient. An effective 
tactic is to reduce the number of derived projects that is actually added or built. We 
suggest to make it possible for the user to

- disable our suggested extension for certain projects.

- exclude or remove combinations of dependencies, to support that some combinations
of dependencies may be irrelevant in the user's context.

Support for these scenarios allows the user to choose which projects to build and how
extensive and how resource intensive the building will be. Available resources can thus
be spent where there is most to gain.
