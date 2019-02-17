#!/usr/bin/python3.6

import sys
from texttable import Texttable

sys.path.append('plugins/bin/')
sys.path.append('plugins/modules/')

from get_running_processes import get_running_processes
from get_running_threads import get_running_threads
from get_loaded_modules import get_loaded_modules
from get_executable_pages import get_executable_pages
from get_memory import get_memory

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
        choice = int(input("\nWhat would you like to do? "))
        if not 1 <= choice <= 6:
            print("\ninvalid choice")
        if choice is 1:
            print("\nRunning Processes:")
            running_processes = get_running_processes()
            print(running_processes.draw())
        if choice is 2:
            print("\nRunning Threads:")
            running_threads = get_running_threads()
            print(running_threads.draw())
        if choice is 3:
            print("\nLoaded Modules:")
            get_loaded_modules()
        if choice is 4:
            print("\nExecutable Pages:")
            get_executable_pages()
        if choice is 5:
            print("\nMemory:")
            get_memory()
        if choice is 6:
            print("\nYou Quit!\n")
        
if __name__ == "__main__":
    main()