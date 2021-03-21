## Challenge 00

Extract or dump MBR from disk as raw data.

## Remarks

MBR or Master Boot Record is the information in the first sector of any storage device which identifies how and where an operating system is located so it can be boot (loaded).

Each OS has its own naming scheme to identify disk.

- Windows: `r"\\.\PhysicalDrive1"` for first disk.
- Linux: `r"/dev/sda"` for first disk, and `r"/dev/mmcblk0"` for first MMC.
- Mac OS: `r"/dev/disk"` for first disk.