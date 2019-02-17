#!/usr/bin/python3.6
#source: https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/
#source: https://pypi.org/project/psutil/
import psutil
from texttable import Texttable

def read_memory():
    print("Gives us a capability to read the memory.\n")
    for process in psutil.process_iter():
        print("name:", process.name())
        print(process.memory_info())