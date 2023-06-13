'''File: NumpyArrays.py
Author: Bobby Parsons
Date: 9/13/21

Demonstrates NumPy arrays
'''

import numpy as np

array_1 = np.array([[10, 15, 20], [2, 3, 4], [9, 14.5, 18]])
array_2 = np.array([[1, 2, 5], [8, 0, 12], [11, 3, 22]])

#Print it to the console
print(array_1)
#Print it's shape
print(array_1.shape)
#Print a 2x2 slice of the array including the values from [0,0] to [1,1]
print(array_1[0:2,0:2])
#Output the boolean value of each element in the array on whether the element is even (even = True, odd = False)
print(array_1 % 2 == 0)

#Print the output of adding the two arrays together elementwise
print(np.add(array_1, array_2))
#Print the output of multiplying the two arrays together elementwise
print(np.multiply(array_1, array_2))

#Print the sum of all the elements in the array
print(array_2.sum())
#Print the product of all elements in the array
print(array_2.prod())
#Print the maximum and minimum value of the elements in the array
print(array_2.max())
print(array_2.min())