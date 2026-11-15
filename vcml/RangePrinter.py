##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

import vcml


class RangePrinter:
    """Pretty printer for vcml::range"""

    def __init__(self, val):
        self.val = val

    def children(self):
        start = self.val['start'].format_string(format='x')
        end = self.val['end'].format_string(format='x')
        list = [('start', start), ('end', end)]
        return iter(list)

vcml.add_printer('vcml::range', '^vcml::range$', RangePrinter)
