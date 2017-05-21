# Author Christian Seely

# Take 2^1000 and convert that to a string. Next map over an
# anonymous function to convert each character in the string to
# an integer then sum those number up.
def problemSixteen():
    return sum(map(lambda x: int(x), (str(pow(2, 1000)))))

print(problemSixteen())
