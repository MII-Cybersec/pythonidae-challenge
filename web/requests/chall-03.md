## Challenge 03

Send a GET request with a modified cookie to URL.

Use User-Agent `pythonidae`.

Modify cookie and set `role` to 0.

## Test

Access the following URL.

```
https://pythonidae.herokuapp.com/web/cookies
```

set `role` to 0, then sent the cookie as GET request to

```
https://pythonidae.herokuapp.com/web-api/modify
```

## Remarks

Cookies are still used to passed information on stateless HTTP. Often, cookies store parameter to the system. By modifying it, we might be able to change the behavior of the application.