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

import systemc


class ScPortInBoolPrinter:
    "Pretty printer for sc_in<bool>"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        name = self.val["m_name"]
        gdb.set_convenience_variable("val", self.val.reference_value())
        if gdb.parse_and_eval("$val.read()").referenced_value():
            val = "true"
        else:
            val = "false"
        return f"{name} = {val}"


class ScPortOutBoolPrinter:
    "Pretty printer for sc_(out|inout)<bool>"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        name = self.val["m_name"]
        gdb.set_convenience_variable("val", self.val.reference_value())
        if gdb.parse_and_eval("$val->read()").referenced_value():
            val = "true"
        else:
            val = "false"
        return f"{name} = {val}"

systemc.add_printer(
    "sc_in<bool>", "^sc_core::sc_in<bool>$", ScPortInBoolPrinter
)
systemc.add_printer(
    "sc_(out|inout)<bool>", "^sc_core::sc_(out|inout)<bool>$", ScPortOutBoolPrinter
)
