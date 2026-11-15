##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

SYSTEMC_HOME ?= /usr/lib/systemc
TARGET_ARCH ?= linux64

SYSTEMC_INC_DIR ?= $(SYSTEMC_HOME)/include
SYSTEMC_LIB_DIR ?= $(SYSTEMC_HOME)/lib-$(TARGET_ARCH)

CXXFLAGS := -g -Wall -pedantic -I$(SYSTEMC_INC_DIR) -std=c++17
LDFLAGS  := -L$(SYSTEMC_LIB_DIR) -L$(SYSTEMC_HOME)/lib -lsystemc -static -std=c++17

.PHONY: all clean run debug

all: example

example: src/example.o
	$(CXX) -o $@ $^ $(LDFLAGS)

src/%.o: src/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	$(RM) src/example.o example

run: example
	./example

debug: example
	gdb example
