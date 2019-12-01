from math import *


# two positions given in pair form
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean(a, b):
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
