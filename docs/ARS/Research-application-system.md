# Research application system

The project had the goal of replacing a legacy system that handled research applications and funding. The legacy system was pre-Internet and inherently "introvert". The only human interface was designed for internal employees. Researchers had to send in paper applications that would then be punched into the system. External reviewers of proposals also had to work by receiving and sending paper documents. Progress reporting for projects that received funding was equally primitive. The new system would allow for a much more efficient and transparent process in handling research applications.

Four main strategies were used in the first phases of the project:

- The new system would be based on the existing database (the [shared database](shared-database.md) pattern). This decision was based on the observation that the existing database platform and structure were acceptable for the new system.

- The system would be built according to the [sequence of the underlying workflow](Partition-the-workflow.md): submission of application, peer review, funding decision, progress reporting, and finally end report. The first release would be a web-based system that allowed researchers to assemble and submit applications.

- The first release would only be used for a small portion of the research applications ([limited release](limited-release.md)). We would only handle the simplest type of research proposal and would limit the number of users that were allowed to send their applications through the system. This strategy was facilitated by the shared database.

- Only functionality that was essential was included ([Scope control](Scope-control.md)). Features that were valuable but not essential were excluded from the first release. This was very difficult in practice  since every stakeholder had a different definition of "essential".

These strategies worked well. The first release was deployed after four months and it received about 100 research applications in the first months of operation. This resulted in valuable feedback and one surprise. The project now had to support a system in production that was characterized by very fixed deadlines (submission dates) and highly demanding users (researchers). This made the prioritizing of features in subsequent releases much more difficult.

The biggest problem was in verifying exactly how the legacy system used the database. Almost all data validation was in the system and not in the database. A set of data that was accepted by the database would cause the legacy system to fail. As with most legacy systems, there was also a lot of dormant functionality that was either obsolete or just rarely used. Ignoring rarely used functionality could lead to nasty surprises so it was important to differentiate it from obsolete functionality.
