##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

macro(cmd_test test)
    set(script test_${test}.py)
    cfg_test_file(${script})
    add_test(NAME test_${test} COMMAND ${Python3_EXECUTABLE} ${script} WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
endmacro()

cmd_test("info_scthreads")
cmd_test("sc_delta-count")
cmd_test("sc_status")
cmd_test("sc_time")
cmd_test("scthreads")
