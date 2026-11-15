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


class TlmSbiPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        cpuid = self.val['cpuid'].format_string(format='x')
        privilege = self.val['privilege'].format_string(format='x')
        asid = self.val['asid'].format_string(format='x')

        if self.val['atype'] == 0:
            atype = "SBI_ATYPE_UX"
        elif self.val['atype'] == 1:
            atype = "SBI_ATYPE_RQ"
        elif self.val['atype'] == 2:
            atype = "SBI_ATYPE_TX"
        else:
            atype = ""

        attrs = []
        if self.val['is_debug']:
            attrs.append('debug')
        if self.val['is_nodmi']:
            attrs.append('nodmi')
        if self.val['is_sync']:
            attrs.append('sync')
        if self.val['is_insn']:
            attrs.append('insn')
        if self.val['is_excl']:
            attrs.append('excl')
        if self.val['is_lock']:
            attrs.append('lock')
        if self.val['is_secure']:
            attrs.append('secure')
        attrs = ','.join(attrs)
        if attrs:
            return f'tlm_sbi {{ cpuid: {cpuid}, priv: {privilege}, asid: {asid}, atype: {atype}, {attrs} }}'
        else:
            return f'tlm_sbi {{ cpuid: {cpuid}, priv: {privilege}, asid: {asid}, atype: {atype} }}'

vcml.add_printer('tlm_sbi', 'vcml::tlm_sbi', TlmSbiPrinter)
