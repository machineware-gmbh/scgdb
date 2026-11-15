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


class DeltaCountCmd(gdb.Command):
    """"Print current simulation delta count"""

    def __init__(self):
        super().__init__("sc delta-count", gdb.COMMAND_USER)

    def invoke(self, argument, from_tty):
        simctx = get_sc_sim_context()
        if simctx:
            delta_count = simctx["m_delta_count"]
            print(delta_count)
        else:
            print("No simulation context")


DeltaCountCmd()
