##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

from functools import wraps

import gdb

import utils
from systemc.helper.ScThreads import get_scthreads, is_active_cor
from systemc.ScCommands.ScThreadWrapper.machinedep import get_cor_regs


class SCThreadHelper:
    """Helper object storing data of a SC_THREAD"""

    def __init__(self, id):
        self.id = int(id)
        self.scth = get_scthreads()[self.id]
        self.frame = None
        if not self.is_active():
            tmp = switch_to_scthread(self.scth)
            self.frame = gdb.selected_frame()
            tmp.restore()

    def name(self):
        return utils.read_std_string(self.scth["m_name"])

    def is_active(self):
        return is_active_cor(self.scth)


CURR_SCTH = None


class RestoreHelper:
    """Helper object storing data of a regular thread"""

    def __init__(self, regs: dict, frame: gdb.Frame):
        self.regs = regs
        self.frame = frame

    def restore(self):
        gdb.newest_frame().select()
        for name, val in self.regs.items():
            gdb.execute(f"set ${name} = {val}")
        self.frame.select()


def scthread_ctx(func):
    """Decorator for running functions in the context of a SC_THREAD"""

    @wraps(func)
    def wrap(*args, **kwargs):
        if CURR_SCTH is None:
            print("No SC_THREAD selected")
        elif CURR_SCTH.is_active():
            raise gdb.GdbError(
                f"SC_THREAD {CURR_SCTH.id} ({CURR_SCTH.name()}) is the active coroutine "
                "and cannot be analyzed with `sc`. Use the regular GDB commands instead."
            )
        else:
            tmp = switch_to_scthread(CURR_SCTH.scth)
            if CURR_SCTH.frame is not None:
                CURR_SCTH.frame.select()
            try:
                func(*args, **kwargs)
            except gdb.error as err:
                print(err)
            CURR_SCTH.frame = gdb.selected_frame()
            tmp.restore()

    return wrap


@scthread_ctx
def gdb_exec_scthread_ctx(arg):
    gdb.execute(arg)


def switch_to_scthread(scth):
    try:
        cor_regs = get_cor_regs(scth)
    except (RuntimeError, gdb.error) as ex:
        print(f"Error reading SC_THREAD regs: {ex}!")
        return None

    frame = gdb.selected_frame()
    gdb.newest_frame().select()
    regs = {i: gdb.parse_and_eval(f"(long)${i}") for i in cor_regs}

    for name, val in cor_regs.items():
        gdb.execute(f"set ${name} = {val}")

    return RestoreHelper(regs, frame)


def cleanup_CURR_SCTH(event):
    global CURR_SCTH
    CURR_SCTH = None


gdb.events.exited.connect(cleanup_CURR_SCTH)


def get_curr_scth():
    return CURR_SCTH


def set_curr_scth(arg):
    global CURR_SCTH

    threads = get_scthreads()
    if threads:
        try:
            id = int(arg)
            CURR_SCTH = SCThreadHelper(id)
        except (ValueError, IndexError):
            print(f"Unknown SC_THREAD {arg}")
            return None
        return CURR_SCTH
