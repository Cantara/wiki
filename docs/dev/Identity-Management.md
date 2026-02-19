# Identity Management

## Identity management in web applications

Identity management covers how you handle the users of your application. You can choose to have a conecpt of user which has a password and that's all. This is a very slim concept which isn't sufficient for most enterprise web applications. Enterprise applications should be developed to support enterprise identity management solutions.

If enterprise identity management integration is out of scope there are some minimal requirements that your web application should meet:

- Authentication - Follow the interface stipulated by ESAPI to implement authentication as a start.
- Authorization - Use Roles which can inherit roles, make sure you implement in a way that it is easy to check which users that has one role, and it is easy to see which roles one user has.

TBD
