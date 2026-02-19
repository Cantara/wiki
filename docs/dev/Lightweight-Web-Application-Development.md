# Lightweight Web Application Development

These pages are supposed to be a place for sharing ideas on how we can quickly develop web applications.

### Some Jetty Notes

From http://www.jroller.com/robwilliams/entry/ganymede_another_broken_pile_of

I prefer Jetty over WTP with Tomcat (which is what I was using before). I generally launch it under debug mode and I rely on HotSpot's hotswap to change code without restarting. Unfortunately, it's quite limited, so restarts are required often. For my specific case it's not a big deal because the web layer is light so restarts are cheap.

The following links may be useful:

http://code.google.com/p/run-jetty-run/
http://www.webtide.com/eclipse
http://www.codecommit.com/blog/java/so-long-wtp-embedded-jetty-for-me

Each of them shows a different way of using Jetty for development.

Hope it helps,
Ismael

Posted by Ismael Juma on April 27, 2008 at 09:04 PM PDT #
