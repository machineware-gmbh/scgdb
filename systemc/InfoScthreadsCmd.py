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
from systemc.helper.Quickthreads import get_qt_member
from systemc.helper.ScSimContext import get_sc_sim_context
from systemc.helper.ScThreads import get_scthreads, is_active_cor


class InfoScthreadsCmd(gdb.Command):
    """Lists SC_THREADs"""

    def __init__(self):
        super().__init__("info scthreads", gdb.COMMAND_USER)

    def invoke(self, argument, from_tty):
        if get_sc_sim_context() is None:
            print("No simulation context")
            return

        threads = get_scthreads()

        if threads is None:
            return

        for i, thread in enumerate(threads):
            name = utils.read_std_string(thread["m_name"])
            sp = get_qt_member(thread, "m_sp")
            if is_active_cor(thread):
                prefix = "*"
            else:
                prefix = " "
            print(f" {prefix} {i}:\t{name} (sp: {sp})")


InfoScthreadsCmd()
