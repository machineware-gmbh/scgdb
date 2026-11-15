/******************************************************************************
 *                                                                            *
 * Copyright (C) 2026 MachineWare GmbH                                        *
 * All Rights Reserved                                                        *
 *                                                                            *
 * This work is licensed under the terms described in the LICENSE file found  *
 * in the root directory of this source tree.                                 *
 *                                                                            *
 ******************************************************************************/

#include "pretty-printers.h"

using namespace vcml;

reg_periph::reg_periph(const sc_core::sc_module_name& nm):
    peripheral(nm, ENDIAN_LITTLE),
    reg_u32("reg_u32", 0x0, 0x12345678),
    reg_u8_array("reg_u8_array", 0x4, 0x0) {
    reg_u8_array[0] = 0xaa;
    reg_u8_array[1] = 0xbb;
    reg_u8_array[2] = 0xcc;
    reg_u8_array[3] = 0xdd;

    clk.stub();
    rst.stub();
}

reg_periph reg_peripheral;
