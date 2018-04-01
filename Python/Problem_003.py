# Author: Christian Seely

def problemThree():
    max, div, remainder = 0, 2, 0
    n = 600851475143
    while True:
        if (div*div) > n:
            if n != 1 and n > max:
                max = n
                break
        if n % div == 0:
            if div > max:
                max = div
            n /= div
        if not remainder:
            div +=1
        while not (n % div):
            n /= div
        div += 1
    return int(max)

print(problemThree())
