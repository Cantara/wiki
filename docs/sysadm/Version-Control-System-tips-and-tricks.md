# Version Control System tips and tricks - Cantara Community Wiki

#### How to choose VCS?

Since most projects are based on Maven, we are limited to using products supported by Maven. See [SCM Overview](http://maven.apache.org/scm/scms-overview.html) .

[Comparison between Bazaar, CVS, Git, Mercurial, Subversion](http://versioncontrolblog.com/comparison/Bazaar/CVS/Git/Mercurial/Subversion/index.html)  might also be helpful.

[Analysis of Git and Mercurial](http://code.google.com/p/support/wiki/DVCSAnalysis)

#### Quickly revert a commit

1. Find the revision number of the commit you want to revert.
   - svn log --limit 5
2. Merge in the negation of the change set from that commit. To revert revision 7:
   - svn merge -c -7 .

#### Use Subversion post-commit hook to send out email

###### Why?

- "Cheap communication" ,i.e. you absorb a lot of information with minimum effort
- Covers some aspects of code and change review and control, since controversial commits are more easily detectable.
- Train developers in VCS best practices. E.g. how to structure your commits and how detailed your commit messages should be.

The only disadvantage of implementing this tactic is increased email sending. This potential challenge is solved by sending email to an email list and setting up sane subjects, as this will allow easy filtering of the email.

###### How?

- Make sure /usr/sbin/sendmail works.
- Copy post-commit template

  ```
  cp ${repoPath}/hooks/post-commit.tmpl ${repoPath}/hooks/post-commit
  ```
- Locate the commit-email.pl sample from the Subversion distribution

  ```
  commitScript=`find / -name commit-email.pl | grep hook-scripts`
  ```
- Copy commit-email.pl sample

  ```
  cp ${commitScript} ${repoPath}/hooks/commit-email.pl
  ```
- Modify ${repoPath}/hooks/commit-email.pl to use sendmail and not smtp. Additional recommended changes can be found in [commit-email.pl.diff](/web/20100615233128/http://wiki.cantara.no/download/attachments/8814624/commit-email.pl.diff?version=2).

  ```
  @@ -47,8 +47,8 @@
   # You should define exactly one of these two configuration variables,
   # leaving the other commented out, to select which method of sending
   # email should be used.
  -#$sendmail = "/usr/sbin/sendmail";
  -$smtp_server = "127.0.0.1";
  +$sendmail = "/usr/sbin/sendmail";
  +#$smtp_server = "127.0.0.1";
  ```
- Modify ${repoPath}/hooks/post-commit to execute commit-email.pl. A minimal version can be

  ```
  #!/bin/sh

  REPOS="$1"
  REV="$2"

  /path/to/repo/hooks/commit-email.pl "$REPOS" "$REV" mailing-list@example.org specific.user1@example.org specific.user2@example.org
  ```
- Make both files executable

  ```
  chmod a+x ${repoPath}/hooks/{commit-email.pl,post-commit}
  ```

###### Resources

- [Quick pragmatic setup](http://blog.charlvn.com/2008/02/setting-up-commit-emailpl.html)
- [A more extensive how-to](http://wordaligned.org/articles/a-subversion-pre-commit-hook)
- [Version Control with Subversion - Hook scripts](http://svnbook.red-bean.com/en/1.0/svn-book.html#svn-ch-5-sect-2.1)
- [Contributed hook scripts at subversion.tigris.org](http://subversion.tigris.org/tools_contrib.html#hook_scripts)

Note that the perl script in SVN has been deprecated in favor of the more powerful python mailer.py.

There is also an even more powerful tool available at <http://opensource.perlig.de/svnmailer/> - however, it requires some python and python-svn bindings and [seems a bit tricky to set up](http://jasonwoodruff.wordpress.com/2006/11/13/svn-mailer/). If you have Ruby installed, the easiest thing to follow this recipe: <http://blog.hungrymachine.com/2007/11/05/pretty-svn-commit-emails/>

#### Avoid IDE specific files and such in the VCS repository

###### Why?

IDE specific files are seldom identical between environments (even though the same IDE is used) and change quite frequently.

###### How

Set up the repository to ignore these files. The following filter is a good starting point.

```
global-ignores = *.iml *.iws *.ipr target test-output activemq-data .classpath .project .settings *.o *.lo *.la ## ..rej *.rej .~ ~ .# .DS_Store
```

This can be done on the root folder of the project or globally for your client.

**Client**:

```
 vim /home/erik/.subversion/config
```

[global-ignores in Subversion documentation](http://svnbook.red-bean.com/en/1.1/ch07.html#svn-ch-7-sect-1.3.2)
