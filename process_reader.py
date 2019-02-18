#!/usr/bin/python3.6

import sys
from texttable import Texttable

sys.path.append('plugins/')

from list_running_processes import list_running_processes
from list_running_threads import list_running_threads
from list_loaded_modules import list_loaded_modules
from list_executable_pages import list_executable_pages
from list_memory import list_memory

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
                list_memory()
            if choice is 6:
                print("\nYou Quit!\n")
        except:
            print("invalid input\n")
            print_menu()
        
        
if __name__ == "__main__":
    main()