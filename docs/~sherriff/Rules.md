# Rules

There are six possible changes that should invoke an action; add/remove projects,
add/remove dependencies from a project and add/remove dependencies from the list of
derived dependencies. The changes and their corresponding actions are as follows:

1. A new project is added -> new derived projects should be created if its dependencies
are relevant.
1. A project is removed -> the original project and all its derived projects should be
deleted.
1. A new dependency is added to the original project -> new derived projects should
be created if the new dependency is relevant.
1. A dependency is removed from the original project -> all affected derived projects
should be deleted.
1. A new dependency is added to the input list -> new derived projects should be
created if the new dependency is correspondent with a relevant dependency in the
original project.
1. A dependency is removed from the input list -> all affected derived projects should
be deleted.
