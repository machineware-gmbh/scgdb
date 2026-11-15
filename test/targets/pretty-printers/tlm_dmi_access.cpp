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

tlm_dmi dmi_none;
tlm_dmi dmi_rw;
tlm_dmi dmi_latency;

static char init_tlm_dmi() {
    dmi_none.allow_none();
    dmi_none.set_start_address(0);
    dmi_none.set_end_address(0xff);
    dmi_none.set_dmi_ptr(nullptr);

    dmi_rw.allow_read_write();
    dmi_rw.set_start_address(0x10);
    dmi_rw.set_end_address(0x20);
    dmi_rw.set_dmi_ptr((unsigned char*)0x424242);

    dmi_latency.allow_read_write();
    dmi_latency.set_start_address(0xa);
    dmi_latency.set_end_address(0xf);
    dmi_latency.set_dmi_ptr((unsigned char*)0x424242);
    dmi_latency.set_read_latency(sc_time(5.0, SC_SEC));
    dmi_latency.set_write_latency(sc_time(10.0, SC_SEC));

    return 0;
}

static char _throwaway = init_tlm_dmi();
