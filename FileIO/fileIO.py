'''File: fileIO.py
Author: Bobby Parsons
Date: 9/15/21

Demonstrates the use of file input and using regular expressions to analyze it
'''

import re

FILE = 'Moby_Dick_Chapter_1.txt'
#FILE = 'Sense_and_Sensibility_Chapter_1.txt'

def count_word(word, line):
    instances = re.findall('[\W]' + word + '[\W]', line, re.IGNORECASE)
    count = len(instances)
    return count

if (__name__ == '__main__'):
    with open(FILE, 'r') as f:
        olds = 0
        waters = 0
        total_length = 0
        sentences = 0

        for line in f:
            total_length += len(line)

            olds += count_word('old', line)
            waters += count_word('water', line)

            sentences += len(re.findall('\.', line))
            sentences -= count_word('Mr.', line)
            sentences -= count_word('Mrs.', line)

        avg_length = total_length / sentences

        print('"Old"s: ' + str(olds))
        print('"Water"s: ' + str(waters))
        print('Average sentence length: ' + str(avg_length))
