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

gpio_comp::gpio_comp(const sc_core::sc_module_name& nm):
    component(nm),
    gpio_out_0("gpio_out_0"),
    gpio_out_1("gpio_out_1"),
    gpio_in("gpio_in"),
    gpio_arr_out("gpio_arr_out"),
    gpio_arr_in("gpio_arr_in") {
    gpio_bind(*this, "gpio_out_0", *this, "gpio_arr_in", 4);
    gpio_bind(*this, "gpio_out_1", *this, "gpio_arr_in", 5);
    gpio_bind(*this, "gpio_arr_out", 2, *this, "gpio_in");
    gpio_out_0[42] = true;
    gpio_arr_out[2][42] = true;
}

gpio_comp gpio_component;
