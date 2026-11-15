# SC_THREAD commands

SystemC coroutines (SC_THREADs) are not OS threads, so GDB's normal `thread` and `backtrace` commands cannot inspect an SC_THREAD that is currently suspended.
scgdb adds commands to list SC_THREADs and to run GDB commands inside one.

Run `sc` or `help sc` at any time for a summary.

All commands need a started simulation and SystemC debug symbols.
Without them, they print `No simulation context`.

The examples below use the simulation from [`example/`](../example/README.md), interrupted with Ctrl-C after a few seconds.

## Command overview

| Command            | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| `info scthreads`   | List all SC_THREADs                                        |
| `sc thread`        | Show the selected SC_THREAD                                |
| `sc thread <id>`   | Select an SC_THREAD                                        |
| `sc <gdb command>` | Run a GDB command in the context of the selected SC_THREAD |
| `sc status`        | Print the simulation status                                |
| `sc time`          | Print the current simulation time                          |
| `sc delta-count`   | Print the current delta cycle count                        |

## Listing SC_THREADs
Before analyzing an SC_THREAD it is helpful to know which threads exist in the current simulation.
`info scthreads` lists all SC_THREADs with their IDs and names:

```
(gdb) info scthreads
   0:	fizzbuzz.thread_buzz (sp: 0x55555558a4b8)
   1:	fizzbuzz.thread_fizz (sp: 0x5555555963c8)
 * 2:	fizzbuzz.thread_main (sp: 0x5555555a22d8)
```

Each line shows:
- an asterisk (`*`) if this SC_THREAD is the coroutine that is currently active,
- the thread ID, which you pass to [`sc thread`](#selecting-an-sc_thread),
- the hierarchical name of the SC_THREAD,
- the saved stack pointer of its coroutine.

The list is collected the first time it is needed and reused until the program exits.
SC_THREADs created after that point do not show up.

> [!NOTE]
> Active coroutines cannot be analyzed yet!
> Selecting one with `sc thread` prints a warning, and running an `sc` command on it results in an error.
> The active coroutine is the one GDB is stopped in, so use the regular GDB commands (`backtrace`, `frame`, ...) for it.

## Selecting an SC_THREAD
An SC_THREAD must be selected before it can be analyzed.
This is done with `sc thread <id>`, using an ID from `info scthreads`.
Running `sc thread` without arguments prints the ID and name of the selected SC_THREAD.

```
(gdb) sc thread 0
[Selecting SC_THREAD 0 (fizzbuzz.thread_buzz)]
(gdb) sc thread
[Current SC_THREAD is 0 (fizzbuzz.thread_buzz)]
```

An invalid ID prints `Unknown SC_THREAD <id>`.
The selection is kept until another SC_THREAD is selected or the program exits.

## Inspecting an SC_THREAD
Once a coroutine is selected, add the prefix `sc` to a GDB command to run it in the context of that SC_THREAD.
For example, `sc backtrace` prints the backtrace of the selected SC_THREAD (output abbreviated):

```
(gdb) sc backtrace
#0  qt_blocki ()
#1  sc_core::sc_thread_process::suspend_me ()
#2  sc_core::sc_thread_process::wait ()
#3  sc_core::wait ()
#4  sc_core::sc_module::wait ()
#5  fizzbuzz_module::thread_buzz ()
#6  sc_core::sc_process_b::semantics ()
...
```

The exact frames depend on the SystemC version and host architecture.
The frame selected inside the SC_THREAD is remembered between `sc` commands, so you can walk the stack as usual:

```
(gdb) sc frame 5
(gdb) sc info locals
(gdb) sc print this->ev_buzz
(gdb) sc list
```

Without a selected SC_THREAD, `sc <gdb command>` prints `No SC_THREAD selected`.

### Forbidden commands

Commands that would resume execution are not allowed in an SC_THREAD context, because the registers of the real thread are only replaced temporarily.
This includes:

`continue`, `fg`, `step`, `stepi`, `si`, `next`, `nexti`, `ni`

Running one of them (or an abbreviation, such as `sc c` or `sc n`) results in an error.
For example:

```
(gdb) sc step
This command cannot be run in a SC_THREAD context!
```

Other commands that resume execution (for example `finish`, `until`, `advance` or `jump`) are not on this list.
Do not run them with the `sc` prefix either.

### How is this done?
Unfortunately, it is not possible to directly feed GDB with arbitrary addresses pointing to stacks of coroutines.
Therefore, a little trickery is required.

The `sc` command manually sets the necessary registers (e.g. frame, stack and instruction pointers) to the values saved for the coroutine before executing the desired command.
This tricks GDB into thinking that it is actually executing the selected coroutine.
After the command is executed, the registers are reset to the values of the real thread.

## Simulation state commands
Besides the wrapper functionality, `sc` also provides commands that print the current state of the simulation.
They do not need a selected SC_THREAD.

- `sc status`: Prints the current status of the simulation, e.g. `elaboration`, `running`, `paused` or `stopped`
- `sc time`: Prints the current simulation timestamp
- `sc delta-count`: Prints the delta count

```
(gdb) sc status
running
(gdb) sc time
5s
(gdb) sc delta-count
10
```

## Limitations
- It is not possible to use the TUI mode of GDB (in a meaningful way), since the `sc` command cannot change the source code listing to that of the selected coroutine.
  As an alternative, you can use the list command (`sc list`).
  You may need to use `sc list .` to force GDB to change the listing to that of the coroutine.
- The active coroutine cannot be analyzed with `sc` (see the note [above](#listing-sc_threads)).
- Only x86-64 and AArch64 host architectures are supported.

----
Documentation updated November 2026
