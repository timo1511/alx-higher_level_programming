#!/usr/bin/python3


def magic_calculation (*args):
    nargs = len(args)
    print(nargs, args)


if __name__ == '__main__':
    import dis
    dis.dis(magic_calculation)
