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

from systemc.helper.Quickthreads import get_qt_member
from systemc.helper.SystemCVersion import get_sysc_ver

CURR_ARCH = None


def get_cor_regs(scth):
    global CURR_ARCH
    sp = get_qt_member(scth, "m_sp")
    if sp is None:
        raise RuntimeError("Could not find a Stack pointer!")

    if CURR_ARCH is None:
        arch_name = gdb.selected_frame().architecture().name()
        if arch_name == "i386:x86-64":
            CURR_ARCH = {
                "get_cor_regs": get_cor_regs_x86_64,
                "stack_sw_addr": stack_sw_addr_x86_64(),
            }
        elif arch_name == "aarch64":
            CURR_ARCH = {
                "get_cor_regs": get_cor_regs_aarch64,
                "stack_sw_addr": stack_sw_addr_aarch64(),
            }
        else:
            raise RuntimeError("Unsupported architecture")

    return CURR_ARCH["get_cor_regs"](sp)


def get_cor_regs_x86_64(sp):
    gdb.set_convenience_variable("thr_sp", int(sp))
    cor_regs = {
        "rsp": sp,
        "rsi": gdb.parse_and_eval("*(long*)($thr_sp)"),
        "rdi": gdb.parse_and_eval("*(long*)($thr_sp+8)"),
        "rdx": gdb.parse_and_eval("*(long*)($thr_sp+8*2)"),
        "rcx": gdb.parse_and_eval("*(long*)($thr_sp+8*3)"),
        "rbx": gdb.parse_and_eval("*(long*)($thr_sp+8*4)"),
        "r15": gdb.parse_and_eval("*(long*)($thr_sp+8*5)"),
        "r14": gdb.parse_and_eval("*(long*)($thr_sp+8*6)"),
        "r13": gdb.parse_and_eval("*(long*)($thr_sp+8*7)"),
        "r12": gdb.parse_and_eval("*(long*)($thr_sp+8*8)"),
        "rip": CURR_ARCH["stack_sw_addr"],
    }
    if get_sysc_ver() <= (2, 3, 0):
        cor_regs["r11"] = gdb.parse_and_eval("*(long*)($thr_sp+8*9)")
        cor_regs["r10"] = gdb.parse_and_eval("*(long*)($thr_sp+8*10)")
        cor_regs["r9"] = gdb.parse_and_eval("*(long*)($thr_sp+8*11)")
        cor_regs["r8"] = gdb.parse_and_eval("*(long*)($thr_sp+8*12)")
        cor_regs["rbp"] = sp + 8 * 13
    else:
        cor_regs["rbp"] = sp + 8 * 10
    return cor_regs


def get_cor_regs_aarch64(sp):
    sp = int(sp)
    if get_sysc_ver() < (3, 0, 0):
        gdb.set_convenience_variable("thr_sp", int(sp))
    else:
        gdb.set_convenience_variable("thr_sp", int(sp) + 160)
    cor_regs = {
        "sp": sp,
        "pc": CURR_ARCH["stack_sw_addr"],
        "x30": gdb.parse_and_eval("*(long*)($thr_sp-8)"),
        "x29": gdb.parse_and_eval("*(long*)($thr_sp-8*2)"),
        "x28": gdb.parse_and_eval("*(long*)($thr_sp-8*3)"),
        "x27": gdb.parse_and_eval("*(long*)($thr_sp-8*4)"),
        "x26": gdb.parse_and_eval("*(long*)($thr_sp-8*5)"),
        "x25": gdb.parse_and_eval("*(long*)($thr_sp-8*6)"),
        "x24": gdb.parse_and_eval("*(long*)($thr_sp-8*7)"),
        "x23": gdb.parse_and_eval("*(long*)($thr_sp-8*8)"),
        "x22": gdb.parse_and_eval("*(long*)($thr_sp-8*9)"),
        "x21": gdb.parse_and_eval("*(long*)($thr_sp-8*10)"),
        "x20": gdb.parse_and_eval("*(long*)($thr_sp-8*11)"),
        "x19": gdb.parse_and_eval("*(long*)($thr_sp-8*12)"),
        "d15.u": gdb.parse_and_eval("*(long*)($thr_sp-8*13)"),
        "d14.u": gdb.parse_and_eval("*(long*)($thr_sp-8*14)"),
        "d13.u": gdb.parse_and_eval("*(long*)($thr_sp-8*15)"),
        "d12.u": gdb.parse_and_eval("*(long*)($thr_sp-8*16)"),
        "d11.u": gdb.parse_and_eval("*(long*)($thr_sp-8*17)"),
        "d10.u": gdb.parse_and_eval("*(long*)($thr_sp-8*18)"),
        "d9.u": gdb.parse_and_eval("*(long*)($thr_sp-8*19)"),
        "d8.u": gdb.parse_and_eval("*(long*)($thr_sp-8*20)"),
    }
    return cor_regs


def disasm_qt_block():
    return gdb.execute("disassemble qt_block", False, True).splitlines()[1:-1]


def stack_sw_addr_aarch64():
    """Get address of instruction where stacks are swapped (aarch64)"""
    disasm = disasm_qt_block()
    addr = disasm[12] if get_sysc_ver() < (3, 0, 0) else disasm[13]
    return addr.lstrip().split()[0]


def stack_sw_addr_x86_64():
    """Get address of instruction where stacks are swapped (x86_64)"""
    disasm = disasm_qt_block()
    return disasm[14].lstrip().split()[0]
