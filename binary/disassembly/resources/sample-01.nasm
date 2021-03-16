; nasm -f bin sample-01.nasm 
;
; Write data to stack and print
bits 32

global _start

section .text
_start:
    sub     esp, 32
	mov	    dword [esp  ], 0x2049494d
    mov     dword [esp+4], 0x65627943
    mov     dword [esp+8], 0x63655372
        
    xor     eax, eax 
    xor     ebx, ebx
    xor     edx, edx 
    mov     byte [esp+12], al
    mov     bl, 1
    mov     ecx, esp 
    mov     dl, 12 
    mov     al, 4
    int     0x80

    xor     eax, eax
    mov     al, 0x1
    int     0x80