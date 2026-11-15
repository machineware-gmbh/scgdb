##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

import systemc
from systemc.helper.SystemCVersion import get_sysc_ver


def get_status_string(val):
    if get_sysc_ver() < (3, 0, 0):
        strings = {
            0x00: "uninitialized",
            0x01: "elaboration",
            0x02: "before end of elaboration",
            0x04: "end of elaboration",
            0x08: "start of simulation",
            0x10: "running",
            0x20: "paused",
            0x40: "stopped",
            0x80: "end of simulation",
            0x100: "end of initialization",
            0x400: "end of update",
            0x800: "before timestep",
        }
    else:
        strings = {
            0x001: "elaboration",
            0x002: "before end of elaboration",
            0x004: "end of elaboration",
            0x008: "start of simulation",
            0x010: "running",
            0x020: "paused",
            0x040: "stopped",
            0x080: "end of simulation",
            0x100: "end of initialization",
        }
    return strings[val]



class ScStatusPrinter:
    """ "Pretty printer for sc_status"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        val = int(self.val)
        return get_status_string(val)


systemc.add_printer("sc_status", "^sc_core::sc_status$", ScStatusPrinter)
