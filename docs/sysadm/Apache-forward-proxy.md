# Apache forward proxy

Hei, 
Forward proxy brukes typisk til å gi klienter på et lukket nett tilgang til internett. (komme igjennom brannmur) 
Generelt vil dette oppsettet maskere original IP og fra "oss" ser det ut som forwarding server som er avsender. 

Disse to modulene må være enablet: 
mod_proxy
mod_proxy_http
mod_proxy_connect 

_connect ser ut til å være nødvendig for å proxy'e https. 

For å sette opp forward proxy som støtter https i apache så tror jeg vi skal sette om noe sånt som: 

Listen localhost:443

<VirtualHost *:443>
ProxyRequests On
ProxyVia On

1. For å begrense hvilke klienter som får lov til å bruke proxyen 
<Proxy *:443>
Require host internal.example.com
Require ip 10.1.0.0/255.255.0.0 
Require ip 10.1.0.0/16
</Proxy>
</VirtualHost>

[1](1.md) http://www.jscape.com/blog/bid/87783/

Dokumentasjon: 
http://httpd.apache.org/docs/current/mod/mod_proxy.html
http://httpd.apache.org/docs/current/mod/mod_authz_host.html

http://www.gossamer-threads.com/lists/apache/docs/423956
