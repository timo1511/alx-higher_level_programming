#!/usr/bin/python3
# encoding: utf-8

def magic_calculation(a, b):
    nargs = len(a, b)
    print(nargs, (a, b))

if __name__ == '__main__':
    import dis
    dis.dis(magic_function)
