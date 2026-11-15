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


class TlmDmiAccessPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        if int(self.val) == 0:
            return 'DMI_ACCESS_NONE'
        if int(self.val) == 1:
            return 'DMI_ACCESS_READ'
        if int(self.val) == 2:
            return 'DMI_ACCESS_WRITE'
        if int(self.val) == 3:
            return 'DMI_ACCESS_READ_WRITE'
        return 'DMI_ACCESS_INVALID'

class TlmDmiPrinter:
    "Pretty printer for tlm_dmi"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        start = self.val['m_dmi_start_address'].format_string(format='x')
        end = self.val['m_dmi_end_address'].format_string(format='x')
        dmi = self.val['m_dmi_ptr'].format_string(format='x')

        access = self.val['m_dmi_access']
        trd = self.val['m_dmi_read_latency']
        twr = self.val['m_dmi_write_latency']

        s = ''
        if int(trd['m_value']) > 0:
            s = s + ' latency_r:' + str(trd)
        if int(twr['m_value']) > 0:
            s = s + ' latency_w:' + str(twr)

        return f'tlm_dmi {{ {access}, {start}..{end} -> {dmi}, r:{trd}, w:{twr} }}'

systemc.add_printer('tlm_dmi_access', '^tlm::tlm_dmi::dmi_access_e', TlmDmiAccessPrinter)
systemc.add_printer('tlm_dmi', '^tlm::tlm_dmi$', TlmDmiPrinter)
