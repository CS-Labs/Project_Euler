# Author Christian Seely
from functools import reduce

# Function to perform a step in the process of calculating
# a factorial. n*(n-1)
def factStep(x, y):
    return x*y

# Calculate 100! using reduce with the help of our factStep function.
# Next map over the number after it is converted to a string and convert
# each character to a number and sum those numbers up.
def problemTwenty():
    return sum(map(lambda x: int(x), str(reduce(factStep, range(1,100)))))


print(problemTwenty())