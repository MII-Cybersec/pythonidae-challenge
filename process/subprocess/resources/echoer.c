#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
    int  length;
    char buffer[1024];

    while(1)
    {
        fflush(stdin);
        // scanf("%127[^\n]", buffer);
        fgets (buffer, 1024, stdin);
        length = strlen(buffer);
        buffer[length-1] = 0;

        if (strcmp(buffer, "exit") == 0)
            break;
        else 
            printf("%d %s\n", strlen(buffer), buffer);
    }
    
    return 0;
}