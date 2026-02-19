# Deployment of the CVAPP code.

### CV App 
Login with cvapp user

1. git clone https://github.com/altran/cvapp.git

### Install dependencies

1. sudo apt<sub>~get install python</sub>~pip
1. sudo apt<sub>~get install libxml2</sub>~dev libxslt1-dev
1. sudo pip install django-webodt
1. sudo pip install appy
1. sudo apt<sub>~get install python</sub>~lxml
1. sudo pip install requests (possibly sudo apt-get pip install requests)
1. sudo apt<sub>~get install python</sub>~imaging 
1. sudo pip install django-haystack
1. sudo pip install django<sub>~admin</sub>~bootstrapped
1. sudo pip install pysolr

### Db

Copy database to /home/cvapp/db/cv.db
DB<sub>~file must have write</sub>~permission for www-data

### Photos

Copy photos to /var/www/media/photos
Photos<sub>~folder must have write</sub>~permission for www-data

### Google Account for converting documents (deprecated - we now use soffice)

Must be authorized for the application's server location. If the Download .DOC and .PDF doesn't work the first time, log in manually to Google. There you'll be prompted to approve suspicious login attempt. After this, the server/location will be approved, and you're good to go.

# Setting up new server with ACS (WIP)

### DNS SETUP
Add DNS record, wait a bit for it to register

### APACHE CONFIG
- Update acs.conf in sites-enabled
- Turn on SSL if needed
-- SSLEngine on
-- a2enmod ssl
-- Add certificates to acs.conf 

### ACS LOCALSETTINGS 
- Update allowed-hosts
- Update DB-reference
- Update SSO-reference
-- Make sure appname and appkey is correct for SSO-setup

### SETUP DB
- Might need to add old sources to apt source list
-- psql -h acsdemo1.cmbef5jatjlu.us<sub>~east</sub>~1.rds.amazonaws.com acsdemo1 acsdemo1
-- python /home/acs-user/acs/cvapp/manage.py syncdb
- Load data
-- sudo python /home/acs-user/acs/cvapp/manage.py loaddata cvdemo.json

### ACS DEMO DAILY RESET
- Prod-data in json.
- Run CRON
-- Clear DB
-- Load JSON-data
-- Clear images folder
-- Copy images from source
