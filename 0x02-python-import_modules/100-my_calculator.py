#!/usr/bin/python3

def check_input(argv):
    n = len(argv) - 1

    if n != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if argv[2] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)


def calculator(argv):
    check_input(argv)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    r = 0

    if op == '+':
        r = add(a, b)
    elif op == '-':
        r = sub(a, b)
    elif op == '*':
        r = mul(a, b)
    elif op == '/':
        r = div(a, b)

    print('{} {} {} = {}'.format(a, op, b, r))


if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv
    calculator(argv)
