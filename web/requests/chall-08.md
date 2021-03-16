## Challenge 08

Send a GET request to a given URL. Get a response which has challenge on it. Solve the challenge and send the answer back. You must answer it in under 5 seconds.

Use User-Agent `pythonidae`.

The request body should be in JSON with `user` field.

```
{'user':'any username'}
```

The response body would be in JSON with `token` and `challenge`.

```
{
    'token':'your token',
    'challenge':'100 characters long string'
}
```

To solve the challenge, `reverse` the string. Send a POST request with request body in JSON.

```
{
    'token':'your token',
    'answer':'reverse of challenge'
}
```

## Test

Given an URL

```
https://pythonidae.herokuapp.com/web/echo
```

solve the challenge by reverse the string.