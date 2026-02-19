# How to install Xvfb on Ubuntu

OS: Ubuntu 10.04 LTS - the Lucid Lynx

#### Install xvfb

```
sudo aptitude install xvfb 
sudo aptitude install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
sudo mod u+s `which Xvfb`
```

(Only xvfb and xfonts-cyrillic was necessary on my system.) 

#### Verify installation 

1. Start Xvfb at display 99
1. Run xclock at display 99
1. Use xwd and xwud to capture the virtual screen in file. 
1. Verify that you can see a visual clock after the last step. 

```
Xvfb :99 -ac &
xclock -display :99 &
xwd -out xfvbtest.xwd -root -display :99
xwud -in xfvbtest.xwd
```

#### Resources 

- [Installing Xvfb on Ubuntu 9.10 (Karmic Koala)](http://blog.martin<sub>~lyness.com/archives/installing</sub><sub>xvfb</sub><sub>on</sub><sub>ubuntu</sub><sub>9</sub><sub>10</sub><sub>karmic</sub>~koala)
