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

scport_mod::scport_mod(const sc_core::sc_module_name& nm):
    module(nm), in("in"), out("out"), inout("inout"), s1("s1") {
    in.bind(s1);
    out.bind(s1);
    inout.bind(s1);
}

scport_mod scport_module;
