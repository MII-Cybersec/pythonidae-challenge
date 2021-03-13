## Challenge 00

Given a path `P` (either relative or absolute).

List the name of files and directories inside `P`.

Optionally, you can:

- give flag to distinguish file and directory.
- accept a filtering function.

## Test

The directory `pythonidae` has following files and directories:

```
drwxrwxrwx .
drwxrwxrwx ..
-rwxrwxrwx README.md
drwxrwxrwx algorithm
drwxrwxrwx binary
drwxrwxrwx bruteforce
drwxrwxrwx crypto
drwxrwxrwx files
drwxrwxrwx hardware
drwxrwxrwx misc
drwxrwxrwx network
drwxrwxrwx process
drwxrwxrwx web
```

the result would be a list:

```python
L = [ "README.md", "algorithm", "binary", "bruteforce", "crypto", "files", "hardware", "misc", "network", "process", "web" ]
```