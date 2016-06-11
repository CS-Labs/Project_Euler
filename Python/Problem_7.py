import math
# Author: Christian Seely

# Method to determine if a number n is prime.
def isPrime(n):
    div = 2
    while(div<=math.sqrt(n)):
        if(n%div==0):
            return False
        div+=1
    return True

def problemSeven():
    numPrime = 0
    i = 2
    while(numPrime<10001):
        if(isPrime(i)):
            numPrime+=1
        i+=1
    return (i-1)

print(problemSeven())