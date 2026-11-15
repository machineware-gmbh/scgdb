# Troubleshooting

## The banner `=== SystemC GDB extensions enabled ===` does not appear
- GDB did not load your `.gdbinit`.
  A `.gdbinit` in the current directory needs `add-auto-load-safe-path`; see [Getting started](getting-started.md#installation).
- Python errors during loading are printed at startup; check the paths in `.gdbinit`.
- `ModuleNotFoundError: No module named 'libstdcxx'`: a `/usr/share/gcc*` directory exists, but it does not contain the libstdc++ printers; see [Installing the libstdc++ printers](getting-started.md#installing-the-libstdc-printers).
- Confirm GDB has Python: `gdb -batch -ex "python print(1)"`.

## `No simulation context`
The SystemC simulation context (`sc_core::sc_curr_simcontext`) is not available:
either the program has not started yet, the context has not been created, or SystemC was built without debug symbols.
Start the program (e.g. `break sc_main`, `run`) and check that your binary and SystemC have been built with debug symbols.

## No `=== Detected SystemC kernel ===` message
SystemC debug symbols were not found.
Link against a SystemC kernel built with debug symbols.

## `No SC_THREAD selected` / `Unknown SC_THREAD <id>`
Select an SC_THREAD with `sc thread <id>` before running `sc <gdb command>`.
Valid IDs are listed by `info scthreads`.

## `Untested SystemC kernel version detected!`
The tested range is 2.3.0 – 3.0.2.
Things may still work; if not, please report an issue.

## `Error reading SC_THREAD regs: ...`
`sc` supports x86-64 and AArch64 only, and needs SystemC's QuickThreads coroutine data.
Other architectures are currently unsupported.

## `This command cannot be run in a SC_THREAD context!`
You tried to resume execution through `sc` (`sc continue`, `sc step`, `sc next`, ...).
Run the command without the `sc` prefix instead.

## `sc` gives an error on the thread marked `*`
The active coroutine is the one GDB is already stopped in.
Use plain GDB commands (`backtrace`, `frame`, ...) for it.

## An SC_THREAD is missing from `info scthreads`
The list is collected once and reused until the program exits, so SC_THREADs created later are not shown.

## Values are printed raw (no pretty-printing)
- Type names must match the registered patterns (e.g. `vcml::reg<...>`, `sc_core::sc_time`); unusual typedefs or wrappers may not be recognized.
- Try `info pretty-printer`.
  If `vcml` or `systemc` is missing, loading failed.
- GPIO socket printers need `/usr/share/gcc*/python` (libstdc++ printers); see [Installing the libstdc++ printers](getting-started.md#installing-the-libstdc-printers).
- Remember `print/r` intentionally disables printers.

## TUI source window shows the wrong code
Expected with `sc`; see the limitations in [SC_THREAD commands](commands.md#limitations).

----
Documentation updated November 2026
