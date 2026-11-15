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

# canid flags
CAN_SID = 0x7FF
CAN_EID = 0x1FFFFFFF


class CanFramePrinter:
    def __init__(self, val):
        self.val = val
        self._canid = int(self.val["canid"])

    def _is_canxl(self):
        return bool(self.val["xlf"])

    def _is_canfd(self):
        return bool(self.val["fdf"]) and not self._is_canxl()

    def _is_eff(self):
        return bool(self.val["eff"])

    def _is_rtr(self):
        return bool(self.val["rtr"])

    def _is_err(self):
        return bool(self.val["err"])

    def _is_brs(self):
        return bool(self.val["brs"])

    def _is_esi(self):
        return bool(self.val["esi"])

    def _is_sec(self):
        return bool(self.val["sec"])

    def _is_rrs(self):
        return bool(self.val["rrs"])

    def _sdt(self):
        return int(self.val["sdt"])

    def _af(self):
        return int(self.val["af"])

    def _msgid(self):
        id = self._canid & (CAN_EID if self._is_eff() else CAN_SID)
        if self._is_eff():
            return f"0x{id:08x}"
        else:
            return f"0x{id:03x}"

    def _vcid(self):
        return int(self.val["vcid"])

    def _dlc(self):
        return int(self.val["dlc"])

    def _data(self):
        gdb.set_convenience_variable("val", self.val.reference_value())
        length = int(gdb.parse_and_eval("$val.length()"))
        data = [
            f"{int(gdb.parse_and_eval(f'(int)$val.data[{i}]')):02x}"
            for i in range(length)
        ]
        return " ".join(data)

    def _attrs(self):
        attrs = []
        if not self._is_canxl():
            if self._is_rtr():
                attrs.append("RTR")
            if self._is_err():
                attrs.append("ERR")
            if self._is_brs():
                attrs.append("BRS")
            if self._is_esi():
                attrs.append("ESI")
            if self._is_canfd():
                attrs.append("FDF")
        else:
            if self._is_sec():
                attrs.append("SEC")
            if self._is_rrs():
                attrs.append("RRS")
            attrs.append("XLF")
        return ",".join(attrs)

    def to_string(self):
        id = self._msgid()
        dlc = self._dlc()
        attrs = self._attrs()
        data = self._data()

        if not self._is_canxl():
            fields = f"id = {id}, dlc = 0x{dlc:x}, data = {{ {data} }}"
        else:
            sdt = self._sdt()
            af = self._af()
            fields = (
                f"id = {id}, vcid = 0x{self._vcid():02x}, "
                f"dlc = 0x{dlc:x}, sdt = 0x{sdt:02x}, af = 0x{af:08x}, "
                f"data = {{ {data} }}"
            )

        if attrs:
            return f"can_frame {{ {fields} [{attrs}] }}"
        else:
            return f"can_frame {{ {fields} }}"


vcml.add_printer("vcml::can_frame", "^vcml::can_frame$", CanFramePrinter)
