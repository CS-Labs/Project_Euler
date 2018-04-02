# Author: Christian Seely

# Find the sum of the squares of the numbers
# 1 to n.
def sumOfSquares(n):
    return sum([i**2 for i in range(1, n)])

# Find the square of the sum of the numbers
# 1 to n.
def squareOfSum(n):
    return sum(range(1, n)) * sum(range(1, n))

def problemSix():
    return squareOfSum(101)-sumOfSquares(101)

if __name__ == '__main__':
    print (problemSix())