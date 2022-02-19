from itertools import count
from operator import le
import numpy as np


# tuple testing
# a = ([1, 2], ["x", "y"],)
# print(a)
# a[0][0] = 3
# a[1][0] = "zzawlla"
# print(a)


def c_sum(arr):
    count = len(arr)
    sum = arr.sum()
    return sum, count


arr = np.random.randint(10, size=8)

a = c_sum(arr)

print(a)
