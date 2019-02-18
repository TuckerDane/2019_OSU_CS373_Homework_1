#!/usr/bin/python3.6
#source: https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/
#source: https://pypi.org/project/psutil/
from ctypes import string_at
from sys import getsizeof
from texttable import Texttable

def list_memory(address):
    print("read the memory.")
    print(string_at(id(address), getsizeof(address)))