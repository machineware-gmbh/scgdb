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

import vcml


class RegPrinter:
    "Pretty printer for vcml::reg<T, N>"

    def __init__(self, val):
        self.val = val

    def get_name(self):
        obj = self.val.cast(gdb.lookup_type('sc_core::sc_object'))
        return obj['m_name']['_M_dataplus']['_M_p'].string()

    def to_string(self):
        value = self.val['m_value']
        cells = int(self.val['m_cell_count'])

        s = '{ ' if cells > 1 else ''

        for i in range(cells):
            v = int(value[i])
            s = f'{s}0x{v:x} '

        if cells > 1:
            s = s + '} '

        return f'{s}"{self.get_name()}"'

vcml.add_printer('vcml::reg', '^vcml::reg<[^>]+>$', RegPrinter)
