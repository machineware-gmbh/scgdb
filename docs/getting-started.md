# Getting started

## Requirements

- GDB with Python support (check with `gdb -batch -ex "python print(1)"`).
- A simulation built **with debug symbols** (`-g`) that links SystemC.
- SystemC versions 2.3.0 – 3.0.2 are tested. Other versions might work but are untested!
- Debug symbols for the SystemC library itself (e.g. `--enable-debug`), since scgdb reads the simulation context from them.
- For the `sc` thread commands: x86-64 or AArch64 host architecture, with SystemC's QuickThreads coroutines.
- VCML printers need no VCML installation, only the VCML types in your binary's debug info.
  GPIO socket printers additionally need the libstdc++ GDB printers (see [Installing the libstdc++ printers](#installing-the-libstdc-printers)).

## Installation

Clone the repository somewhere permanent:

```sh
git clone https://github.com/machineware-gmbh/scgdb.git ~/scgdb
```

Create a `.gdbinit` in your home directory (applies to every GDB session) or in the
working directory of your VP (applies there only):

```
python
import sys
# expand python path so that scgdb modules can be found
sys.path.append('/path/to/scgdb')
end

# source the main init script and register with gdb
source /path/to/scgdb/gdbinit.py
```

GDB refuses to load `.gdbinit` from the current directory unless it is trusted.
If you see an "auto-loading has been declined" message, add this to `~/.gdbinit`
(or `~/.config/gdb/gdbinit`):

```
add-auto-load-safe-path /path/to/your/vp
```

## Installing the libstdc++ printers

scgdb's GPIO socket printers reuse GCC's libstdc++ GDB printers.
All other scgdb printers work without them.
scgdb looks for them in `/usr/share/gcc*/python`, so first check whether they are already installed:

```sh
ls -d /usr/share/gcc*/python
```

On RHEL-based systems this is typically `/usr/share/gcc-<version>/python`; on current Debian/Ubuntu it is `/usr/share/gcc/python`.
The printers are part of the libstdc++ runtime package.
If the directory is missing, install it:

```sh
# Debian / Ubuntu
sudo apt install libstdc++6

# RHEL / Fedora / Rocky / Alma
sudo dnf install libstdc++
```

If the directory is still missing, find the owning package with `apt-file search libstdcxx/v6/printers.py` (Debian/Ubuntu) or `dnf provides '*/libstdcxx/v6/printers.py'` (RHEL), and install it.
Restart GDB afterward.

## Verify the installation

Start GDB on your simulator:

```sh
gdb ./my_vp
```

You should see:

```
=== SystemC GDB extensions enabled ===
```

Once a binary with SystemC debug symbols is loaded, GDB also prints the detected SystemC kernel version:

```
=== Detected SystemC kernel: 2.3.3 ===
```

Then try `help sc`, which lists all available commands.
If something is missing, see [Troubleshooting](troubleshooting.md).

## Try the example

The `example/` folder contains a small simulation (a `fizzbuzz` module with three SC_THREADs) with a ready-made `.gdbinit`.
See [example/README.md](../example/README.md) for build instructions, then:

```sh
cd example
make debug      # starts gdb with scgdb loaded
```

A first session: start the simulation, let it run for a few seconds and interrupt it with Ctrl-C.

```
(gdb) run
^C
Program received signal SIGINT, Interrupt.
(gdb) info scthreads
   0:	fizzbuzz.thread_buzz (sp: 0x55555558a4b8)
   1:	fizzbuzz.thread_fizz (sp: 0x5555555963c8)
 * 2:	fizzbuzz.thread_main (sp: 0x5555555a22d8)
(gdb) sc thread 0
[Selecting SC_THREAD 0 (fizzbuzz.thread_buzz)]
(gdb) sc backtrace
(gdb) sc time
5s
```

`thread_main` is marked with `*` because it is the coroutine that was running when the simulation was interrupted.
The other two are suspended in `wait()`, which is what `sc backtrace` shows for `thread_buzz`.

See the [command reference](commands.md) for what each of these commands does.

----
Documentation updated November 2026
