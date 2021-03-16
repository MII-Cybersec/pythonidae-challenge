## Challenge 01

Open any executable file (PE / ELF). Get the (relative/virtual) address of `entrypoint`.

You can use any library or parse the executable format manually.

Optionally, calculate the entrypoint when program is loaded into memory.

## Remarks

Entrypoint is the address of first instruction that will be executed. A compiler generated executable will do some setup to make sure the executable can run propertly. Once the setup is done, the user-defined main-function will be called.

Getting the entrypoint is the first step in binary analysis. In the case when binary has no protection, we can simply trace all functions and basic-blocks from entrypoint. In the case of protection such as packer, we can search for code responsible for unpacking and try to emulate the code to obtain original program.

Some functions declared at `TLS (Thread Local Storage)` might be executed before the main function.