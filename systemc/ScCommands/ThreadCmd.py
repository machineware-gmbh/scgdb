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
from systemc.ScCommands.ScThreadWrapper import get_curr_scth, set_curr_scth


class ThreadCmd(gdb.Command):
    """
    Select a SC_THREAD or print the current one
    usage: sc thread (<thread_id>)
    """

    def __init__(self):
        super().__init__("sc thread", gdb.COMMAND_USER)

    def invoke(self, argument, from_tty):
        argv = gdb.string_to_argv(argument)
        if get_sc_sim_context() is None:
            print("No simulation context")
            return
        if len(argv) == 0:
            scth = get_curr_scth()
            if scth is None:
                print("No SC_THREAD selected")
            else:
                print(f"[Current SC_THREAD is {scth.id} ({scth.name()})]")
        else:
            scth = set_curr_scth(argv[0])
            if scth:
                print(f"[Selecting SC_THREAD {scth.id} ({scth.name()})]")
                if scth.is_active():
                    print(
                        "Warning: this SC_THREAD is the active coroutine and cannot be analyzed with `sc`. "
                        "Use the regular GDB commands instead."
                    )


ThreadCmd()
