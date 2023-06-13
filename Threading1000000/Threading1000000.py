'''File: Threading1000000.py
Author: Bobby Parsons
Date: 11/17/21

Generates 1,000,000 random numbers and uses multithreading to determine
how many are greater than 5.
'''
import threading
import random

arr_lock = threading.Lock()
greater_than_5 = 0

def generate_1000000():
    arr = []
    for i in range(1000000):
        arr.append(random.randint(0, 10))
    
    return arr

def count_greater_than_5(num):
    with arr_lock:
        if num > 5:
            global greater_than_5
            greater_than_5 += 1

arr = generate_1000000()
greater_than_5 = 0

for num in arr:
    thread = threading.Thread(target=count_greater_than_5, args=(num, ))
    thread.start()

print(greater_than_5)