'''
Question - Consecutive Pairs

Consider the set of 10 consecutive integers {1,2,…,10}. 
How many subsets contain exactly 1 pair of consecutive integers? 
For example, {3,5,6,9} contains exactly 1 pair of consecutive integers.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def non_consecutive_counter(n, alt_array_data):
    alt_array_data.append(1)
    alt_array_data.append(2)
    for i in range(2, n + 1):
        alt_array_data.append(alt_array_data[i-1] + alt_array_data[i-2])
    return alt_array_data

def consecutive_counter(n, array_data, alt_array_data, x):
    alt_array_data = non_consecutive_counter(n, alt_array_data)
    array_data.append(0)
    array_data.append(0)
    array_data.append(1)
    x.append(0)
    x.append(1)
    x.append(2)
    for i in range(3, n + 1):
        array_data.append(array_data[i-1] + array_data[i-2] + alt_array_data[i-3])
        x.append(i)
    return x, array_data, alt_array_data

array_data = []
alt_array_data = []
x = []
x, array_data, alt_array_data = consecutive_counter(15, array_data, alt_array_data, x)
print(x)
print(array_data)
print(alt_array_data)

plt.plot(x, array_data, label='array_data', color='blue')
plt.plot(x, alt_array_data, label='alt_array_data', color='red')
plt.xlabel("x")
plt.ylabel("Values")
plt.legend()
plt.title("Comparison of array_data and alt_array_data")
plt.show()