# Author Christian Seely
import math


def problemThirtyFour():

    oNumToFact = {}
    # Create lookup table for first 10 factorial values (0-9)
    for i in range(0,10):
        oNumToFact[i] = math.factorial(i)

    iTotalSum = 0
    iUPPER_BOUND = math.factorial(9)*7 # Define an upper bound 9!*7

    for i in range(10, iUPPER_BOUND):
        nString = str(i)
        iSum = 0
        for c in nString:
            iSum += oNumToFact[int(c)]
        if iSum == i: # Factorial value of digits sum to number.
            iTotalSum += iSum

    return iTotalSum

print(problemThirtyFour())
