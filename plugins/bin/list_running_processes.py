#!/usr/bin/python3.6
#source: https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/
#source: https://pypi.org/project/psutil/
import psutil
from texttable import Texttable

def list_running_processes():
    print("Enumerate all the running processes.\n")
    t = Texttable()
    t.add_rows([['Process Name', 'PID']])
    for process in psutil.process_iter():
        t.add_row([process.name(), process.pid])
    print(t.draw())