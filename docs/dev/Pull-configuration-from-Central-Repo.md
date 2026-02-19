# Pull configuration from Central Repo

In continuous deployment the application should find it's configuration from a central repo. We have not found any tools, or framework for this thus far. This OpenSource tool will fill this gap.

### Basic functionality

### Prerequisite

### The scenario

x number of servers. Started automatically. Pulling running code from Nexus. Need to pull configuration from somewhere.
The Configuration should have a frontend enabling editing individual parameters.

### Lessons learnt from JNDI

- You must NOT allow deployment personell to make individual adjustment to the config.
    - This will fail over time. You will not have a consistent running environment.
