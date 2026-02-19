# Agile Project Communication

## Intro

- Agile communication 
    - Which software-stack is needed to support the agile methodologies we want to use? 
        - Wiki, jira and email lists (+ Scrumworks?) 
        - Single-Point-of-Entry to the documentation above, plus Maven site and test & build history

## Implementation recommendations 

#### Email lists 

- projectName@company.com - Public email list for the project team. Goes to all members of the team. 

- projectName-dev@company.com - Email list all developers of the team. Can be used instead of projectName when the topic is not relevant for alle members on the projectName list. 

- projectName-builds@company.com - alias for projectName-dev@company.com. Email from the CI server should be sent to this alias to simplify email filtering. 

- projectName-commits@company.com - alias for projectName-dev@company.com. Email sent with a post-commit hook from the VCS server should be sent to this alias to simplify email filtering. See [Use Subversion post-commit hook to send out email](http://wiki.community.objectware.no/pages/viewpage.action?pageId=3473431#VersionControlSystemtips&tricks-UseSubversionpostcommithooktosendoutemail) for details on the svn post-commit hook setup. 

## White-boards 

At least one big whiteboard available to the development team increases efficiency dramatically. It is not expensive, so just try it :)
