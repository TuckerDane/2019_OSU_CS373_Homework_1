#!/usr/bin/python3.6
#source: https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/
#source: https://pypi.org/project/psutil/
import psutil
from texttable import Texttable

def main():
    print()
    list_running_processes()
    print()
    list_running_threads()
    print()
    list_loaded_modules()
    #print()
    #list_executable_pages()
    #print()
    #read_memory()
    return 0

def list_running_processes():
    print("Enumerate all the running processes.\n")
    t = Texttable()
    t.add_rows([['Name', 'PID']])
    for process in psutil.process_iter():
        t.add_row([process.name(), process.pid])
    print(t.draw())

def list_running_threads():
    print("List all the running threads within process boundary.\n")
    t = Texttable()
    t.add_rows([['Name', 'Num Threads', 'Threads']])
    for process in psutil.process_iter():
            t.add_row([process.name(), process.num_threads(), process.threads()])
    print(t.draw())
def list_loaded_modules():
    print("Enumerate all the loaded modules within the processes.\n")
    for process in psutil.process_iter():
        print("name:", process.name())

def list_executable_pages():
    print("Is able to show all the executable pages within the processes.\n")

def read_memory():
    print("Gives us a capability to read the memory.\n")
    for process in psutil.process_iter():
        print("name:", process.name())
        print(process.memory_info())

if __name__ == "__main__":
    main()