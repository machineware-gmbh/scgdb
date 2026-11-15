##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

import gdb

import utils
import vcml


def is_multicast(addr):
    return bool(addr["bytes"]["_M_elems"][0] & 1)


def is_broadcast(addr):
    for i in range(6):
        if addr["bytes"]["_M_elems"][i] != 0xFF:
            return False
    return True


class MacAddrPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        bytes = self.val["bytes"]["_M_elems"]
        return f"{int(bytes[0]):02x}:{int(bytes[1]):02x}:{int(bytes[2]):02x}:{int(bytes[3]):02x}:{int(bytes[4]):02x}:{int(bytes[5]):02x}"


class EthFramePrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        gdb.set_convenience_variable("val", self.val.reference_value())

        type = utils.read_std_string(gdb.parse_and_eval("$val.identify()"))
        if gdb.parse_and_eval("$val.empty()") or not gdb.parse_and_eval("$val.valid()"):
            return f'ethernet_frame {{ {type} }}'

        dest = gdb.parse_and_eval("$val.destination()")
        src = gdb.parse_and_eval("$val.source()")
        size = int(gdb.parse_and_eval("$val.size()"))

        attr = None
        if is_multicast(dest):
            attr = "MULTICAST"
        elif is_broadcast(dest):
            attr = "BROADCAST"

        data = []
        for i in range(size):
            byte = int(gdb.parse_and_eval(f"(int)$val[{i}]"))
            data.append(f"{byte:02x}")
        data = " ".join(data)

        if attr:
            return f'ethernet_frame {{ {type}, {size}bytes, from = {src.format_string()}, to = {dest.format_string()} ({attr}), data = {{ {data} }} }}'
        else:
            return f'ethernet_frame {{ {type}, {size}bytes, from = {src.format_string()}, to = {dest.format_string()}, data = {{ {data} }} }}'


vcml.add_printer("vcml:mac_addr", "^vcml::mac_addr$", MacAddrPrinter)
vcml.add_printer("vcml::eth_frame", "^vcml::eth_frame$", EthFramePrinter)
