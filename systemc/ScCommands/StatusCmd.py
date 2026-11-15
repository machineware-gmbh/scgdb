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

from systemc.helper.ScSimContext import get_sc_sim_context


class StatusCmd(gdb.Command):
    """Print current simulation status"""

    def __init__(self):
        super().__init__("sc status", gdb.COMMAND_USER)

    def parse_status(self, simctx):
        sim_status = simctx["m_simulation_status"]
        in_sim_control = simctx["m_in_simulator_control"]
        enum_type = gdb.lookup_type("sc_core::sc_status")
        SC_RUNNING = gdb.Value(0x10).cast(enum_type)
        SC_PAUSED = gdb.Value(0x20).cast(enum_type)
        if sim_status != SC_RUNNING:
            return sim_status
        else:
            if in_sim_control:
                return SC_RUNNING
            return SC_PAUSED

    def invoke(self, argument, from_tty):
        simctx = get_sc_sim_context()
        if simctx:
            status = self.parse_status(simctx)
            print(status)
        else:
            print("No simulation context")


StatusCmd()
