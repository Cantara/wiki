# Maven Project Terminology

| **trunk** | A location in the code repository bordering _tags_ and _branches_ |
| **project** | A maven project. If there's a pom, it's a project |
| **pom** | Project Object Model. The meta-information for project |
| **parent pom/project** | A project of type 'pom' being referenced as a parent from another project |
| *[company pom | Company parent pom example for only Java projects]* | The parent pom shared by all projects in a company |
| **module** | A project which is handled together with other projects |
| **reactor project** | A project with modules. Usually it is also the parent of each module because it manages project versions |
| **builder project** | A project with modules that do not reference it as parent - it's a utility/hack for typically building snapshots together |
| **artifact** | Output of a maven project build |
| **deployment unit** | An artifact that can be deployed |  |
