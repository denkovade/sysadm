
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
 BIOS -> MBR -> GRUB -> Kernel -> Init Process -> Runlevels
 
# Reboots&Runlevels
 telinit X - change init level;X is number of runlevel 
 init X - change init level;X is number of runlevel
 whoami - check user 
 runlevel - check runlevel
 shutdown -r now - reboot the computer

## Runlevels
- 0 Halt
- 1 Singe-user mode
- 2 Multi-user with partial services
- 3 Full multi-user with networking (text mode)
- 4 Not used
- 5 Full multi-user graphical mode (provides a GUI desktop login)
- 6 Reboot

##Some kernel processes on Linux systems
- kjournald - commits filesystem journal updates to disk
- kwsapd - swaps processes wen physical memory is low
- ksoftirqd - handles soft interrupt if they can't be dealt with context swich time
- khubd - configures USB devices

- fstab or vfstab - files determine how the filesystem should be mount
- fsck - this command check & repair filesystem


# renicing and killing rouge processes ->nice level
* -20 highest priority
* 0 normal, default
* 19 lowest priority

# Prmissions
```chmod```<br />
```d _ _ _ _ _ _ _ _ _ filename ```<br />
```user group other```<br />
r = 4   w = 2  x = 1
```chmod u+x file```
```chmod ugo -w file```
```chmod 555 file```

# command **STDIN STDOUT STDERR**
STDIN - comes from keyboard
STDOUT - goes to console
STDERR - cose to console

* Not all commands listen for STDIN

* 0< redirect STDIN <br />
* 1> redirect STDOUT <br />
* 2> redirect STDERR <br />
* '|' pipe resolts into STDIN of a command <br />
* '>>' this will append instead of everwriting <br />
* & used if redirecting STDERR into STDOUT or vice versa <br />