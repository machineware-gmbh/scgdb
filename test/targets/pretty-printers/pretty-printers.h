/******************************************************************************
 *                                                                            *
 * Copyright (C) 2026 MachineWare GmbH                                        *
 * All Rights Reserved                                                        *
 *                                                                            *
 * This work is licensed under the terms described in the LICENSE file found  *
 * in the root directory of this source tree.                                 *
 *                                                                            *
 ******************************************************************************/

#include "vcml.h"

namespace vcml {

// can
extern can_frame can_frame_empty;
extern can_frame can_frame_normal;
extern can_frame can_frame_eff;
extern can_frame can_frame_rtr;
extern can_frame can_frame_err;
extern can_frame can_frame_fdf;
extern can_frame can_frame_brs;
extern can_frame can_frame_esi;
extern can_frame can_frame_xl_normal;
extern can_frame can_frame_xl_sec_rrs;

// ethernet
extern eth_frame eth_frame_invalid;
extern eth_frame eth_frame_empty;
extern eth_frame eth_frame_min;
extern eth_frame eth_frame_multicast;

extern mac_addr mac_empty;
extern mac_addr mac_normal;

// range
extern range range_normal;

// register
class reg_periph : public peripheral
{
public:
    reg<u32> reg_u32;
    reg<u8, 4> reg_u8_array;

    reg_periph(const sc_core::sc_module_name& nm = "reg_peripheral");
};

extern reg_periph reg_peripheral;

// property
class prop_comp : public component
{
public:
    property<std::string> prop_str;
    property<u64> prop_u64;
    property<u32> not_inited;
    property<u32, 4> prop_array;
    property<range> prop_range;
    property<void> prop_void;
    property<std::vector<i32>> prop_vector;

    prop_comp(const sc_core::sc_module_name& nm = "prop_component");
};

extern prop_comp prop_component;

// tlm_sbi
extern tlm_sbi sbi_insn;
extern tlm_sbi sbi_excl;
extern tlm_sbi sbi_debug;
extern tlm_sbi sbi_secure;

// gpio
class gpio_comp : public component
{
public:
    gpio_initiator_socket gpio_out_0;
    gpio_initiator_socket gpio_out_1;
    gpio_target_socket gpio_in;
    gpio_initiator_array<8> gpio_arr_out;
    gpio_target_array<8> gpio_arr_in;

    gpio_comp(const sc_core::sc_module_name& nm = "gpio_component");
};

extern gpio_comp gpio_component;

// sc_port
class scport_mod : public module
{
public:
    sc_core::sc_in<bool> in;
    sc_core::sc_out<bool> out;
    sc_core::sc_inout<bool> inout;
    sc_core::sc_signal<bool> s1;

    scport_mod(const sc_core::sc_module_name& nm = "scport_module");
};

extern scport_mod scport_module;

} // namespace vcml

namespace tlm {

// tlm_dmi_access
extern tlm_dmi dmi_none;
extern tlm_dmi dmi_rw;
extern tlm_dmi dmi_latency;

// tlm_generic_payload
extern tlm_generic_payload tlm_gp_read;
extern tlm_generic_payload tlm_gp_write_ok;
extern tlm_generic_payload tlm_gp_be;
extern tlm_generic_payload tlm_gp_sbiext;

} // namespace tlm
