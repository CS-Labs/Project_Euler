# Author: Christian Seely

import functools

def gcd(a,b):
    while b:
        r = a%b
        a, b = b, r
    return a

def lcm(a,b):
    return a/gcd(a,b)*b

def problemFive():
    return int(functools.reduce(lcm, range(1,21)))

print (problemFive())

