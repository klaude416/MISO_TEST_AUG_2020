# Test #1
# Write a command-line program that prints out the sum of two non-negative integers as input arguments. 
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

import sys

def help_and_exit():
    print('Usage:')
    print(f'{sys.argv[0]} [non-negative integer] [non-negative integer]')
    sys.exit(1)

def parse_int(str_param):
    str_numbers = [cha for cha in '0123456789']
    tot = 0
    for i, num in enumerate(str_param[::-1]):
        tot += str_numbers.index(num) * (10 ** i)

    return tot

def test():
    input1 = '12345678'
    input2 = '87654321'
    output = 99999999
    assert parse_int(input1) + parse_int(input2) == output
    print('test succeed')

if __name__ == "__main__":
    test()

    if len(sys.argv) != 3:
        help_and_exit()
    
    int1 = parse_int(sys.argv[1])
    int2 = parse_int(sys.argv[2])

    print(f'{int1} + {int2} = { int1 + int2 }')
    sys.exit(0)