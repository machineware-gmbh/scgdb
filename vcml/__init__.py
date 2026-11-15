##############################################################################
#                                                                            #
# Copyright (C) 2026 MachineWare GmbH                                        #
# All Rights Reserved                                                        #
#                                                                            #
# This work is licensed under the terms described in the LICENSE file found  #
# in the root directory of this source tree.                                 #
#                                                                            #
##############################################################################

import os

import gdb
import gdb.printing

_vcml_printers = gdb.printing.RegexpCollectionPrettyPrinter("vcml")
gdb.printing.register_pretty_printer(None, _vcml_printers)


def add_printer(name, regex, printer):
    _vcml_printers.add_printer(name, regex, printer)


from .CanFramePrinter import CanFramePrinter
from .EthFramePrinter import EthFramePrinter, MacAddrPrinter
from .PropertyPrinter import (
    PropertyPrinter,
    PropertyPrinterArrayLike,
    PropertyPrinterString,
    PropertyPrinterVector,
    PropertyPrinterVoid,
)
from .RangePrinter import RangePrinter
from .RegPrinter import RegPrinter
from .TlmSbiPrinter import TlmSbiPrinter

# Search for libstdc++ printer module
# The printers will not be registered if it cannot be found
for subdir in os.listdir("/usr/share"):
    if subdir.startswith("gcc"):
        import sys

        sys.path.insert(0, f"/usr/share/{subdir}/python")
        from .GpioSocketPrinter import (
            GpioArrayPrinter,
            GpioInitiatorSocketPrinter,
            GpioTargetSocketPrinter,
        )
