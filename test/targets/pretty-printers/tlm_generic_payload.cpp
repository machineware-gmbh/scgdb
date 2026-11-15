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

tlm_generic_payload tlm_gp_read;
tlm_generic_payload tlm_gp_write_ok;
tlm_generic_payload tlm_gp_be;
tlm_generic_payload tlm_gp_sbiext;

static const tlm_sbi gp_sbiext = {
    0, 0, 0, 1, 0, 0, 0, SBI_ATYPE_UX, 0, SBI_PRIVILEGE_NONE, 1
};

static unsigned char data[] = { 0xab, 0xbc, 0xcd, 0xde, 0xef };
static unsigned char byte_en[] = { 0x0, 0xff, 0x42 };

static char init_tlm_gp() {
    tx_setup(tlm_gp_read, TLM_READ_COMMAND, 0x0, nullptr, 0);

    tx_setup(tlm_gp_write_ok, TLM_WRITE_COMMAND, 0x123, &data, 5);
    tlm_gp_write_ok.set_response_status(TLM_OK_RESPONSE);

    tx_setup(tlm_gp_be, TLM_WRITE_COMMAND, 0x456, &data, 5);
    tlm_gp_be.set_byte_enable_ptr(byte_en);
    tlm_gp_be.set_byte_enable_length(3);
    tlm_gp_be.set_response_status(TLM_GENERIC_ERROR_RESPONSE);

    tx_setup(tlm_gp_sbiext, TLM_READ_COMMAND, 0x0, nullptr, 0);
    tx_set_sbi(tlm_gp_sbiext, gp_sbiext);

    return 0;
}

static char _throwaway = init_tlm_gp();
