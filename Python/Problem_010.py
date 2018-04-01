# Author: Christian Seely

import math

# Method to find the sum of primes from 2 to 2,000,000
# using the Sieve of Eratosthenes algorithm.
def problemTen():
    scope = 2000000
    # The index in the array represents a natural number.
    # The possible values at each index have the following meaning:
    # 1 = Prime, 0 = Not prime.
    n = [1] * scope
    bound = math.sqrt(len(n))
    for i in range(2, int(bound)):
        if n[i] == 1:
            j = (i*i)
            k = 1
            while j < scope:
                n[j] = 0
                j = (i*i)+(k*i)
                k+=1
    sum = 0
    # Sum all the indices such that
    # n[i] = 1 (implies i is prime)
    for i in range(2, scope):
        if n[i]:
            sum += i
    return sum

print(problemTen())