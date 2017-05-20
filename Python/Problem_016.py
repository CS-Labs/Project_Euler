# Author Christian Seely

def problemSixteen():
    return sum(map(lambda x: int(x), (str(pow(2, 1000)))))


print(problemSixteen())