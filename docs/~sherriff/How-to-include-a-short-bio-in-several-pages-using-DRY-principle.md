# How to include a short bio in several pages using DRY principle

When you publish an article on this wiki you should also include a little author bio in order to make it clear who wrote the article (and to promote yourself :-)). A nice way to do this in a consistent manner is to add a page to your own wiki homepage, and include it in your article in the following way:

```
{info:title=Author: <your name>}
{include:~<username>:ShortBio}
{info}
```

NB! Remember that your bio-page must be viewable by 'everybody' otherwise people who are not logged in will get an error message.
