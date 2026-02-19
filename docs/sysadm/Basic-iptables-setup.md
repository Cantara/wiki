# Basic iptables setup

###### List 

```
sudo iptables -L -v
```

###### Rules using classic iptables (not verified!) 
- Allow ssh, web @ port 80 and 443, ping. 
- Deny: everything else 

```
sudo iptables -A INPUT -p tcp --dport ssh -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
sudo iptables -A OUTPUT -p icmp --icmp-type echo-reply -j ACCEPT
sudo iptables -I INPUT 1 -i lo -j ACCEPT

sudo iptables -A INPUT -j DROP
```

```
iptables-save
```

- Docs 
    - [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
    - [http://www.thegeekstuff.com/2011/06/iptables-rules-examples/](http://www.thegeekstuff.com/2011/06/iptables-rules-examples/)
