# 3.Party Access Providers

### Data we need/wish for:

**UserConnection** table containing:

- UserId
- ProviderId (eg. Facebook/Google/Twitter/LinkedIn)
- ProviderUserId -
- AccessToken - token received from the provider.
- AccessTokenExpireTime - timeout as decided by the provider.
- DisplayName - name of the user
- ProfileUrl - link address to the person's profile.
- ImageUrl - link to an image. Eg. found on the profile of the user.

### When authenticating an user from 3.party access provider

When first authenticated:

- Create an record in the UserConnection table  
  ...
