; Execve
; buffer is global address, not in stack.
;
; (linux)
; nasm -f elf32 sample-04.nasm -o sample-04.o && ld -m elf_i386 -o sample-04 sample-04.o

bits 32

global _start

section .text
_start:
    ; filling '/bin/sh'
    mov     dword [buffer + 3], 0x68732f2f      ; //sh
    mov     dword [buffer    ], 0x6e69622f      ; /bin

    ; nullify
    xor     ebx, ebx 
    mov     ecx, buffer                         
    mov     byte  [buffer +  7], bl             ; Fill A
    mov     dword [ecx    +  8], ecx            ; Fill BBBB
    mov     dword [ecx    + 12], ebx            ; Fill CCCC

    ; execve
    lea     ebx,  [buffer     ]
    lea     ecx,  [buffer +  8]
    lea     edx,  [buffer + 12]
    xor     eax, eax 
    mov     al, 0xb
    int     0x80

section .bss
    ; modify this buffer, fed to execve
    ; /bin/shABBBBCCCC
    ;   A = 0 (null)
    ;   BBBB = address to argument (null)
    ;   CCCC = null address
    buffer: resb 16