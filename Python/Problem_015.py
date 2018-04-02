# Author Christian Seely

import functools

# Inspired from PE user intinig's solution in ruby.
# This method finds all the paths recursively.
# The lru_cache method from the functools library
# is a decorator for the function that memoizes it.
# By using memoization we are caching the results
# of our function calls which drastically increases
# the speed.
@functools.lru_cache(maxsize=None)
def solve(iXStart, iYStart):
    iNumRoutes = 0
    iNumRoutes += solve(iXStart, iYStart-1) if (iYStart > 0) else 0
    iNumRoutes += solve(iXStart-1, iYStart) if (iXStart > 0) else 0
    iNumRoutes += 1 if (iXStart == 0 and iYStart == 0) else 0
    return iNumRoutes

def problemFifteen():
    return solve(20,20)

if __name__ == '__main__':
    print(problemFifteen())