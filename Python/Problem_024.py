# Author Christian Seely
import itertools

def problemTwentyFour():
    # Generate all permutations in lexicographical order where each permutation
    # is confined to a tuple. Next use islice to move the one millionths permutation
    # to the front of the iterator. Then call next to grab the one millionth item from
    # the iterator. Finally, consolidate the digits in the tuple into a string.
    return  "".join(d for d in next(itertools.islice(itertools.permutations("0123456789"), 999999, None)))

if __name__ == '__main__':
    print(problemTwentyFour())