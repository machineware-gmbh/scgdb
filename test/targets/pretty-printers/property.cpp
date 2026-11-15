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

prop_comp prop_component;

prop_comp::prop_comp(const sc_core::sc_module_name& nm):
    component(nm),
    prop_str("prop_str", "abc"),
    prop_u64("prop_u64", 0xffffffffffffffff),
    not_inited("prop_not_inited", 42),
    prop_array("prop_array", 7),
    prop_range("prop_range", { 1, 2 }),
    prop_void("prop_void", 4, 2),
    prop_vector("prop_vector", { 1, 2, 3 }) {
    prop_str = "hello world";
    prop_u64 = 0x123456789abcdef0;
    prop_array.set(0, 0);
    prop_array.set(1, 1);
    prop_array.set(2, 2);
    prop_array.set(3, 3);
    prop_range = range(0x10, 0x1f);
    prop_void.assign({ "0xaabbccdd", "0x11223344" });
    prop_vector.set({ -1, -2, -3, -4 });
}
