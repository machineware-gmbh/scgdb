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

#include <vector>

using namespace vcml;

eth_frame init_eth_frame_invalid() {
    eth_frame tmp;
    tmp.clear();
    tmp.push_back(0x11);
    return tmp;
}

eth_frame eth_frame_invalid = init_eth_frame_invalid();
eth_frame eth_frame_empty = eth_frame();
eth_frame eth_frame_min = eth_frame(eth_frame::FRAME_MIN_SIZE);
eth_frame eth_frame_multicast = eth_frame(
    "ff:ff:ff:ff:ff:ff", "12:23:34:45:56:67", { 0x11, 0x22, 0x33, 0x44 });

mac_addr mac_empty = mac_addr();
mac_addr mac_normal = mac_addr("12:23:34:45:56:67");
