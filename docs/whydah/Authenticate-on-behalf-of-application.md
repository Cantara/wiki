# Authenticate on-behalf of application

> ⚠️ Description is not generic enough to be open for everyone. 

Scenario: 

- SOAP webservice client, basic http auth + https. Considered difficult to force client to implement more sophisticated authentication schemes. 

Sequence 

1. ReceiptControl (RC) authenticates against Whydah and gets back a token. The token should give RC privilege to query the whole graph in Machine Location Service. 
1. IcaBus perfoms a WS request (e.g. verify) and provides user name and password. 
1. RC performs authentication against Whydah, _on behalf-of_ IcaBus, with the username and a hash of the clear-text password and gets a token back. 
1. RC stores username, password hash and the IcaBus token in a local cache. The cache is persisted in MongoDB. 
    1. RC is responsible for verifying username and password against the cache when IcaBus performs requests and for renewing the token when it times out. 
1. RC queries Machine Location Service (MLS) for which machines this client has access to using a list of orgUnitIds from the IcaBus token. 
1. MLS returns the list of machines IcaBus has access to which is cached in RC. 

- Sub-sequent requests from IcaBus will hit caches in Receipt Control every time. 
- IcaBus' access token is renewed async by RC. 
- MLS will notify if the graph changes.  

TODO: Sequence diagram or collaboration/process diagram?
