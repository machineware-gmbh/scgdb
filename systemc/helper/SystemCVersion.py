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


def parse_sysc_version():
    major = int(gdb.parse_and_eval("sc_core::sc_version_major"))
    minor = int(gdb.parse_and_eval("sc_core::sc_version_minor"))
    patch = int(gdb.parse_and_eval("sc_core::sc_version_patch"))

    return (major, minor, patch)


def parse_sysc_originator():
    originator = utils.read_std_string(
        gdb.parse_and_eval("sc_core::sc_version_originator")
    )
    return originator


SYSC_VER = None
SYSC_ORIGINATOR = None


def get_sysc_ver():
    return SYSC_VER


def get_sysc_originator():
    global SYSC_ORIGINATOR
    if not SYSC_ORIGINATOR:
        SYSC_ORIGINATOR = parse_sysc_originator()
        if len(SYSC_ORIGINATOR) == 0:
            SYSC_ORIGINATOR = None
    return SYSC_ORIGINATOR


def setup_version(event):
    """
    Try to set global version and originator variables
    If unsuccessful, global variables stay `None`
    """
    global SYSC_VER
    if SYSC_VER is None:
        try:
            gdb.lookup_type("sc_core")
        except gdb.error:
            return
        else:
            SYSC_VER = parse_sysc_version()
            (major, minor, patch) = SYSC_VER
            print(f"=== Detected SystemC kernel: {major}.{minor}.{patch} ===")

            if SYSC_VER < (2, 3, 0) or SYSC_VER > (3, 0, 2):
                print("=== Untested SystemC kernel version detected! ===")


# Try to set variables on gdb startup & when a object file is loaded
setup_version(None)
gdb.events.new_objfile.connect(setup_version)


def clear_version(event):
    """Reset global variables when object files are cleared from gdb"""
    global SYSC_VER, SYSC_ORIGINATOR
    SYSC_VER = None
    SYSC_ORIGINATOR = None


gdb.events.clear_objfiles.connect(clear_version)
