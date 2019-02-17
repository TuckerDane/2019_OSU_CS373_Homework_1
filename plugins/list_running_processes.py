#!/usr/bin/python3.6
#source: https://pypi.org/project/psutil/
#source: https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/

import psutil
from texttable import Texttable

def list_running_processes():
    print("\nRunning Processes:")
    running_processes = Texttable()
    running_processes.add_rows([['PID', 'Process Name']])
    for process in psutil.process_iter():
        running_processes.add_row([process.pid, process.name()])
    print(running_processes.draw())