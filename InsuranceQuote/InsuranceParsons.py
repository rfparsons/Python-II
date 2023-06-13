'''File: InsuranceParsons.py
Author: Bobby 
Date: 8/25/21

Calculates an insurance rate for a customer
'''

CUSTOMER_ID = 0 # not sure what to do with this since there's only one customer to enter
ACCIDENT_RATE = 0.41

if (__name__ == '__main__'):
    rate_table = {16:{'SM':2593, 'L':2957, 'F':6930},
    25:{'SM':608, 'L':691, 'F':1745},
    35:{'SM':552, 'L':627, 'F':1564},
    45:{'SM':525, 'L':596, 'F':1469},
    55:{'SM':494, 'L':560, 'F':1363},
    65:{'SM':515, 'L':585, 'F':1402}}

    name = ''
    age = 0
    coverage_level = ''
    coverage_cost = 0
    input_valid = False
    accident = False
    accident_input = ''

    id = CUSTOMER_ID
    customer_dict = {}

    while (not input_valid):
        try:
            input_valid = True
            name = input('Enter the customer\'s name: ')
            age = int(input('Enter the customer\'s age: '))
            coverage_level = input('Enter the customer\'s desired coverage level: ')
            
            if (age < 16):
                print('Customer cannot drive!')
                input_valid = False
            if (not coverage_level in ['SM', 'L', 'F']):
                print('Invalid coverage level!')
                input_valid = False
        except:
            print('Invalid input!')
            input_valid = False

    #Get the right age from the table
    if (age >= 65):
        coverage_cost = rate_table[65][coverage_level]
    elif (age >= 55):
        coverage_cost = rate_table[55][coverage_level]
    elif (age >= 45):
        coverage_cost = rate_table[45][coverage_level]
    elif (age >= 35):
        coverage_cost = rate_table[35][coverage_level]
    elif (age >= 25):
        coverage_cost = rate_table[25][coverage_level]
    else:
        coverage_cost = rate_table[16][coverage_level]

    customer_dict[id] = [name, age, coverage_cost]

    input_valid = False

    while (not input_valid):
        try:
            accident_input = input('Has the customer been in an accident? [Y/N]: ').upper()

            if (accident_input == 'Y'):
                accident = True
                input_valid = True
            elif (accident_input == 'N'):
                accident = False
                input_valid = True
            else:
                print('Please enter either "Y" or "N".')
        except:
            print('Invalid input!')

    if (accident):
        customer_dict[id][2] = coverage_cost + coverage_cost * ACCIDENT_RATE

    print('Name: ' + customer_dict[id][0])
    print('Age: ' + str(customer_dict[id][1]))
    print('Annual cost: ' + str(customer_dict[id][2]))