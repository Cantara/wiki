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
    - [https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server](https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server)
    - [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
