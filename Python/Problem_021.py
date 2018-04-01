# Author Christian Seely
from math import sqrt


def d(n):
    iSum = 1
    # We only need to go up to sqrt(n), the plus one is
    # effectively the ceiling.
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            # Now add the pairing (i and n/i) to our sum.
            iSum += i
            iSum += int(n/i)
    return n, iSum


def problemTwentyOne():
    # Generate a list of tuples (n,d(n)) where n is from 1 to 9999.
    aPropDivisorSums = list((map(d, range(1, 10000))))
    aAns = []
    for (a, b) in aPropDivisorSums:
        (_, iSum) = d(b)
        if iSum == a: # This implies d(a) = d(b) (an amicable pair)
            # Remove tuples where a equals b or the flipped tuple already exists.
            if a != b and (b, a) not in aAns:
                aAns.append((a, b))
    # Now return the sum of the amicable pairs.
    return sum(map(lambda x: x[0] + x[1], aAns))

print(problemTwentyOne())
