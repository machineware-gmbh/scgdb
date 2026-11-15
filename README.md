# SystemC GDB (scgdb)

Utility scripts that make GDB a better debugger for SystemC and VCML simulations.

- **Pretty-printers** for SystemC, TLM and VCML types: `sc_time`, `tlm_generic_payload`, `tlm_dmi`,
  `vcml::reg`, `vcml::property`, CAN/Ethernet frames, GPIO sockets, and more.
- **SC_THREAD commands** to list SystemC threads and run GDB commands (`backtrace`, `up`, `print`, ...)
  inside a suspended coroutine.
- **Simulation state commands** to query the simulation status, time and delta count.

```
(gdb) info scthreads
   0:	system.cpu.processor_thread (sp: 0x55555558a4b8)
 * 1:	system.serial.serial_transmit (sp: 0x5555555a22d8)
(gdb) sc thread 0
[Selecting SC_THREAD 0 (system.cpu.processor_thread)]
(gdb) sc backtrace
(gdb) print my_frame
$1 = can_frame { id = 0x123, dlc = 0x4, data = { 11 22 33 44 } }
```

[![Nightly Status](https://github.com/machineware-gmbh/scgdb/actions/workflows/nightly.yml/badge.svg?branch=main)](https://github.com/machineware-gmbh/scgdb/actions/workflows/nightly.yml)
[![Test Status](https://github.com/machineware-gmbh/scgdb/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/machineware-gmbh/scgdb/actions/workflows/test.yml)
[![Code Style](https://github.com/machineware-gmbh/scgdb/actions/workflows/style.yml/badge.svg?branch=main)](https://github.com/machineware-gmbh/scgdb/actions/workflows/style.yml)

---

## Requirements

- GDB with Python support
- A simulation built with debug symbols (`-g`), including SystemC itself
- SystemC 2.3.0a – 3.0.2 (tested); `sc` thread commands support x86-64 and AArch64 host architecture
- Optional: GCC's libstdc++ GDB printers for the GPIO socket printers
  ([how to install](docs/getting-started.md#installing-the-libstdc-printers))

---

## Installation

Clone this repository, then create a `.gdbinit` either in your home directory or in the working
directory of your VP:

```
python
import sys
# expand python path so that scgdb modules can be found
sys.path.append('/path/to/scgdb')
end

# source the main init script and register with gdb
source /path/to/scgdb/gdbinit.py
```

When GDB starts you should see `=== SystemC GDB extensions enabled ===`. If you use a `.gdbinit` in
the working directory, GDB may require further configuration; see
[Getting started](docs/getting-started.md#installation).

---

## Usage

Run `help sc` (or just `sc`) in GDB for a list of commands.

| Command            | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| `info scthreads`   | List all SC_THREADs                                        |
| `sc thread [<id>]` | Select an SC_THREAD, or show the selected one              |
| `sc <gdb command>` | Run a GDB command in the context of the selected SC_THREAD |
| `sc status`        | Print the simulation status                                |
| `sc time`          | Print the current simulation time                          |
| `sc delta-count`   | Print the current delta count                              |

Pretty-printers work automatically.

---

## Documentation

| Guide                                      | Contents                                        |
| ------------------------------------------ | ----------------------------------------------- |
| [Getting started](docs/getting-started.md) | Requirements, installation, verifying the setup |
| [Pretty Printers](docs/pretty-printers.md) | Supported types and sample output               |
| [SC_THREAD commands](docs/commands.md)     | Command reference, limitations, how it works    |
| [Troubleshooting](docs/troubleshooting.md) | Common problems                                 |

---

## Example

[`example/`](example/README.md) contains a small SystemC simulation with a ready-to-use `.gdbinit`
for trying out scgdb (`make debug`).

---

## Development

Tests live in [`test/`](test/) and run against several SystemC versions in CI.
The expected pretty-printer output is defined in
[`test/test-scripts/PrinterExpOutput.py`](test/test-scripts/PrinterExpOutput.py) and published to the
[project wiki](https://github.com/machineware-gmbh/scgdb/wiki/Expected-pretty-printer-output).

---

## License

This project is licensed under the GNU General Public License, version 2 license - see the
[LICENSE](LICENSE) file for details.
