##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

def read_std_string(std_string):
    """
    Converts a std::string (or std::__cxx11::basic_string) to a Python string.
    """
    length = std_string['_M_string_length']
    start_ptr = std_string['_M_dataplus']['_M_p']
    return start_ptr.string(length=length)
