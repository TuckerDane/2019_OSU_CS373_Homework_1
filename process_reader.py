#!/usr/bin/python3.6
#source: https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/
import psutil

def main():
    print()
    list_running_processes()
    print()
    list_running_threads()
    print()
    list_loaded_modules()
    print()
    list_executable_pages()
    print()
    read_memory()
    return 0

def list_running_processes():
    print("Enumerate all the running processes.\n")
    for process in psutil.process_iter():
        p_name = process.name()
        pid = process.pid
        print(pid, ":", p_name)

def list_running_threads():
    print("List all the running threads within process boundary.\n")

def list_loaded_modules():
    print("Enumerate all the loaded modules within the processes.\n")

def list_executable_pages():
    print("Is able to show all the executable pages within the processes.\n")

def read_memory():
    print("Gives us a capability to read the memory.\n")

if __name__ == "__main__":
    main()