'''File: wrapper.py
Author: Bobby Parsons
Date: 8/27/21

Demonstrates a wrapper function and decorators
'''


def multiplication_dec(func):
    def wrapper(num1, num2):
        if (num2 != 0):
            print('Doubling ' + str(num1) + ' and tripling ' + str(num2))
            return func(num1 * 2, num2 * 3)
        else:
            print('Can\'t divide by zero!')
            return None

    return wrapper


@multiplication_dec
def divide(num1, num2):
    return int(num1 / num2)


if (__name__ == '__main__'):
    print(divide(12, 2))
    print(divide(36, 4))
    print(divide(12, 0))
