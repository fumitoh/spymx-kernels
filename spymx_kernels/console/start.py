# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2009- Spyder Kernels Contributors
#
# Licensed under the terms of the MIT License
# (see spyder_kernels/__init__.py for details)
# -----------------------------------------------------------------------------

"""
File used to start kernels for the IPython Console
"""

# Standard library imports
import os
import os.path as osp
import sys
import site

# Third-party imports
from traitlets import DottedObjectName

# Local imports

from spyder_kernels.console.start import import_spydercustomize
from spyder_kernels.console.start import kernel_config
from spyder_kernels.console.start import varexp



def main():
    # Remove this module's path from sys.path:
    try:
        sys.path.remove(osp.dirname(__file__))
    except ValueError:
        pass

    try:
        locals().pop('__file__')
    except KeyError:
        pass
    __doc__ = ''
    __name__ = '__main__'

    # Import our customizations into the kernel
    import_spydercustomize()

    # Remove current directory from sys.path to prevent kernel
    # crashes when people name Python files or modules with
    # the same name as standard library modules.
    # See spyder-ide/spyder#8007
    while '' in sys.path:
        sys.path.remove('')

    # Main imports
    from ipykernel.kernelapp import IPKernelApp
    from spymx_kernels.console.kernel import ModelxKernel

    class SpyderKernelApp(IPKernelApp):

        outstream_class = DottedObjectName(
            'spyder_kernels.console.outstream.TTYOutStream')

        def init_pdb(self):
            """
            This method was added in IPykernel 5.3.1 and it replaces
            the debugger used by the kernel with a new class
            introduced in IPython 7.15 during kernel's initialization.
            Therefore, it doesn't allow us to use our debugger.
            """
            pass

        def close(self):
            """Close the loopback socket."""
            socket = self.kernel.loopback_socket
            if socket and not socket.closed:
                socket.close()
            return super().close()

    # Fire up the kernel instance.
    kernel = SpyderKernelApp.instance()
    kernel.kernel_class = ModelxKernel
    try:
        kernel.config = kernel_config()
    except:
        pass
    kernel.initialize()

    # Set our own magics
    kernel.shell.register_magic_function(varexp)

    # Set Pdb class to be used by %debug and %pdb.
    # This makes IPython consoles to use the class defined in our
    # sitecustomize instead of their default one.
    import pdb
    kernel.shell.InteractiveTB.debugger_cls = pdb.Pdb

    # Start the (infinite) kernel event loop.
    kernel.start()


if __name__ == '__main__':
    main()
