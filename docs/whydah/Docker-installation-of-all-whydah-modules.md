# Docker installation of all whydah modules

### Simple instruction to run whydah in a pre-built docker configuration

**Steps:**

1. Install docker
2. Run (sudo docker run -it -p 9000:9999 totto/whydah /usr/bin/supervisord)
3. Goto <http://localhost:9000/sso/welcome>
4. Congrats - you made it :!!

**Debug**

---

**Steps to build custom images**

1. (Install docker)
2. Copy Dockerfile
3. Build container from Dockerfile (ie: sudo docker build -t="example/whydah-demo" .)
4. Run (sudo docker run -it -p 9000:9999 example/whydah /usr/bin/supervisord)
5. Goto <http://localhost:9000/sso/welcome>
6. Congrats - you made it !! Now you can change the configuration to your likings

**Dockerfile** (From here: <https://github.com/altran/Whydah/tree/master/config/Docker>)

**Build**

**Access**

- <http://172.17.0.116:9999/sso/login>
