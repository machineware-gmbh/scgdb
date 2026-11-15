##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

find_package(Threads REQUIRED)

if(NOT DEFINED SYSTEMC_HOME AND DEFINED ENV{SYSTEMC_HOME})
    set(SYSTEMC_HOME $ENV{SYSTEMC_HOME})
endif()
if(NOT DEFINED SYSTEMC_HOME)
    message(FATAL_ERROR "SYSTEMC_HOME is not set!")
endif()

if(NOT DEFINED TARGET_ARCH AND DEFINED ENV{TARGET_ARCH})
    set(TARGET_ARCH $ENV{TARGET_ARCH})
endif()
if(NOT DEFINED TARGET_ARCH)
    message(FATAL_ERROR "TARGET_ARCH is not set!")
endif()

add_executable(fizzbuzz "src/fizzbuzz.cpp")
target_compile_features(fizzbuzz PUBLIC cxx_std_17)
target_include_directories(fizzbuzz SYSTEM PUBLIC ${SYSTEMC_HOME}/include)

find_library(SYSTEMC_LIBRARIES NAME systemc PATHS ${SYSTEMC_HOME}/lib-${TARGET_ARCH} ${SYSTEMC_HOME}/lib)
target_link_libraries(fizzbuzz PUBLIC ${SYSTEMC_LIBRARIES} PUBLIC Threads::Threads)
