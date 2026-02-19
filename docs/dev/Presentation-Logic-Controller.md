# Presentation Logic Controller

#### How to reduce the impact on testability incurred by generated GUI code 

When creating a Graphical User Interface (GUI) in Java it is common to use GUI builder tools like e.g. Matisse. These tools generate code that is difficult to change and debug without the tool and (afaik) **impossible to test**. To improve testability is it recommended to use the GUI builder only for the actual _layout_ and such. Everything that even remotely _resemble_ logic (yes, also view logic) can be split out to a separate controller. (This will give an extra "controller" in addition to the controller for the MVC pattern.) 

**Presentation Logic Controller**

The MVC-controller has a reference to the data model and references to one or more Presentation Logic Controllers (PLC). Each PLC use a _bindingSource_ to fetch data from an entity. The PLC is given the responsibility of handling presentation logic (e.g. enabling/disabling buttons). The PLC is appropriate when the GUI has a complex relationship with the data model. 

Is this the same as has been described in [Decoupling presentation logic with MVP](http://pragmatic-code.blogspot.com/2007/12/presenter-first-decoupling-presentation.html)? 

Could you have solved the same problem with [Blackboard](http://www.vico.org/pages/PatronsDisseny/Pattern%20Blackboard/)? (The various GUI-elements that read and write the same data (spread across different data objects) can work on a Blackboard.

[Roadmap for Windows Forms data binding](http://support.microsoft.com/kb/313482)

#### Fixtures for Easy Software Testing (FEST)

Using Abbot and TestNG to test Swing GUI. 

[FEST home page](http://fest.easytesting.org/)

[FEST project at Google Code](http://code.google.com/p/fest/)
Article [Test-driven GUI development with FEST](http://www.javaworld.com/javaworld/jw-07-2007/jw-07-fest.html) by Alex Ruiz
[Test-Driven GUI Development with TestNG and Abbot](http://csdl2.computer.org/persagen/DLAbsToc.jsp?resourcePath=/dl/mags/so/&toc=comp/mags/so/2007/03/s3toc.xml&DOI=10.1109/MS.2007.92)

#### Resources

- [GUI Test Patterns](http://blog.perottobergumchristensen.com/?p=41)
