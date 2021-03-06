## Challenge 06

Send a POST request with an JWT token in headers as `authorization` header.

Optionally, try to use random string as `Authorization`.

Note: the token is generated from `Challenge 04`.

## Test

Send POST request with `user` and `pass` in JSON format, to this URL.

```
https://pythonidae.herokuapp.com/web/login
```

get `jwt_token`, send a POST request to this URL.

```
https://pythonidae.herokuapp.com/web/jwt_header
```

## Remarks

Some web service API need access token embedded in the headers as `authorization` header.

JWT is not the only schme used to authenticate. In some machine to machine communication where environment is controlled, a simple API key can be used as token to authenticate.