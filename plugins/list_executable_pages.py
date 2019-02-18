#!/usr/bin/python3.6
#source: https://pypi.org/project/psutil/

import psutil
from texttable import Texttable

def list_executable_pages(pid):
    print("Is able to show all the executable pages within the processes.")
    process = psutil.Process(pid)
    process_table = Texttable()
    maps_table = Texttable()
    process_table.add_rows([['PID', 'Process Name']])
    process_table.add_row([process.pid, process.name()])
    maps_table.add_rows([['Memory Range', 'Offset', 'Path']])
    maps_path = "/proc/"+str(process.pid)+"/maps"
    fp = open(maps_path, 'r') 
    for line in fp:
        values = line.split()
        if len(values) is 6:
            for each in values:
                maps_table.add_row([values[0], values[2], values[5]])
        else:
            for each in values:
                maps_table.add_row([values[0], values[2], 'none'])
    print(process_table.draw()) 
    print(maps_table.draw())