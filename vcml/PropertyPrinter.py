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
import vcml


def get_fullname(property):
    try:
        name = utils.read_std_string(property['m_fullname'])
        return f'"{name}"'
    except (gdb.error, UnicodeDecodeError):
        return '""'

class PropertyPrinter:
    """Pretty printer for vcml::property<T, 1>"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        if self.val['m_inited']:
            init = ""
            values = self.val['m_value'][0].format_string()
        else:
            init = ' (uninitialized), default val'
            values = self.val['m_defval'][0].format_string()
        return f'{get_fullname(self.val)}{init} = {values}'

class PropertyPrinterString:
    """Pretty printer for vcml::property<std::__cxx11::basic_string<.*>, 1>"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        if self.val['m_inited']:
            init = ""
            values = utils.read_std_string(self.val['m_value'])
        else:
            init = ' (uninitialized), default val'
            values = utils.read_std_string(self.val['m_defval'])
        return f'{get_fullname(self.val)}{init} = "{values}"'

class PropertyPrinterArrayLike:
    """Pretty printer for vcml::property<T, N>"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        if self.val['m_inited']:
            init = ""
            values = self.val['m_value'].format_string(pretty_arrays=True, array_indexes=True)
        else:
            init = ' (uninitialized), default val'
            values = self.val['m_defval'].format_string(pretty_arrays=True, array_indexes=True)
        return f'{get_fullname(self.val)}{init} = {values}'

class PropertyPrinterVector:
    """Pretty printer for vcml::property<vector<T>, 1>"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        if self.val['m_inited']:
            init = ""
            values = self.val['m_val'].format_string(pretty_arrays=True, array_indexes=True)
        else:
            init = ' (uninitialized), default val'
            values = self.val['m_def'].format_string(pretty_arrays=True, array_indexes=True)
        return f'{get_fullname(self.val)}{init} = {values}'

class PropertyPrinterVoid:
    """Pretty printer for vcml::property<void, N>"""

    def __init__(self, val):
        self.val = val

    def children(self):
        if self.val['m_inited']:
            size = self.val['m_size']
            if size == 1:
                type = gdb.lookup_type("mwr::u8")
            elif size == 2:
                type = gdb.lookup_type("mwr::u16")
            elif size == 4:
                type = gdb.lookup_type("mwr::u32")
            elif size == 8:
                type = gdb.lookup_type("mwr::u64")
            else:
                type = gdb.lookup_type("void")
            gdb.set_convenience_variable('dat', self.val['m_data'])
            idx = 0
            while True:
                if idx >= self.val['m_count']:
                    return None
                res = f'[#{idx}]', gdb.parse_and_eval(f'$dat+{size}*{idx}').cast(type.pointer()).dereference().format_string(format='x')
                idx += 1
                yield (res)
        else:
            data = [
                ("[default]", self.val['m_default'].format_string(format='x')),
            ]
            return iter(data)

    def to_string(self):
        if self.val['m_inited']:
            return f'{get_fullname(self.val)}'
        else:
            return f'{get_fullname(self.val)} (uninitialized)'


vcml.add_printer('vcml::property', '^vcml::property<(?!std::vector|void|std::__cxx11::basic_string<.*>).*, 1>$', PropertyPrinter)
vcml.add_printer('vcml::property', '^vcml::property<std::__cxx11::basic_string<.*>, 1>$', PropertyPrinterString)
vcml.add_printer('vcml::property', '^vcml::property<(?!std::vector|void|std::__cxx11::basic_string<.*>).*, .*>$', PropertyPrinterArrayLike)
vcml.add_printer('vcml::property', '^vcml::property<std::vector<.*>, 1>$', PropertyPrinterVector)
vcml.add_printer('vcml::property', '^vcml::property<void, .*>$', PropertyPrinterVoid)
