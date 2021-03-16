/*
Compile: 
    (x64)
    $ gcc -shared -fPIC -o clib-x64.so clib-so.c

    (x86)
    $ gcc -shared -fPIC -m32 -o clib-x86.so clib-so.c
*/

#include <stdio.h>
#include <string.h>
#include <stdint.h>

struct monster
{
    char name [10];
    int  damage;
};

void hello ()
{
    printf ("Hello World!\n");
}

int32_t retval_test (int32_t input)
{
	return input + 135;
}

void modify_str (char * input)
{
	int i, len;

	for (i = 0, len = strlen(input); i < len; i++)
		input[i] ++;
}

void init_monster (struct monster * m)
{
	strcpy(m->name, "Monster");
	m->damage = 10;
}