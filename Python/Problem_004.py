# Author: Christian Seely

import itertools

def problemFour():
    nRange = list(range(101, 1000)) # Candidates
    palindromicMultiples = []
    for p1, p2 in itertools.permutations(nRange, 2): #Iterate all possible pairings.
        multiple = str(p1*p2)
        firstHalf, secondHalf = multiple[:len(multiple)//2], multiple[len(multiple)//2:] # Split in half.
        if (len(multiple) % 2) != 0: # If even ignore middle digit.
            secondHalf = secondHalf[1:]
        secondHalf = secondHalf[::-1]
        # Disregarding middle digit, if firstHalf = secondHalf reversed then we have a palindromic number.
        if firstHalf == secondHalf:
            palindromicMultiples.append(multiple)
    return max(map(int,palindromicMultiples))

print(problemFour())


