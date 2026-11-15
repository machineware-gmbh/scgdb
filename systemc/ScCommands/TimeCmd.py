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


class TimeCmd(gdb.Command):
    """Print current simulation timestamp"""

    def __init__(self):
        super().__init__("sc time", gdb.COMMAND_USER)

    def invoke(self, argument, from_tty):
        simctx = get_sc_sim_context()
        if simctx:
            timestamp = simctx["m_curr_time"]
            print(timestamp)
        else:
            print("No simulation context")


TimeCmd()
