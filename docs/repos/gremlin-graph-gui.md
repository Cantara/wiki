# gremlin-graph-gui

Application visualizing neural-graph based on Gremlin, Neptune and JWT authentication

| Field | Value |
| --- | --- |
| **GitHub** | [https://github.com/Cantara/gremlin-graph-gui](https://github.com/Cantara/gremlin-graph-gui) |
| **Language** | JavaScript |
| **Stars** | 1 |
| **Last updated** | 2023-07-03 |

---

## README

# gremlin-graph-gui
Application visualizing neural-graph based on Gremlin, Neptune and JWT authentication

## Getting started

```
yarn install
yarn started
```

## How to

1. http://localhost:3000/login
2. Login to AD redirects to 3.
3. http://localhost:3000/token/
4. copy id_token to Bearer
5.
```
curl -i -X GET \
   -H "Authorization:Bearer <add id_token>" \
 'http://localhost:3000/me/'
```
6. Expect Ok

## AzureAd setup

`"oauth2AllowImplicitFlow": true,`

