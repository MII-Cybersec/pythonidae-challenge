## Challenge 03

Call a function `init_monster` in shared library with a defined structure as argument. Print all the field's value.

The structure defined as:

```
struct monster
{
    char name [10];
    int damage;
};
```

Note: argument is passed by reference.

## Test 

Based on your architecture, load the `clib` shared library. Call `init_monster` and pass a reference to structure.