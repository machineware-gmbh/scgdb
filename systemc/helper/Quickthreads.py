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


def get_qt(scth):
    """Get pointer of Quick Threads object"""
    sc_cor = scth["m_cor_p"]
    if not sc_cor:
        return None
    sc_cor_qt_type = gdb.lookup_type("sc_core::sc_cor_qt").pointer()
    return sc_cor.cast(sc_cor_qt_type)


def get_qt_member(scth, var):
    """Get a member variable of a Quick Threads object"""
    sc_cor_qt = get_qt(scth)
    if not sc_cor_qt:
        return None
    return sc_cor_qt[var]
