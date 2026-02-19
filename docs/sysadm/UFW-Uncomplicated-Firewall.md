# UFW - Uncomplicated Firewall

###### Setup using ufw 

```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

```
sudo ufw enable
sudo ufw status verbose
```

- Docs 
    - [https://www.digitalocean.com/community/tutorials/how<sub>~to</sub><sub>setup</sub><sub>a</sub><sub>firewall</sub><sub>with</sub><sub>ufw</sub><sub>on</sub><sub>an</sub><sub>ubuntu</sub><sub>and</sub><sub>debian</sub><sub>cloud</sub><sub>server](https://www.digitalocean.com/community/tutorials/how</sub><sub>to</sub><sub>setup</sub><sub>a</sub><sub>firewall</sub><sub>with</sub><sub>ufw</sub><sub>on</sub><sub>an</sub><sub>ubuntu</sub><sub>and</sub><sub>debian</sub><sub>cloud</sub>~server)
    - [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
