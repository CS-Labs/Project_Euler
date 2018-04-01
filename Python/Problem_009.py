# Author: Christian Seely

# Method to find the Pythagorean Triple such that
# a+b+c = 1000. This method uses Euclid's formula
# for increased speed. Euclid's formula works by
# providing two numbers in this case i, and j such
# that i>j and generates a unique Pythagorean Triple.
# This version of Euclid's formula does not make use
# of the constant k so all possible combinations of
# i and j | i>j only encompass a subset of the total
# solution set of Pythagorean Triples. In this case the
# answer we were looking for was contained in the subset.
def euclidsFormulaHelper(i, j):
    a = (i*i)-(j*j)
    b = 2*i*j
    c = (i*i)+(j*j)
    if a + b + c == 1000:
        return True, a * b *c
    else:
        return False, 0


def problemNine():
    for i in range(1000):
        for j in range(1000):
            if i > j:
                (exit,ans) = euclidsFormulaHelper(i,j)
                if exit :
                    return ans


print (problemNine())





