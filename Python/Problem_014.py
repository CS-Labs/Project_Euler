# Author: Christian Seely
import sys
dict = {} # Head of Collatz Sequence -> Length of Collatz Sequence
# This method create and ultimately find the length
# of a Collatz sequence with a starting node n.
# To increase performance once the length of a Collatz Sequence is found
# the head of the sequence is mapped to the length of said sequence
# in dict. That means whenever n is a key in our dictionary we
# do not have to waste time calculating the length of the rest
# of the sequence since we have already found it. So we can just add the
# known length to the length we have thus far to get the new length.
# This method of mapping sequence heads to the length of the
# sequence results in around a 2250% performance boost.
def createCollatzSequence(n):
    collatzSequence = [n]
    # Looping over range is faster than
    # using a while loop.
    for i in range(sys.maxsize):
        if(n in dict):
            newLen = len(collatzSequence)+dict.get(n)-1
            dict[collatzSequence[0]] = newLen
            return (newLen)
        if(n%2==0):
            n=((int(n/2)))
            collatzSequence.append(n)
        else:
            n = 3*n+1
            collatzSequence.append(n)
        if (n==1):
            newLen = len(collatzSequence)
            dict[collatzSequence[0]] = newLen
            return (newLen)

def problemFourteen():
    maxLen = 0
    val = 0
    for i in range(1,1000000):
        chainLen = createCollatzSequence(i)
        if(chainLen > maxLen):
            val = i
            maxLen = chainLen
    return (val)


print(problemFourteen())
