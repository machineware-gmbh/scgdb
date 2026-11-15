##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

SET(VCML_USE_SDL2 OFF CACHE BOOL "Disable SDL2")
SET(VCML_USE_VNC OFF CACHE BOOL "Disable VNC")
SET(VCML_USE_RFB OFF CACHE BOOL "Disable RFB")
SET(VCML_USE_SLIRP OFF CACHE BOOL "Disable SLiRP")
SET(VCML_USE_TAP OFF CACHE BOOL "Disable TAP")
SET(VCML_USE_LUA OFF CACHE BOOL "Disable Lua")
SET(VCML_USE_SOCKETCAN OFF CACHE BOOL "Disable SocketCAN")
SET(VCML_USE_USB OFF CACHE BOOL "Disable USB")
SET(VCML_BUILD_UTILS OFF CACHE BOOL "Disable Utils")
find_github_repo(vcml "machineware-gmbh/vcml")

add_executable(pretty-printers
    pretty-printers.cpp
    can.cpp
    eth.cpp
    property.cpp
    range.cpp
    reg.cpp
    sbi.cpp
    tlm_dmi_access.cpp
    tlm_generic_payload.cpp
    gpio.cpp
    sc_ports.cpp
)
target_link_whole_archives(pretty-printers vcml)
target_compile_features(pretty-printers PUBLIC cxx_std_17)
