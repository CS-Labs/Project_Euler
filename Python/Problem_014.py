# Author: Christian Seely

import sys
import operator

dict = {} # Head of the Collatz Sequence -> Length of Collatz Sequence

# This method creates and ultimately find the length
# of a Collatz sequence with a starting node n.
# To increase performance once the length of a Collatz Sequence is found
# the head of the sequence is mapped to the length of said sequence
# That means whenever n is a key in our dictionary we
# do not have to waste time calculating the length of the rest
# of the sequence since we have already found it. So we can just add the
# known length to the length we have thus far to get the new length.
def createCollatzSequence(n):
    collatzSequence = [n]
    # Looping in this mannor is faster than a while loop.
    for i in range(sys.maxsize):
        if n in dict:
            newLen = len(collatzSequence)+dict.get(n)-1
            dict[collatzSequence[0]] = newLen
            return newLen
        if n % 2 == 0:
            n = int(n/2)
            collatzSequence.append(n)
        else:
            n = 3*n+1
            collatzSequence.append(n)
        if n == 1:
            newLen = len(collatzSequence)
            dict[collatzSequence[0]] = newLen
            return newLen

def problemFourteen():
    maxIndex, _ = max(enumerate([createCollatzSequence(i) for i in range(1,1000000)]), key=operator.itemgetter(1))
    return maxIndex + 1 # Account for result being zero-indexed.
print(problemFourteen())
