'''
Question - Shattering Orbs

7 orbs are labeled 1−7 and are linked linearly in a vertical stack from the ceiling with orb 1 being a part of the ceiling and orb 7 being closest to the floor. 
Each orb is attached to adjacent orbs by a chain link. At each time step, one of the remaining links is going to be uniformly at random selected and cut. 
As a result, all the orbs below that link will fall and shatter. 
What is the expected number of cuts needed until orb 1 is the only remaining orb?
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def orb_checker(n, array_data, x):
    if n == 2:
        array_data.append(1)
        x.append(n)
        return array_data, x
    if n > 2:
        array_data, x = orb_checker(n-1, array_data, x)
        orb_cuts = 1 + (1 / (n - 1)) * (sum(array_data))
        array_data.append(orb_cuts)
        x.append(n)
        return array_data, x

array_data = []
x = []
orb_checker(500, array_data, x)

# Plotting the data
plt.plot(x, array_data)
plt.xlabel("n")
plt.ylabel("Orb Cuts")
plt.title("Orb Cuts vs n")
plt.show()