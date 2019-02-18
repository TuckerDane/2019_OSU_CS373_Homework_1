#!/usr/bin/python3.6

import sys
import psutil
from texttable import Texttable
from ctypes import string_at
from sys import getsizeof
from texttable import Texttable

def main():
    print_menu()
    make_choice()
    return 0

def print_menu():
    t = Texttable()
    t.add_rows([['Choice', 'Description']])
    t.add_row(['1', 'list running processes'])
    t.add_row(['2', 'list running threads'])
    t.add_row(['3', 'list loaded modules'])
    t.add_row(['4', 'list executable pages'])
    t.add_row(['5', 'read memory'])
    t.add_row(['6', 'quit'])
    print(t.draw())

def make_choice():
    choice = -1
    while choice is not 6:
        choice = input("\nWhat would you like to do? ")
        try:
            choice = int(choice)
            if not 1 <= choice <= 6:
                print("\ninvalid choice")
            if choice is 1:
                list_running_processes()
            if choice is 2:
                pid = int(input("Which Process ID? "))
                try:
                    list_running_threads(pid)
                except:
                    print("no such process")
            if choice is 3:
                print("\nLoaded Modules:")
                list_loaded_modules()
            if choice is 4:
                print("\nExecutable Pages:")
                pid = int(input("Which Process ID? "))
                try:
                    list_executable_pages(pid)
                except:
                    print("no such process")
            if choice is 5:
                print("\nMemory:")
                address = int(input("Which Memory Address? "))
                list_memory(address)
            if choice is 6:
                print("\nYou Quit!\n")
        except:
            print("invalid input\n")
            print_menu()

def list_running_processes():
    print("\nRunning Processes:")
    running_processes = Texttable()
    running_processes.add_rows([['PID', 'Process Name']])
    for process in psutil.process_iter():
        running_processes.add_row([process.pid, process.name()])
    print(running_processes.draw())

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

def list_loaded_modules():
    print("Enumerate all the loaded modules within a processes.")
    loaded_modules = Texttable()
    loaded_modules.add_rows([['Module Name']])
    for module in sys.modules.keys():
        loaded_modules.add_row([module])
    print(loaded_modules.draw())

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

def list_memory(address):
    print("read the memory.")
    print(string_at(id(address), getsizeof(address)))

if __name__ == "__main__":
    main()