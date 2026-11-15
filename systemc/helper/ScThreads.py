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

from systemc.helper.Quickthreads import get_qt, get_qt_member
from systemc.helper.ScSimContext import get_sc_sim_context
from systemc.helper.SystemCVersion import get_sysc_ver

SC_THREADS = None


def get_scthreads():
    if SC_THREADS is None:
        analyze_sc_threads()

    if not SC_THREADS:
        print("No SC_THREADs")
        return None

    return SC_THREADS


def analyze_sc_threads():
    """Collect all SC_THREADS"""

    global SC_THREADS
    simctx = get_sc_sim_context()
    if simctx is None:
        return
    ptable = simctx["m_process_table"]
    if get_sysc_ver() < (2, 3, 2):
        current = ptable["m_thread_q"]
    else:
        threads = ptable["m_threads"]
        current = threads["m_head"]

    sc_thread_handle_type = gdb.lookup_type("sc_core::sc_thread_handle")

    SC_THREADS = []
    while current:
        SC_THREADS.append(current)
        current = current["m_exist_p"].cast(sc_thread_handle_type)


def get_curr_cor(scth):
    if get_sysc_ver() < (3, 0, 0):
        return gdb.parse_and_eval("sc_core::curr_cor")
    qt_pkg = get_qt_member(scth, "m_pkg")
    if qt_pkg is None:
        return None
    return qt_pkg["m_curr_cor"]


def is_active_cor(scth):
    qt = get_qt(scth)
    if qt is None:
        return False
    return qt == get_curr_cor(scth)


def cleanup_SC_THREADS(event):
    global SC_THREADS
    SC_THREADS = None


gdb.events.exited.connect(cleanup_SC_THREADS)
