# Author Christian Seely

def problemFortyEight():
    # Sum up the series 1^1 + 2^2 +... 1000^1000 then reverse
    # the resulting number. Next take the first 10 numbers off and reverse the
    # resulting 10 numbers to get the answer.
    return str(sum([i**i for i in range(1,1001)]))[::-1][:10][::-1]

print(problemFortyEight())