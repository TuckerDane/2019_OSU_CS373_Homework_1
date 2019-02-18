#!/usr/bin/python3.6
#source: https://pypi.org/project/psutil/

import sys
from texttable import Texttable

def list_loaded_modules():
    print("Enumerate all the loaded modules within the processes.")
    loaded_modules = Texttable()
    loaded_modules.add_rows([['Module Name']])
    for module in sys.modules.keys():
        loaded_modules.add_row([module])
    print(loaded_modules.draw())