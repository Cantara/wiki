# blitz-docker

Docker Image running Blitz and ApacheRiver

| Field | Value |
| --- | --- |
| **GitHub** | [https://github.com/Cantara/blitz-docker](https://github.com/Cantara/blitz-docker) |
| **Language** | Dockerfile |
| **Stars** | 1 |
| **Last updated** | 2026-05-08 |

!!! tip "Related Wiki Pages"
    This project has documentation in the Cantara Wiki.
    See the [BLITZ section](../blitz/index.md).

---

## README

# blitz-docker
Docker Image running Blitz and ApacheRiver for Java Spaces

To run
-----
* sudo docker run -it -p 8085:8085 -p 4160:4160 -p 4444:22 cantara/blitz 

Log into running instance
-----
* ssh -p 4444 root@localhost (password in Dockerfile)

