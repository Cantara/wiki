# Facebook configuration

Whydah can be configured to use Facebook as a third party Identity Provider.   
This is a setup guide to help you get the cofiguration right.  
See example at <https://www.facebook.com/games/getwhydah> and try to log in at <https://demo.getwhydah.com/test/hello>

## Why use Facebook?

Facebook OAUTH is useful instead of forcing users outside your organization to sign up for a new identity.  
With Whydah the Facebook users are given a set of predefined roles.

## Prerequisites

- Whydah installation and known public IP for you SSO-LoginWebApp
- Name of app
- Preferred contact e-mail for people who have questions about the app.
- App Icon, 1024 x 1024 pixels
- Small app Icon, 16 x 16 pixels

## Facebook configuration

### 1. Create app on Facebook

- Go to <https://developers.facebook.com/apps/async/create/platform-setup/dialog/>
- Set up the App
  - On the Settings - Basic pane
    - Enter Display Name, Namespace, App Domains, Contact Email
    - Press *Add Plattform* and add a Web plattform, the URL should be the URL to your app (Not to whydah login webapp).
      - Repeat if other platforms should be supported.
  - On the Settings - Advanced Pane
    - Deauthorize callback URL is not yet implemented by Whydah
    - Activate Social Discovery (if you prefer)
    - Activate Client OAuth
    - Enter the IP of <Probably SSO-LoginWebApp> for Server IP Whitelist
    - Enter Valid OAuth redirect URIs. This should point to /fbauth on your SSO-LoginwebApp. Example: <http://hademo.getwhydah.com/sso/fbauth>
  - On the Settings - Migrations
    - Enable Stream post URL security (Not sure if this is Necessary)
  - On the Status & Review - Status Pane
    - Make the app Public
    - Check the items of information that you want to retrieve from FBGraph and submit them for review.
  - On the App Details Pane
    - Enter *Primary Language*, *Tagline*, *Short Description*, *Publisher*, *Long Description* , *Category*, *Business*, *Explanation for Permissions*
    - Enter *Privacy Policy URL*, *Terms of Service URL*, *User Support Email*, *User Support URL*, *Marketing URL* (Should be a marketing website, not the one that triggers login)
    - Upload App Icons (and promotional images/video if you like)

- Retrieve *App ID* and *App Secret* to be used in the next step

### 2. Configure Whydah

- Configure UserIdentityBackend default roles for new Facebook-users.

- Restart the service

- Configure SSO-LoginWebApp

- Restart the service

### 3. Verify

- Go to your app, you should be redirected to SSO Login Web App, there you should see a "Login with Facebook" - click it.
- If you have done everything right you will be sent back to your app through /fbauth on SSO-LoginWebApp
