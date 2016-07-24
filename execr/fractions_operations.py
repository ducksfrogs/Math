'''
fractions_opretions.py

'''

from fractions import Fraction

def add(a, b):
    print('Result of adding {0} and {1} is {2}'.format(a, b, a+b))

def substract(a, b):
    print('Result of Subtract: {0}'.format(a, b, a-b))


if __name__ == '__main__':
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        if op == 'Add':
            add(a,b)
