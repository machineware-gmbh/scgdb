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

forbidden_cmds = ["continue", "fg", "step", "stepi", "si", "next", "nexti", "ni"]


class ScCmd(gdb.Command):
    """
    SystemC status commands and SC_THREAD wrapper

    Runs gdb commands in a SC_THREAD context and provides SystemC convenience commands.
    For wrapping capability, select a thread with `sc thread <id>` and then prefix your desired gdb command with `sc`.
    For example: `sc up 3`.
    """

    def __init__(self):
        super().__init__("sc", gdb.COMMAND_USER, gdb.COMPLETE_COMMAND, True)

    def invoke(self, argument, from_tty):
        if len(argument) == 0:
            gdb.execute("help sc")
        else:
            for forbidden in forbidden_cmds:
                if forbidden.startswith(argument):
                    print("This command cannot be run in a SC_THREAD context!")
                    return
            gdb_exec_scthread_ctx(argument)


ScCmd()

from .DeltaCountCmd import DeltaCountCmd
from .ScThreadWrapper import gdb_exec_scthread_ctx
from .StatusCmd import StatusCmd
from .ThreadCmd import ThreadCmd
from .TimeCmd import TimeCmd
