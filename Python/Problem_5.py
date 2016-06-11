import functools
# Author: Christian Seely

# Method to find the Greatest Common Divisor (gcd)
# given two numbers a and b.
def gcd(a,b):
    while(b!=0):
        r=a%b
        a=b
        b=r
    return a
# Method to find the Least Common Multiple (lcm)
# given two numbers a and b.
def lcm(a,b):
    return a/gcd(a,b)*b

def problemFive():
    return (functools.reduce(lcm,range(1,21))) 

print (int(problemFive()))

