# Author: Christian Seely

def problemThree():
    max, div = 0, 2
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
        while not (n % div):
            n /= div
        div += 1
    return int(max)

if __name__ == '__main__':
    print(problemThree())
