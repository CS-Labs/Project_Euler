# Author: Christian Seely

import math

# Method to determine if a number n is prime.
def isPrime(n):
    div = 2
    while div <= math.sqrt(n):
        if (n % div) == 0:
            return False
        div += 1
    return True

def problemSeven():
    numPrime, i = 0, 2
    while numPrime < 10001:
        if isPrime(i):
            numPrime += 1
        i += 1
    return i-1

if __name__ == '__main__':
    print(problemSeven())