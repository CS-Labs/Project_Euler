# Author Christian Seely

def problemThirty():
    # Iterate through the range 10 to 1000000 (bound found arbitrary through testing)
    # and filter out any i such that the sum of it's digits each to the fifth power
    # equals i.
    return sum([i for i in range(10,1000000) if sum(int(x)**5 for x in str(i)) == i])

print(problemThirty())
