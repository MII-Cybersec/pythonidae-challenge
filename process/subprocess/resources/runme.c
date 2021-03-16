#include <stdio.h>

int main(int argc, char* argv[])
{
    if (argc > 1)
        printf("Receive: %s\n", argv[1]);
    
    return 135;
}