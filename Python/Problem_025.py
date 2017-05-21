# Author Christian Seely

# Function that takes steps in the fib sequence acting
# as an iterator.
def fibStep():
    x = 1
    y = 1
    i = 3 # We start by looking at the 3rd index in the sequence.
    while True:
        tmp = x + y
        x = y
        y = tmp
        yield x, y, i
        i += 1


def problemTwentyFive():
    for x, y, i in fibStep():
        if len(str(y)) >= 1000:
            return i  # Index i such that length of fibSequence(i) >= 1000.

print(problemTwentyFive())
