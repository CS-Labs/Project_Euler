# Author Christian Seely

def problemFortyEight():
    # Sum up the series 1^1 + 2^2 +... 1000^1000 then take
    # the first 10 numbers. 
    return str(sum([i**i for i in range(1,1001)]))[-10:]
print(problemFortyEight())