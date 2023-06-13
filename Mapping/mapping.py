'''File: mapping.py
Author: Bobby Parsons
Date: 9/6/21

Demonstrates the use of the "map" function
'''

def string_len(input):
    return [input, len(input)]

if (__name__ == '__main__'):
    str_list = ['word', 'word1', 'word2', 'w3rd', '4thword', 'word (5)', '6wo6rd', 'word7', 'word8', 'word10']

    output = map(string_len, str_list)

    for i in output:
        print(i[1])