# Scratchpad

hostname: Temporary failure in name resolution
make-ssl-cert: Could not get FQDN, using "altubuntu01".
make-ssl-cert: You may want to fix your /etc/hosts and/or DNS setup and run
make-ssl-cert: make-ssl-cert generate-default-snakeoil --force-overwrite
make-ssl-cert: again.
Processing triggers for ureadahead ...
Processing triggers for ufw ...
Setting up apache2-mpm-worker (2.2.22-6ubuntu2.1) ...
 * Starting web server apache2                                                  apache2: apr_sockaddr_info_get() failed for altubuntu01

---

Need to initialize the database with manage.py
Twitter-Bootstrap needs to be installed
Django needs write access to the directory that the db is in
Login button always points to Altran SSO (/admin will force django auth login though)
The server tries to access jquery.js, django admin static content, bootstrap etc. in /var/www/static
  Most of this is easy to find, but also looks for /var/www/static/js/jquery-ui-1.8.22.custom.min.js
