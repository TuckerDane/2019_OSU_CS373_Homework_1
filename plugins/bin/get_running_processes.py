#!/usr/bin/python3.6
#source: https://pypi.org/project/psutil/
#source: https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/

import psutil
from texttable import Texttable

def get_running_processes():
    t = Texttable()
    t.add_rows([['PID', 'Process Name']])
    for process in psutil.process_iter():
        t.add_row([process.pid, process.name()])
    return t