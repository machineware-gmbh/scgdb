##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

import systemc
from systemc.helper.ScSimContext import get_sc_sim_context


def get_default_time_unit():
    sim_ctx = get_sc_sim_context()
    if sim_ctx is None:
        return None
    unit = sim_ctx['m_time_params']['default_time_unit']
    return int(unit)

_time_units_map = {
    1: "fs",
    1000: "ps",
    1000000: "ns",
    1000000000: "us",
    1000000000000: "ms",
    1000000000000000: "s",
}

class ScTimePrinter:
    "Pretty printer for sc_time"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        val = int(self.val['m_value'])
        time_unit = get_default_time_unit()
        if time_unit is not None:
            val = val * time_unit
            for factor, unit in sorted(_time_units_map.items(), reverse=True):
                if val % factor == 0:
                    return f'{val//factor}{unit}'
        return f'sc_time {{ {val} }}'

systemc.add_printer('sc_time', '^sc_core::sc_time$', ScTimePrinter)
