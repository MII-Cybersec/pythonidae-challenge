## Challenge 05

Load content of a page. Find and read the a JS script referenced by the page. Parse and get the string value.

A configuration usually written in key-value form, with direct or indirect value assignment.

Example of direct value assignment:

- `key = value`, in case of variable assignment.
- `"key":"value"`, in case of inside of structure (JSON).

Example of indirect value assignment:

- `temp = value; key=temp`

## Test

Given an URL

```
https://pythonidae.herokuapp.com/web/js-file
```

## Remarks

Some sensitive information might be stored inside a JavaScript, such as: base API URL, API endpoint, API key, etc.

One might also expect some functions which generate a string. However, executing the script is not the purpose of this challenge.