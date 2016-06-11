# Author: Christian Seely
def problemTwo():
    i = 1
    j = 2
    sum = j
    while True:
        k = i+j
        if(k>4000000):
            break
        if(k%2==0):
            sum+=k
        temp = j
        j = k
        i = temp
    return sum
print (problemTwo())
