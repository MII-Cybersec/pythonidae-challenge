; nasm -f bin sample-00.nasm
;
; Exit shellcode
; Return a non zero value when exiting
bits 32

global _start

section .text
_start:
    xor     eax, eax 
    mov     ebx, eax
    mov     al, 1
    mov     bl, 135
    int     0x80