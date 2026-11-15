##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

TEST_SEQUENCE = [
    {
        "name": "can_frame_empty",
        "expOutput": "can_frame { id = 0x000, dlc = 0x0, data = {  } }",
        "desc": "vcml::can - empty frame",
    },
    {
        "name": "can_frame_normal",
        "expOutput": "can_frame { id = 0x123, dlc = 0x4, data = { 11 22 33 44 } }",
        "desc": "vcml::can - regular frame",
    },
    {
        "name": "can_frame_eff",
        "expOutput": "can_frame { id = 0x1a2b3c4d, dlc = 0x4, data = { 11 22 33 44 } }",
        "desc": "vcml::can - EFF frame",
    },
    {
        "name": "can_frame_rtr",
        "expOutput": "can_frame { id = 0x123, dlc = 0x8, data = { 00 00 00 00 00 00 00 00 } [RTR] }",
        "desc": "vcml::can - RTR frame",
    },
    {
        "name": "can_frame_err",
        "expOutput": "can_frame { id = 0x456, dlc = 0x2, data = { de ad } [ERR] }",
        "desc": "vcml::can - ERR frame",
    },
    {
        "name": "can_frame_fdf",
        "expOutput": "can_frame { id = 0x123, dlc = 0x5, data = { 00 aa bb cc dd } [FDF] }",
        "desc": "vcml::can - regular FD frame",
    },
    {
        "name": "can_frame_brs",
        "expOutput": "can_frame { id = 0x123, dlc = 0x1, data = { ff } [BRS,FDF] }",
        "desc": "vcml::can - BRS FD frame",
    },
    {
        "name": "can_frame_esi",
        "expOutput": "can_frame { id = 0x123, dlc = 0x2, data = { 11 22 } [ESI,FDF] }",
        "desc": "vcml::can - ESI FD frame",
    },
    {
        "name": "can_frame_xl_normal",
        "expOutput": "can_frame { id = 0x055, vcid = 0x02, dlc = 0xc, sdt = 0x00, af = 0x12345678, data = { 01 02 03 04 05 06 07 08 09 0a 0b 0c } [XLF] }",
        "desc": "vcml::can - CAN XL frame",
    },
    {
        "name": "can_frame_xl_sec_rrs",
        "expOutput": "can_frame { id = 0x1aa, vcid = 0x07, dlc = 0x2, sdt = 0x01, af = 0xdeadbeef, data = { aa bb } [SEC,RRS,XLF] }",
        "desc": "vcml::can - CAN XL frame with SEC and RRS",
    },
    {
        "name": "eth_frame_invalid",
        "expOutput": "ethernet_frame { ETHERNET_INVALID }",
        "desc": "vcml::eth - invalid frame",
    },
    {
        "name": "eth_frame_empty",
        "expOutput": "ethernet_frame { ETHERNET_EMPTY }",
        "desc": "vcml::eth - empty, zero sized frame",
    },
    {
        "name": "eth_frame_min",
        "expOutput": "ethernet_frame { IEEE802.3, 60bytes, from = 00:00:00:00:00:00, to = 00:00:00:00:00:00, data = { 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 } }",
        "desc": "vcml::eth - empty, regular sized frame",
    },
    {
        "name": "eth_frame_multicast",
        "expOutput": "ethernet_frame { IEEE802.3, 60bytes, from = 12:23:34:45:56:67, to = ff:ff:ff:ff:ff:ff (MULTICAST), data = { ff ff ff ff ff ff 12 23 34 45 56 67 00 04 11 22 33 44 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 } }",
        "desc": "vcml::eth - multicast frame",
    },
    {
        "name": "mac_empty",
        "expOutput": "00:00:00:00:00:00",
        "desc": "vcml::mac_addr - empty",
    },
    {
        "name": "mac_normal",
        "expOutput": "12:23:34:45:56:67",
        "desc": "vcml::mac_addr - regular",
    },
    {
        "name": "range_normal",
        "expOutput": "{start = 0xab, end = 0xcd}",
        "desc": "vcml::range - regular",
    },
    {
        "name": "reg_peripheral.reg_u32",
        "expOutput": '0x12345678 "reg_peripheral.reg_u32"',
        "desc": "vcml::reg<u32>",
    },
    {
        "name": "reg_peripheral.reg_u8_array",
        "expOutput": '{ 0xaa 0xbb 0xcc 0xdd } "reg_peripheral.reg_u8_array"',
        "desc": "vcml::reg<u8> - (array)",
    },
    {
        "name": "prop_component.prop_str",
        "expOutput": '"prop_component.prop_str" = "hello world"',
        "desc": "vcml::property<std::string>",
    },
    {
        "name": "prop_component.prop_u64",
        "expOutput": '"prop_component.prop_u64" = 1311768467463790320',
        "desc": "vcml::property<u64>",
    },
    {
        "name": "prop_component.not_inited",
        "expOutput": '"prop_component.prop_not_inited" (uninitialized), default val = 42',
        "desc": "vcml::property<u32> - uninitialized",
    },
    {
        "name": "prop_component.prop_array",
        "expOutput": '"prop_component.prop_array" = {\n  [0] = 0,\n  [1] = 1,\n  [2] = 2,\n  [3] = 3\n}',
        "desc": "vcml::property<u32,4>",
    },
    {
        "name": "prop_component.prop_range",
        "expOutput": '"prop_component.prop_range" = {start = 0x10, end = 0x1f}',
        "desc": "vcml::property<vcml::range>",
    },
    {
        "name": "prop_component.prop_void",
        "expOutput": '"prop_component.prop_void" = {[#0] = 0xaabbccdd, [#1] = 0x11223344}',
        "desc": "vcml::property<void>",
    },
    {
        "name": "prop_component.prop_vector",
        "expOutput": '"prop_component.prop_vector" = std::vector of length 4, capacity 4 = {\n  [0] = -1,\n  [1] = -2,\n  [2] = -3,\n  [3] = -4\n}',
        "desc": "vcml::property<std::vector<i32>>",
    },
    {
        "name": "sbi_insn",
        "expOutput": "tlm_sbi { cpuid: 0x0, priv: 0x0, asid: 0x1, atype: SBI_ATYPE_UX, insn }",
        "desc": "vcml::tlm_sbi - insn",
    },
    {
        "name": "sbi_excl",
        "expOutput": "tlm_sbi { cpuid: 0x0, priv: 0x0, asid: 0x3, atype: SBI_ATYPE_UX, excl }",
        "desc": "vcml::tlm_sbi - excl",
    },
    {
        "name": "sbi_debug",
        "expOutput": "tlm_sbi { cpuid: 0x0, priv: 0x0, asid: 0x4, atype: SBI_ATYPE_UX, debug,nodmi }",
        "desc": "vcml::tlm_sbi - debug & nodmi",
    },
    {
        "name": "sbi_secure",
        "expOutput": "tlm_sbi { cpuid: 0x0, priv: 0x0, asid: 0x5, atype: SBI_ATYPE_UX, sync,secure }",
        "desc": "vcml::tlm_sbi - secure & sync",
    },
    {
        "name": "tlm_gp_read",
        "expOutput": "tlm_generic_payload { TLM_READ_COMMAND, addr = 0x0, data = nullptr, TLM_INCOMPLETE_RESPONSE }",
        "desc": "tlm::tlm_generic_payload - read cmd, empty",
    },
    {
        "name": "tlm_gp_write_ok",
        "expOutput": "tlm_generic_payload { TLM_WRITE_COMMAND, addr = 0x123, data = { ab bc cd de ef }, TLM_OK_RESPONSE }",
        "desc": "tlm::tlm_generic_payload - write cmd, ok",
    },
    {
        "name": "tlm_gp_be",
        "expOutput": "tlm_generic_payload { TLM_WRITE_COMMAND, addr = 0x456, data = { -- bc invalid -- ef }, TLM_GENERIC_ERROR_RESPONSE }",
        "desc": "tlm::tlm_generic_payload - write cmd + byte enabled, generic error",
    },
    {
        "name": "tlm_gp_sbiext",
        "expOutput": "tlm_generic_payload { TLM_READ_COMMAND, addr = 0x0, data = nullptr, TLM_INCOMPLETE_RESPONSE, 1 extension(s) }",
        "desc": "tlm::tlm_generic_payload - read cmd, empty, sbiext",
    },
    {
        "name": "dmi_none",
        "expOutput": "tlm_dmi { DMI_ACCESS_NONE, 0x0..0xff -> 0x0, r:0s, w:0s }",
        "desc": "tlm::tlm_dmi - nullptr, none",
    },
    {
        "name": "dmi_rw",
        "expOutput": "tlm_dmi { DMI_ACCESS_READ_WRITE, 0x10..0x20 -> 0x424242, r:0s, w:0s }",
        "desc": "tlm::tlm_dmi - regular, rw",
    },
    {
        "name": "dmi_latency",
        "expOutput": "tlm_dmi { DMI_ACCESS_READ_WRITE, 0xa..0xf -> 0x424242, r:5s, w:10s }",
        "desc": "tlm::tlm_dmi - regular, rw, latency",
    },
    {
        "name": "gpio_component.gpio_out_0",
        "expOutput": '"gpio_component.gpio_out_0" = true',
        "desc": "gpio_initiator_socket - set (vector: 42)",
    },
    {
        "name": "gpio_component.gpio_out_1",
        "expOutput": '"gpio_component.gpio_out_1" = false',
        "desc": "gpio_initiator_socket - not set",
    },
    {
        "name": "gpio_component.gpio_in",
        "expOutput": '"gpio_component.gpio_in" = true',
        "desc": "gpio_target_socket - set",
    },
    {
        "name": "gpio_component.gpio_arr_out",
        "expOutput": '"gpio_component.gpio_arr_out" = { [2] = true }',
        "desc": "gpio_initiator_array<8> - set (idx: 2, vector: 42)",
    },
    {
        "name": "gpio_component.gpio_arr_in",
        "expOutput": '"gpio_component.gpio_arr_in" = { [5] = false, [4] = true }',
        "desc": "gpio_target_array<8> - idx 4 set, idx 5 not set",
    },
    {
        "name": "scport_module.in",
        "expOutput": '"scport_module.in" = false',
        "desc": "sc_in<bool>",
    },
    {
        "name": "scport_module.out",
        "expOutput": '"scport_module.out" = false',
        "desc": "sc_out<bool>",
    },
    {
        "name": "scport_module.inout",
        "expOutput": '"scport_module.inout" = false',
        "desc": "sc_inout<bool>",
    },
]


def export_expected_output(path="expected_output.md"):
    with open(path, "w") as out_file:
        out_file.write("# Expected output of pretty printers\n")
        for test in TEST_SEQUENCE:
            if test["desc"] is None:
                desc = test["name"]
            else:
                desc = test["desc"]
            out_file.writelines(f"## `{desc}`\n```c\n{test['expOutput']}\n```\n\n")
        print(f"*** Expected output can be found in: {out_file.name} ***")
