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

tlm_sbi sbi_insn = { 0, 0, 0, 1, 0, 0, 0, SBI_ATYPE_UX, 0, SBI_PRIVILEGE_NONE,
                     1 };
tlm_sbi sbi_excl = { 0, 0, 0, 0, 1, 0, 0, SBI_ATYPE_UX, 0, SBI_PRIVILEGE_NONE,
                     3 };
tlm_sbi sbi_debug = { 1, 1, 0, 0, 0, 0, 0, SBI_ATYPE_UX, 0, SBI_PRIVILEGE_NONE,
                      4 };
tlm_sbi sbi_secure = {
    0, 0, 1, 0, 0, 0, 1, SBI_ATYPE_UX, 0, SBI_PRIVILEGE_NONE, 5
};
