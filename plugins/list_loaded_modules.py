#!/usr/bin/python3.6
#source: https://pypi.org/project/psutil/

import psutil
from texttable import Texttable

def list_loaded_modules():
    print("Enumerate all the loaded modules within the processes.")