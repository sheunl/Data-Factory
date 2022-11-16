'''
Data Factory Entry Point

Input data from shell


'''
import sys

def shellcall():
    print("Shell")

def interactive():
    print("Interactive")

if __name__ == '__main__':
    sysinput =sys.argv[1:]
    if len(sysinput) > 0:
        shellcall()
    else:
        interactive()