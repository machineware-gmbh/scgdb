##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

find_package(Python3 "3.3" REQUIRED)

macro(cfg_test_file file)
    configure_file(${file}.in ${file} @ONLY)
    file(GENERATE OUTPUT ${file} INPUT ${CMAKE_CURRENT_BINARY_DIR}/${file})
endmacro()

get_filename_component(SCGDB_ROOT ${PROJECT_SOURCE_DIR} DIRECTORY)

add_subdirectory(sc_commands)

cfg_test_file(test_nonsysc.py)
add_test(NAME test_nonsysc COMMAND ${Python3_EXECUTABLE} test_nonsysc.py WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})

cfg_test_file(test_pretty-printers.py)
add_test(NAME test_pretty-printers COMMAND ${Python3_EXECUTABLE} test_pretty-printers.py WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
configure_file(PrinterExpOutput.py ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)
