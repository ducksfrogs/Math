'''
Multiplication table printer
'''

def multi_table(a,b):
    for i in range(b):
        print('{0}x{1}={2}'.format(a, i, a*i))

if __name__ == '__main__':
    try:
        a = float(input('Enter a number: '))
        b = float(input('Enter a number: '))
        if not b.is_integer() or b <0:
            print('The number of multiples should be a positive integer')
        else:
            multi_table(a, int(b))
    except ValueError:
        print('You entered an invaild input')
