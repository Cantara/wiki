# Debug Java applications on Unix or Linux

The intended audience for this page is sysadmins new to Java applications and Java developer unfamiliar with system administration and/or Linux/Unix. 

What I'm trying to say is: creating a good service requires sysadmins and developers to collaborate! Some basic knowledge bordering another groups profession is thus necessary. 

#### Must know 

| Command | Popular commands | Examples/tutorial |  |
| --- | --- | --- | --- |
| [top | http://linuxmanpages.com/man1/top.1.php] |  | [Using Top More Efficiently | http://www.linuxforums.org/articles/using<sub>~top</sub>~more-efficiently_89.html] |
| [grep | http://linuxmanpages.com/man1/grep.1.php] |  | [How To Use grep Command In Linux / UNIX | http://www.cyberciti.biz/faq/howto<sub>~use</sub><sub>grep</sub><sub>command</sub><sub>in</sub><sub>linux</sub>~unix/] |  |
| [ps | http://linuxmanpages.com/man1/ps.1.php] |  |  |  |
| [tail | http://linuxmanpages.com/man1/tail.1.php] |  |  |  |
| [more | http://linuxmanpages.com/man1/more.1.php] / [less | http://linuxmanpages.com/man1/less.1.php] |  | [Unix Less Command: 10 Tips for Effective Navigation | http://www.thegeekstuff.com/2010/02/unix<sub>~less</sub><sub>command</sub><sub>10</sub><sub>tips</sub><sub>for</sub>~effective-navigation/] |  |
| [wget | http://linuxmanpages.com/man1/wget.1.php] |  |  |  |
| vi / [vim | http://linuxmanpages.com/man1/vim.1.php] |  | [8 Essential Vim Editor Navigation Fundamentals | http://www.thegeekstuff.com/2009/03/8<sub>~essential</sub><sub>vim</sub><sub>editor</sub>~navigation-fundamentals/] |
| [find | http://linuxmanpages.com/man1/find.1.php] |  | [Mommy, I found it!  15 Practical Linux Find Command Examples | http://www.thegeekstuff.com/2009/03/15<sub>~practical</sub><sub>linux</sub><sub>find</sub>~command-examples/] |  |
| [df | http://linuxmanpages.com/man1/df.1.php] / [du | http://linuxmanpages.com/man1/du.1.php] | df -h / du -hs folderName |  |  |
| [netstat | http://linuxmanpages.com/man8/netstat.8.php] | netstat -nlpt | [Linux Howtos Using netstat | http://www.linuxhowtos.org/Network/netstat.htm] \\ [UNIX / Linux: 10 Netstat Command Examples | http://www.thegeekstuff.com/2010/03/netstat<sub>~command</sub>~examples/] |  |

#### Nice to know 

| Command/tool/concepts | Short description | Examples/tutorial |  |
| --- | --- | --- | --- |
| [curl | http://linuxmanpages.com/man1/curl.1.php] |  |  |  |
| [lsof | http://linuxmanpages.com/man8/lsof.8.php] |  |  |  |
| [pargs | http://manpages.unixforum.co.uk/man<sub>~pages/unix/solaris</sub><sub>10</sub><sub>11_06/1/pargs</sub>~man-page.html] |  | Unix only, not Linux? |  |
| sed |  | [World's best introduction to sed | http://www.catonmat.net/blog/worlds<sub>~best</sub><sub>introduction</sub><sub>to</sub>~sed/] |  |
| Wireshark |  |  |  |
| Splunk |  |  |  |
|  |  |  |  |

See also the page about [Java Profiling](Java-Profiling.md)

###### How to learn 

- [50 Most Frequently Used UNIX / Linux Commands (With Examples)](http://www.thegeekstuff.com/2010/11/50<sub>~linux</sub>~commands/) 

- [Open Source Debugging Tools - A 60 Minute Boot Camp](http://tcs.java.no/tcs/?id=091FCD40<sub>~999F</sub><sub>42D4</sub><sub>AA88</sub>~7833550B4D10)

- [What is your favorite open source debugging tool?](http://stackoverflow.com/questions/659780/what<sub>~is</sub><sub>your</sub><sub>favorite</sub><sub>open</sub><sub>source</sub>~debugging-tool) 

#### Unknown 

[Multitail](http://www.thegeekstuff.com/2009/09/multitail<sub>~to</sub><sub>view</sub><sub>tail</sub><sub>f</sub><sub>output</sub><sub>of</sub><sub>multiple</sub><sub>log</sub><sub>files</sub><sub>in</sub><sub>one</sub>~terminal/)
