#!/usr/bin/python3.6
import psutil

def main():
    print(psutil.pids())
    one()
    two()
    three()
    four()
    five()
    return 0

def one():
    print("one")

def two():
    print("two")

def three():
    print("three")

def four():
    print("four")

def five():
    print("five")

if __name__ == "__main__":
    main()