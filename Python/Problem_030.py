# Author Christian Seely

def problemThirty():
    # Iterate through the range 2 to 295946 (5*9^5)
    # and filter out any i such that the sum of it's digits each to the fifth power
    # equals i.
    return sum([i for i in range(2,295946) if sum(int(x)**5 for x in str(i)) == i])

if __name__ == '__main__':
    print(problemThirty())
