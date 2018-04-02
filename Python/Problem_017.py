# Author Christian Seely

import inflect
import re

# For the numbers 1 to 1000 use the inflection engine to convert each
# number to its english representation. Next remove all unwanted characters and
# record the length of the english representation of the number. Finally sum up all
# the lengths.
def problemSeventeen():
    p = inflect.engine()
    return sum([len(re.sub('[-, ]', '', p.number_to_words(i))) for i in range(1, 1001)])

if __name__ == '__main__':
    print(problemSeventeen())
