#!/usr/bin/python3.6
#source: https://pypi.org/project/psutil/

import psutil
from texttable import Texttable

def get_running_threads():
    t = Texttable()
    t.add_rows([['Process Name', 'Num Threads', 'Threads']])
    for process in psutil.process_iter():
            t.add_row([process.name(), process.num_threads(), process.threads()])
    return t