#!/usr/bin/python3
# encoding: utf-8

import dis


def magic_calculation(a, b):
    from calculator_1 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else: 
        return (sub(a, b))

dis.dis(magic_calculation)
    
