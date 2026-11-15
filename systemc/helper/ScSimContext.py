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


def get_sc_sim_context():
    """Return the simcontext or None if simcontext is nullptr or not found"""
    try:
        tmp = gdb.parse_and_eval("sc_core::sc_curr_simcontext")
    except gdb.error:
        return None

    if tmp == gdb.Value(0):
        return None
    return tmp
