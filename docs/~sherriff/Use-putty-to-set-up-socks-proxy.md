# Use putty to set up socks proxy

#### To establish the tunnel from Windows: 
- Download putty.exe and put it in PATH 
- 'Start --> Run...':  putty -D 9853 username@sshhost 

#### To configure Firefox to work with the proxy follow these instructions:

   1. Open FireFox.
   2. Click 'Tools' at the top to pull down the Tools Menu.
   3. From the menu, select 'Options...' at the very bottom. This opens the Options window.
   4. Click 'Advanced' at the top right corner of the window.
   5. Click the 'Network' tab.
   6. Where it says 'Configure how Firefox connects to the Internet' click the 'Settings...' button. This opens the Connection Settings window.
   7. Select 'Manual proxy configuration:'.
   8. Where it says 'SOCKS Host:' enter localhost into the box.
   9. 9) Where it says 'Port:' enter 9853 into the box.
  10. Click the 'OK' button.
  11. Click the 'OK' button on the previous window.
  12. In the browser location bar (the place where you type web addresses), type about:config and press Enter. This opens a different set of Firefox preferences.
  13. Where it says 'Filter:' at the top, type network.proxy.socks. The list of preferences will automatically change to show your proxy preferences.
  14. Highlight 'network.proxy.socks_remote_dns' by clicking it only once. Then, right<sub>~click it. This opens a small pull</sub>~down menu. Select 'Toggle' from the menu to change its value to 'true'. This adds privacy by preventing DNS queries from leaking. This is the reason why Firefox is recommended over other browsers for using this service.
  15. Close Firefox and restart it.
  16. Go to a site like cmyip.com to check and make sure your IP address shows up as the proxy address and not your real IP. 

#### Resources 

[Configure PuTTY To Create SSH SOCKS Proxy For Secure Browsing](http://vectrosecurity.com/content/view/67/26/)
[Configure Firefox To Use SSH SOCKS Proxy Tunnel](http://vectrosecurity.com/content/view/68/26/)
