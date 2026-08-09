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

try:
    # spyder-kernels 3.1.0 and later define SpyderKernelApp in its own module.
    # Reusing it, instead of re-deriving one from IPKernelApp here, is what
    # gives MxConsole kernels the SpyderParentPoller that kills them when
    # Spyder, their parent process, exits or crashes.
    # See spyder-ide/spyder#22414.
    from spyder_kernels.console.kernelapp import SpyderKernelApp
except ImportError:
    # spyder-kernels 3.0.x and earlier define SpyderKernelApp inside
    # start.main(), so it cannot be imported. main() below falls back to
    # defining an equivalent class. Those versions ship with Spyder 6.0 and
    # earlier, which do not set SPY_PARENT_PID, so there is no parent process
    # to poll for anyway.
    SpyderKernelApp = None



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

    if SpyderKernelApp is None:
        # Copied from spyder_kernels/console/start.py in spyder-kernels 3.0.5,
        # for spyder-kernels earlier than 3.1.0.
        class KernelApp(IPKernelApp):

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
    else:
        # outstream_class, init_pdb and close are all defined the same way
        # in spyder-kernels' own SpyderKernelApp, so nothing to override.
        # Only kernel_class is replaced, below, on the instance.
        KernelApp = SpyderKernelApp

    # Fire up the kernel instance.
    kernel = KernelApp.instance()
    kernel.kernel_class = ModelxKernel
    try:
        kernel.config = kernel_config()
    except:
        pass

    # Re-add current working directory path into sys.path after all of the
    # import statements, but before initializing the kernel.
    # SpyderKernel.__init__ snapshots sys.path during initialize(), and Spyder
    # rebuilds sys.path from that snapshot on every update_syspath call, so
    # inserting '' after initialize() would be wiped out later.
    # See fumitoh/spymx-kernels#11.
    if '' not in sys.path:
        sys.path.insert(0, '')

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
