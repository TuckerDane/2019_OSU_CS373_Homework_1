#!/usr/bin/python3.6

import sys
sys.path.append('plugins/bin/')
sys.path.append('plugins/modules/')

from list_running_processes import list_running_processes

def main():
    print()
    list_running_processes()
    #print()
    #list_running_threads()
    #print()
    #list_loaded_modules()
    #print()
    #list_executable_pages()
    #print()
    #read_memory()
    return 0

if __name__ == "__main__":
    main()