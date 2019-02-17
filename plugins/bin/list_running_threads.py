#!/usr/bin/python3.6
#source: https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/
#source: https://pypi.org/project/psutil/
import psutil
from texttable import Texttable

def list_running_threads():
    print("List all the running threads within process boundary.\n")
    t = Texttable()
    t.add_rows([['Process Name', 'Num Threads', 'Threads']])
    for process in psutil.process_iter():
            t.add_row([process.name(), process.num_threads(), process.threads()])
    print(t.draw())