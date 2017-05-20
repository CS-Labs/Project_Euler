# Author Christian Seely
from functools import reduce

def factStep(x,y):
    return x*y

def problemTwenty():
    return sum(map(lambda x: int(x), str(reduce(factStep, range(1,100)))))


print(problemTwenty())