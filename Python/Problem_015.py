# Author Christian Seely

import functools
from math import factorial as fact

# The number of paths from (0,0) to (n,k) can
# be represented as (n+k)Cn or in this
# case 40C20 (40 choose 20).
def mathBased():
    return int(fact(40)/(fact(20)*(fact(40-20))))


# Inspired from PE user intinig's solution in ruby.
# This method finds all the paths recursively.
# The lru_cache method from the functools library
# is a decorator for the function that memoizes it.
# By using memoization we are caching the results
# of our function calls which drasticlly increases
# the speed.
@functools.lru_cache(maxsize=None)
def progBased(iXStart, iYStart):
    iNumRoutes = 0
    iNumRoutes += progBased(iXStart, iYStart-1) if (iYStart > 0) else 0
    iNumRoutes += progBased(iXStart-1, iYStart) if (iXStart > 0) else 0
    iNumRoutes += 1 if (iXStart == 0 and iYStart == 0) else 0
    return iNumRoutes


def problemFifteen():
    sAnswer = "{0:<20} {1:>8}\n".format('Math Based: ', mathBased())
    sAnswer += "{0:<20} {1:>8}\n".format('Programming Based: ', progBased(20,20))
    return sAnswer


print(problemFifteen())