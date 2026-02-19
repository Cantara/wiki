# Documentation

### Blitz Documentation

- [Overview](Overview.md) - About Blitz
- [Install Guide](Installation.md) - To run Blitz.
- [FAQ](Blitz-FAQ.md) - Online.
- [Tools Guide](Tools.md) - Standard utilities including dashboard.
- [ServiceUI Support](http://dancres.org/bjspj/docs/docs/serviceui.html) - For ServiceUI related options.
- [Developers Guide](http://dancres.org/bjspj/docs/docs/dev_guide.html) - For Blitz system developers and those wishing to build from source.
- [Simple Example](Example.md) - Provides a simple helloworld-style example of a JavaSpaces application.
- [API Documentation](http://dancres.org/bjspj/docs/docs/javadocs/index.html) - For Javadocs.
- [Blitz Extensions](http://dancres.org/bjspj/docs/docs/extensions.html) - Blitz-specific features.
- [Blitz Tuning](http://dancres.org/bjspj/docs/docs/tuning.html) - How to get the best out of Blitz.
- [Future Work and Limitations](http://dancres.org/bjspj/docs/docs/future_limits.html) - What's next for Blitz.
- [License](http://dancres.org/bjspj/docs/docs/LICENSE.TXT) - and how it [affects you](http://dancres.org/bjspj/docs/docs/licensing.html).
- [Required Packages](http://dancres.org/bjspj/docs/docs/required_packages.html) - What you need to run or compile blitz
- [Contrib](http://dancres.org/bjspj/docs/docs/contrib.html) - Useful bits and pieces submitted by Blitz users
- [Reporting Bugs, Providing Feedback or Asking Questions](http://dancres.org/bjspj/docs/docs/feedback.html) - Checklists and email addresses
- [Blitz Project Website](http://www.dancres.org/blitz/) - For news, updates and new releases.

### Platform Specific Notes

- [Mac OS X](http://dancres.org/bjspj/docs/docs/mac_osx.html) - Important notes for running Blitz (compulsory reading).
- [Linux](http://dancres.org/bjspj/docs/docs/linux.html) - Notes on tuning (optional reading).

### Credits

Blitz contains source code from [Prevayler 1.02](http://www.prevayler.org/) and [Doug Lea's concurrency package.](http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/util/concurrent/intro.html)

The Prevayler source code is not quite original as it has been modified to support several different Prevayler types, optional FD.sync() calls, asynchronous checkpointing, buffering and programmatical control of objectoutputstream::reset. With kind permission from Klaus Wuestefeld this code is licensed under the revised BSD license.

Blitz also makes use of [Disney's Trove 1.3.0](http://sourceforge.net/projects/teatrove/) (note that the distribution in the source tree is not the most up to date and was modified to compile correctly under JDK 1.4.x. Trove is licensed under the following terms

Thanks to all these projects for making my life easier!

Blitz uses Berkeley DB Java Edition for persistence ([License](http://dancres.org/bjspj/docs/docs/db_license.html)). Thanks to everyone at [Sleepycat](http://www.sleepycat.com/). The source code for Db Java Edition is available from [SleepyCat](http://www.sleepycat.com/).

Thanks to Nigel Warren and Phil Bishop for contributing a great test suite in the form of the source code for all the examples in their book, "[JavaSpaces in Practice](http://www.djip.co.uk/jsipinfo/)". Special thanks to Phil for doing the initial testing with the examples which allowed me to concentrate on fixing the bugs.

Integration with Inca X, the associated installer and the ServiceUI support in Dashboard was almost entirely the work of the [Inca X team](http://www.incax.com/) - a big thank you to them.

Lastly, thanks to Nimrod Megiddo and Dharmendra S. Modha at IBM Almaden for designing [ARC](http://citeseer.nj.nec.com/megiddo03arc.html) and publishing an article in [;Login: magazine](http://www.usenix.org/publications/login/) which set me thinking.....
