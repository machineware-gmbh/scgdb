##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

from libstdcxx.v6.printers import StdHashtableIterator

import vcml


class GpioInitiatorSocketPrinter:
    "Pretty printer for gpio_initiator_socket"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        name = self.val["m_name"]
        for entry in StdHashtableIterator(self.val["m_state"]["_M_h"]):
            if entry["second"]["state"]:
                val = "true"
                break
        else:
            val = "false"
        return f"{name} = {val}"


class GpioTargetSocketPrinter:
    "Pretty printer for gpio_target_socket"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        name = self.val["m_name"]
        for entry in StdHashtableIterator(self.val["m_state"]["_M_h"]):
            if entry["second"]:
                val = "true"
                break
        else:
            val = "false"
        return f"{name} = {val}"


class GpioArrayPrinter:
    "Pretty printer for gpio_array_socket"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        name = self.val["m_name"]
        values = []
        for socket in StdHashtableIterator(self.val["m_sockets"]["_M_h"]):
            for entry in StdHashtableIterator(
                socket["second"].referenced_value()["m_state"]["_M_h"]
            ):
                if entry["second"]:
                    val = "true"
                    break
            else:
                val = "false"
            values.append(f"[{socket['first']}] = {val}")
        return f"{name} = {{ {', '.join(values)} }}"


vcml.add_printer(
    "gpio_initiator_socket",
    "^vcml::gpio_initiator_socket$",
    GpioInitiatorSocketPrinter,
)
vcml.add_printer(
    "gpio_target_socket", "^vcml::gpio_target_socket$", GpioTargetSocketPrinter
)
vcml.add_printer(
    "gpio_array",
    "^vcml::socket_array<vcml::gpio_(initiator|target)_socket, [0-9]*>$",
    GpioArrayPrinter,
)
