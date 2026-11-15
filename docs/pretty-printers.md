# Pretty Printers

scgdb registers GDB pretty-printers, so `print`, `info locals`, `backtrace` arguments and the like show readable values for SystemC, TLM and VCML types.
They activate automatically; no commands are needed.

```
(gdb) print my_can_frame
$1 = can_frame { id = 0x123, dlc = 0x4, data = { 11 22 33 44 } }
```

Use `print/r <expr>` to bypass a printer and see the raw structure, and `info pretty-printer` to list what is registered (`systemc` and `vcml` collections).

## SystemC and TLM

| Type                                            | Example output                                                                                        |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `sc_core::sc_time`                              | `5s`, `10us`                                                                                          |
| `sc_core::sc_status`                            | `elaboration`, `running`, `paused`, `stopped`, ...                                                    |
| `sc_in<bool>`, `sc_out<bool>`, `sc_inout<bool>` | `"scport_module.in" = false`                                                                          |
| `tlm::tlm_generic_payload`                      | `tlm_generic_payload { TLM_WRITE_COMMAND, addr = 0x123, data = { ab bc cd de ef }, TLM_OK_RESPONSE }` |
| `tlm::tlm_dmi`                                  | `tlm_dmi { DMI_ACCESS_READ_WRITE, 0x10..0x20 -> 0x424242, r:0s, w:0s }`                               |

Notes:
- `sc_time` is printed in the largest unit that represents the value exactly.
  Without a simulation context it falls back to the raw value: `sc_time { <value> }`.
- Of the SystemC ports, only the `bool` variants are supported.
- `tlm_generic_payload`: disabled bytes (byte enables) show as `--`, a null data pointer shows `data = nullptr`, and extensions are summarized as `N extension(s)`.

## VCML

| Type                                                      | Example output                                                                                                   |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `vcml::can_frame`                                         | `can_frame { id = 0x123, dlc = 0x4, data = { 11 22 33 44 } }` (flags such as `[RTR]`, `[FDF]`, `[XLF]` appended) |
| `vcml::eth_frame`                                         | `ethernet_frame { IEEE802.3, 60bytes, from = ..., to = ... (MULTICAST), data = { ... } }`                        |
| `vcml::mac_addr`                                          | `12:23:34:45:56:67`                                                                                              |
| `vcml::range`                                             | `{start = 0xab, end = 0xcd}`                                                                                     |
| `vcml::reg<T>`                                            | `0x12345678 "reg_peripheral.reg_u32"`                                                                            |
| `vcml::property<T>`                                       | `"prop_component.prop_u64" = 1311768467463790320`                                                                |
| `vcml::tlm_sbi`                                           | `tlm_sbi { cpuid: 0x0, priv: 0x0, asid: 0x1, atype: SBI_ATYPE_UX, insn }`                                        |
| `vcml::gpio_initiator_socket`, `vcml::gpio_target_socket` | `"gpio_component.gpio_out_0" = true`                                                                             |
| GPIO socket arrays                                        | `"gpio_component.gpio_arr_in" = { [5] = false, [4] = true }`                                                     |

`vcml::property` handles scalars, strings, arrays, `std::vector` and `void` properties.
Uninitialized properties show their default: `"prop_component.prop_not_inited" (uninitialized), default val = 42`.

GPIO socket printers are only registered if the libstdc++ GDB printers are found under `/usr/share/gcc*/python`; see [installation instructions](getting-started.md#installing-the-libstdc-printers).

## Full list of expected output

Every printer and output format is verified by the test suite.
The complete list is published in the project wiki as [Expected pretty-printer output](https://github.com/machineware-gmbh/scgdb/wiki/Expected-pretty-printer-output), generated from [`test/test-scripts/PrinterExpOutput.py`](../test/test-scripts/PrinterExpOutput.py).

----
Documentation updated November 2026
