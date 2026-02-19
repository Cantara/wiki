# 3part token whydah inner workings

- SSO -> STS
    - createandlogin
- STS -> UIB
    - create valid usertoken (from applicationtokenid) for UIB with WhydahUserAdmin role
    - createandlogin 
- UIB -> STS
    - gettokenbytokenid
- UIB
    - create user
    - add default roles
