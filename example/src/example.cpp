/******************************************************************************
 *                                                                            *
 * Copyright (C) 2026 MachineWare GmbH                                        *
 * All Rights Reserved                                                        *
 *                                                                            *
 * This work is licensed under the terms described in the LICENSE file found  *
 * in the root directory of this source tree.                                 *
 *                                                                            *
 ******************************************************************************/

#include <iostream>
#include <thread>
#include <systemc>

class fizzbuzz_module : public sc_core::sc_module
{
    SC_HAS_PROCESS(fizzbuzz_module);

private:
    sc_core::sc_event ev_fizz;
    sc_core::sc_event ev_buzz;

    void thread_main() {
        while (true) {
            int cnt = (int)sc_core::sc_time_stamp().to_seconds();
            if (cnt % 3 == 0)
                ev_fizz.notify();
            if (cnt % 5 == 0)
                ev_buzz.notify();
            if (cnt % 3 != 0 && cnt % 5 != 0)
                std::cout << cnt;

            std::this_thread::sleep_for(std::chrono::seconds(1));
            wait(1, sc_core::SC_SEC);
            std::cout << std::endl;
        }
    }

    void thread_fizz() {
        while (true) {
            wait(ev_fizz);
            std::cout << "FIZZ";
        }
    }

    void thread_buzz() {
        while (true) {
            wait(ev_buzz);
            std::cout << "BUZZ";
        }
    }

public:
    fizzbuzz_module(const sc_core::sc_module_name& nm):
        sc_module(nm), ev_fizz("ev_fizz"), ev_buzz("ev_buzz") {
        SC_THREAD(thread_main);
        SC_THREAD(thread_fizz);
        SC_THREAD(thread_buzz);
    }
};

int sc_main(int argc, char* argv[]) {
    fizzbuzz_module example("fizzbuzz");
    sc_core::sc_start(100, sc_core::SC_SEC);
    return 0;
}
