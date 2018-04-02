# Author Christian Seely

# Function that takes steps in the fib sequence acting
# as an iterator.
def fibStep():
    x, y , i = 1, 1, 3 # We start by looking at the 3rd index in the sequence.
    while True:
        x, y = y, x + y
        yield x, y, i
        i += 1


def problemTwentyFive():
    for x, y, i in fibStep():
        if len(str(y)) >= 1000:
            return i  # Index i such that length of fibSequence(i) >= 1000.

if __name__ == '__main__':
    print(problemTwentyFive())
