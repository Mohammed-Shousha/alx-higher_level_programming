#!/usr/bin/python3

def print_args(argv):
    n = len(argv) - 1

    if n == 0:
        print('{} arguments.'.format(n))
    elif n == 1:
        print('{} argument:'.format(n))
        print('1: {}'.format(argv[1]))
    else:
        print('{} arguments:'.format(n))
        for i in range(1, len(argv)):
            print('{}: {}'.format(i, argv[i]))


if __name__ == '__main__':
    from sys import argv
    print_args(argv)
