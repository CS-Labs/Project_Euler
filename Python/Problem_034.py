# Author Christian Seely
import math


def problemThirtyFour():

    oNumToFact = {}
    # Create lookup table for first 10 factorial values (0-9)
    for i in range(0,10):
        oNumToFact[i] = math.factorial(i)

    iTotalSum = 0
    for i in range(10, 100000): # Upper bound found through testing.
        nString = str(i)
        iSum = 0
        for c in nString:
            iSum += oNumToFact[int(c)]
        if iSum == i: # Factorial value of digits sum to number.
            iTotalSum += iSum

    return iTotalSum

if __name__ == '__main__':
    print(problemThirtyFour())
