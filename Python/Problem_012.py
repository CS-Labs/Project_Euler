# Author: Christian Seely

import math
# Function to find the number of factors for some
# number num.
def numFactors(num):
    nFactors = 0
    # We only have to check up to the square root of the num.
    bound = int(math.sqrt(num)+1)
    for div in range(1, bound):
        if not (num % div):
            nFactors += 1
    # Factors come in pairs multiple answer by two.
    return nFactors*2


def problemTwelve():
    i = 2
    while True:
        sum = int(i*(i+1)/2) # Obtain triangle number.
        if numFactors(sum) > 500:
            return sum
        i += 1

print(problemTwelve())

