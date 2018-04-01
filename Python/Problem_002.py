# Author: Christian Seely

def problemTwo():
    prev, curr, sum = 0, 1, 0
    breakValue = 4000000
    while True:
        curr, prev = prev + curr, curr
        if curr > breakValue:
            break
        if curr % 2 == 0:
            sum += curr
    return sum
print (problemTwo())
