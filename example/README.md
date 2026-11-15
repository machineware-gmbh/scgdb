# scgdb example

## Build
0. Fetch and build SystemC with debug symbols and static libraries:
    ```sh
    wget https://www.accellera.org/images/downloads/standards/systemc/systemc-2.3.2.tar.gz
    tar -xzf systemc-2.3.2.tar.gz && cd systemc-2.3.2
    export SYSTEMC_HOME=`pwd`
    export TARGET_ARCH=linux64
    mkdir BUILD && cd BUILD
    ../configure --prefix=$SYSTEMC_HOME --enable-debug --enable-static
    make -j 4 && make install
    ```
1. Run make in this folder. You may need to configure the `SYSTEMC_HOME` and `TARGET_ARCH` (`linux64` or `linuxaarch64`) variables according to your system.
    ```sh
    make SYSTEMC_HOME=<PATH_TO_SYSTEMC_BUILD> TARGET_ARCH=<YOUR_ARCHITECTURE>
    ```
2. Start the example with `make run` or start a gdb session with `make debug`. GDB should print `=== SystemC GDB extensions enabled ===` to indicate that scgdb has been loaded.

---

This folder contains the source of an example SystemC simulation to illustrate the capabilities of scgdb.

The simulation consists of a SystemC module (called `fizzbuzz`) with 3 SC_THREADs.

The first is the main thread (`fizzbuzz.thread_main`). It triggers the other threads based on the current simulation time. This is done via `sc_event`s.

The other threads (`fizzbuzz.thread_fizz` and `fizzbuzz.thread_buzz`) print a string to stdout upon receiving their event (either *FIZZ* or *BUZZ*). After that they will wait for the next event.

For a first debugging session with this example, see [Getting started](../docs/getting-started.md#try-the-example).
The available commands are described in [SC_THREAD commands](../docs/commands.md).
