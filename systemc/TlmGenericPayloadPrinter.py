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

import systemc


class TlmCommandPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        cmd = int(self.val)
        if cmd == 0:
            return "TLM_READ_COMMAND"
        if cmd == 1:
            return "TLM_WRITE_COMMAND"
        if cmd == 2:
            return "TLM_IGNORE_COMMAND"
        return "TLM_INVALID_COMMAND"


class TlmResponseStatus:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        resp = int(self.val)
        if resp == 1:
            return "TLM_OK_RESPONSE"
        if resp == 0:
            return "TLM_INCOMPLETE_RESPONSE"
        if resp == -1:
            return "TLM_GENERIC_ERROR_RESPONSE"
        if resp == -2:
            return "TLM_ADDRESS_ERROR_RESPONSE"
        if resp == -3:
            return "TLM_COMMAND_ERROR_RESPONSE"
        if resp == -4:
            return "TLM_BURST_ERROR_RESPONSE"
        if resp == -5:
            return "TLM_BYTE_ENABLE_ERROR_RESPONSE"
        return "TLM_UNKNOWN_RESPONSE"


class TlmGenericPayloadPrinter:
    def __init__(self, val):
        self.val = val

    def parse_data(self):
        len = int(self.val["m_length"])
        if len == 0 or not self.val["m_data"]:
            return None

        data = self.val["m_data"]
        byte_enable = self.val["m_byte_enable"]
        byte_enable_len = int(self.val["m_byte_enable_length"])

        gdb.set_convenience_variable("data", data)
        gdb.set_convenience_variable("be", byte_enable)
        char_pointer_type = gdb.lookup_type("unsigned char").pointer()
        byte_enable_available = byte_enable_len != 0 and byte_enable.address is not None

        result = []
        for idx in range(len):
            val = int(
                gdb.parse_and_eval(f"$data+{idx}").cast(char_pointer_type).dereference()
            )
            if byte_enable_available:
                be_idx = idx % byte_enable_len
                enabled = int(
                    gdb.parse_and_eval(f"$be+{be_idx}")
                    .cast(char_pointer_type)
                    .dereference()
                )
                if enabled == 0x0:
                    result.append("--")
                elif enabled == 0xFF:
                    result.append(f"{val:02x}")
                else:
                    result.append("invalid")
            else:
                result.append(f"{val:02x}")
        return " ".join(result)

    def to_string(self):
        cmd = self.val["m_command"]
        addr = self.val["m_address"].format_string(format="x")
        resp_status = self.val["m_response_status"]
        dat = self.parse_data()
        if dat:
            dat = f"{{ {dat} }}"
        else:
            dat = "nullptr"

        nr_exts = 0
        gdb.set_convenience_variable("gp", self.val.reference_value())
        for i in range(int(gdb.parse_and_eval("$gp.m_extensions.size()"))):
            if gdb.parse_and_eval(f"$gp.get_extension({i})"):
                nr_exts += 1

        if nr_exts:
            return f"tlm_generic_payload {{ {cmd}, addr = {addr}, data = {dat}, {resp_status}, {nr_exts} extension(s) }}"
        else:
            return f"tlm_generic_payload {{ {cmd}, addr = {addr}, data = {dat}, {resp_status} }}"


systemc.add_printer("tlm_command", "^tlm::tlm_command$", TlmCommandPrinter)
systemc.add_printer(
    "tlm_response_status", "^tlm::tlm_response_status$", TlmResponseStatus
)
systemc.add_printer(
    "tlm_generic_payload", "^tlm::tlm_generic_payload$", TlmGenericPayloadPrinter
)
