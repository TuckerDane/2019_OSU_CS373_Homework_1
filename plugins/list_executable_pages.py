#!/usr/bin/python3.6
#source: https://pypi.org/project/psutil/

import psutil
from texttable import Texttable

def list_executable_pages():
    print("Is able to show all the executable pages within the processes.")