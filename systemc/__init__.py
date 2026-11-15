##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

import gdb
import gdb.printing

_systemc_printers = gdb.printing.RegexpCollectionPrettyPrinter("systemc")
gdb.printing.register_pretty_printer(None, _systemc_printers)


def add_printer(name, regex, printer):
    _systemc_printers.add_printer(name, regex, printer)


import systemc.helper.SystemCVersion

from .InfoScthreadsCmd import InfoScthreadsCmd
from .ScCommands import ScCmd
from .ScPortsPrinter import ScPortInBoolPrinter, ScPortOutBoolPrinter
from .ScStatusPrinter import ScStatusPrinter
from .ScTimePrinter import ScTimePrinter
from .TlmDmiPrinter import TlmDmiPrinter
from .TlmGenericPayloadPrinter import TlmGenericPayloadPrinter
