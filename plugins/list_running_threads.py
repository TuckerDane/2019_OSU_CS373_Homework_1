#!/usr/bin/python3.6
#source: https://pypi.org/project/psutil/

import psutil
from texttable import Texttable

def list_running_threads(pid):
    print("\nRunning Threads:")
    process = psutil.Process(pid)
    process_table = Texttable()
    thread_table = Texttable()
    process_table.add_rows([['PID', 'Process Name', 'Num Threads']])
    process_table.add_row([process.pid, process.name(), process.num_threads()])
    thread_table.add_rows([['Thread IDs']])
    for thread in process.threads():
        thread_table.add_row([thread.id])
    print(process_table.draw())
    print(thread_table.draw())