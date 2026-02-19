# 1. Installation Choices

### Installer

#### GUI Install

If you're a new user or just want to get something up and running, it's recommended that you download the installer which includes a simple readme and does most of the configuration work for you. The installer package is named installer_pj_n_nn.jar where n_nn is the release version number. Note that you'll still need to download and install the appropriate version of JINI - see required packages. To run the installer use java -jar which will display a simple GUI for gathering paths and port settings.

#### Headless Install

The installer can also be run in headless mode (command-line install) where one should specify the paths and port settings as follows:

```
java -jar installer.jar JDK_Home Jini_Home Install_Dir HTTP_Port
```

or

```
java -jar installer.jar Jini_Home Install_Dir HTTP_Port
```

#### Manual Install

If you're an experienced user who needs ultimate control over installation layout or a developer seeking to make modifications to Blitz, you will wish to download either a binary or source distribution and read the rest of this guide which will guide you through the installation process.
