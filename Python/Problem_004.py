import itertools
# Author: Christian Seely
def problemFour():
    nRange = list(range(101, 1000)) # Candidates
    palindromicMultiples = []
    for pair in itertools.permutations(nRange, 2): #Iterate all possible pairings.
        multiple = (str(pair[0]*pair[1]))
        firstHalf, secondHalf = multiple[:len(multiple)//2], multiple[len(multiple)//2:] # Split in half.
        if(len(multiple)%2!=0): # If even ignore middle digit.
            secondHalf = secondHalf[1:]
        secondHalf = secondHalf[::-1]
        # Disregarding middle digit, if firstHalf = secondHalf reversed then we have a palindromic number.
        if(firstHalf==secondHalf):
            palindromicMultiples.append(multiple)
    largest = 0
    palindromicMultiples = list(map(int,palindromicMultiples))
    # Find the largest of the palindromic numbers found.
    for palindromicMultiple in palindromicMultiples:
        if(palindromicMultiple>largest):
            largest = palindromicMultiple
    return largest

print(problemFour())


