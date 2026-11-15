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

can_frame can_frame_empty = can_frame();

can_frame can_frame_normal = can_frame{
    .canid = 0x123,
    .dlc = 0x4,
    .data = { 0x11, 0x22, 0x33, 0x44 },
};

can_frame can_frame_eff = can_frame{
    .canid = 0x1a2b3c4d,
    .eff = 1,
    .dlc = 0x4,
    .data = { 0x11, 0x22, 0x33, 0x44 },
};

can_frame can_frame_rtr = can_frame{
    .canid = 0x123,
    .rtr = 1,
    .dlc = 0x8,

    .data = { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
};

can_frame can_frame_err = can_frame{
    .canid = 0x456,
    .err = 1,
    .dlc = 0x2,
    .data = { 0xde, 0xad },
};

can_frame can_frame_fdf = can_frame{ .canid = 0x123,
                                     .fdf = 1,
                                     .dlc = 0x5,
                                     .data = { 0x00, 0xaa, 0xbb, 0xcc,
                                               0xdd } };

can_frame can_frame_brs = can_frame{
    .canid = 0x123, .brs = 1, .fdf = 1, .dlc = 0x1, .data = { 0xff }
};

can_frame can_frame_esi = can_frame{
    .canid = 0x123, .esi = 1, .fdf = 1, .dlc = 0x2, .data = { 0x11, 0x22 }
};

can_frame can_frame_xl_normal = can_frame{
    .canid = 0x055,
    .xlf = 1,
    .dlc = 0xc,
    .sdt = 0x00,
    .vcid = 0x02,
    .af = 0x12345678,
    .data = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b,
              0x0c },
};

can_frame can_frame_xl_sec_rrs = can_frame{
    .canid = 0x1aa,
    .sec = 1,
    .rrs = 1,
    .xlf = 1,
    .dlc = 0x2,
    .sdt = 0x01,
    .vcid = 0x07,
    .af = 0xdeadbeef,
    .data = { 0xaa, 0xbb },
};
