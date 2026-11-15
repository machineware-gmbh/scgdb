##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

cmake_minimum_required(VERSION 3.11)
project(scgdb-tests LANGUAGES C CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../cmake)
include(FindGithubRepo)
include(LinkWhole)

enable_testing()

add_subdirectory(targets)
add_subdirectory(test-scripts)

