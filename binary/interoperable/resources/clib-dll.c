/*
Compile:
	$ cl /LD clib-dll.c
*/

#include <windows.h>
#include <string.h>
#include <stdint.h>

#ifdef _MSC_VER
#pragma comment(lib,"advapi32")
#pragma comment(lib,"kernel32")
#pragma comment(lib,"user32")
#pragma comment(lib,"vcruntime")
#pragma comment(lib,"libucrt")
#endif

struct monster
{
    char name [10];
    int  damage;
};

__declspec(dllexport)
void hello ()
{
    DWORD dwtemp = 62;
	TCHAR szname[64], szbuff[MAX_PATH+1];
	
	if (GetUserName(szname, &dwtemp))
		wsprintf(szbuff, "Hello %s", szname);
	else
		lstrcpyn(szbuff, "Hello stranger!", 15);
	MessageBox(NULL, szbuff, TEXT("Title"), MB_OK | MB_ICONINFORMATION);
}

__declspec(dllexport)
int32_t retval_test (int32_t input)
{
	return input + 135;
}

__declspec(dllexport)
void modify_str (char * input)
{
	int i, len;

	for (i = 0, len = strlen(input); i < len; i++)
		input[i] ++;
}

__declspec(dllexport)
void init_monster (struct monster * m)
{
	strcpy(m->name, "Monster");
	m->damage = 10;
}



BOOL WINAPI _DllMainCRTStartup (HINSTANCE hInst, DWORD dwReason, LPVOID lpReserved)
{
    return 1;
}