# Jira - notes

TODO: Write more about Jira and VCS. Mention http://www.atlassian.com/software/crucible

---
Fra Axel W.: 

Jeg mener man trenger å bruke doble fix<sub>~versjoner, nå som Jira støtter det. Altså at sprint</sub><sub> og mavenversjoner i utgangspunktet er én</sub><sub>til</sub>~én, men at man skiller mellom kode og tidsbruk, slik at når man jobber på dotrelease fra forrige sprint kan man sette tiden på inneværende sprint og kodeendringen på dotreleasen. Så lenge man må gjøre slike fikser ihvertfall. Må man aldri det, så kan man slå de to konseptene sammen. Det spørs også litt på hvor nøye tidsoppfølging man trenger, kanskje er det ikke noe problem at tid i inneværende sprint skrives på forrige sprint/versjon, men tasken burde aldri se ut som om den er gjort på en annen kodeversjon enn den faktiske.

https://plugins.atlassian.com/plugins/com.ecliptictech.connector

http://blogs.atlassian.com/2010/08/video_connecting_jira_to_ms_project/

http://www.ceptah.com/

http://www.the-connector.com/index.aspx

---

###### Challenge: Several product owners / scrum master compete for the same resources 

- Time sharing: A developer spends 80% of her time on project A and 20% on project B. 

- All developers work 100% on a single project/team. Teams may "trade" developers. E.g. team A borrows a developer from team B to do some graphical design for 3 days. Team B borrows a database expert from team A to do help debug a difficult SQL problem. 

Should be avoided if possible. 

###### Challenge: Services or libraries used by several teams 

The general way to approach this challenge is to realise that we are now outside the [project scope](../architecture/Project<sub>~Architect.md) and must look to architects and strategies in the [organisation scope](../architecture/Organizational</sub>~Architect.md) or the [product scope](../architecture/Product-Architect.md). 

Often more structure or organisation is unnecessary - the two teams can simply collaborate on the shared library and include tasks in the respective sprints.
