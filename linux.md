
# Phases of the boot process
Bootstrapping  means "starting up a computer". During bootstrapping the kernel is loaded into memory and begining to execute.
- reading of the bootloades from the MBR(master boot record)
- loading & initialization of the kernel
- device detection & configuration
- creation of kernel process
- administrator intervention (single-user mode onluy)
- execution of the system startup scripts

The kernel is itself a program and the first bootstrappping task is to get this program into memory so that it can be executed.
/unix or /vmunix <-> /boot/vmlinuz

## Schema of bootstraping
 BIOS -> MBR -> GRUB -? Kernel -> Init Process -> Runlevels

## Runlevels
- 0 Halt
- 1 Singe-user mode
- 2 Multi-user with partial services
- 3 Full multi-user with networking (text mode)
- 4 Not used
- 5 Full multi-user graphical mode (provides a GUI desktop login)
- 6 Reboot