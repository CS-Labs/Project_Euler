# Author: Christian Seely
def problemThree():
    max = 0
    n = 600851475143
    primeFactors = []
    testDivisor = 2
    terminate = False
    # Find prime factors of n.
    while(not(terminate)):
        if((testDivisor*testDivisor)>n):
            if(n!=1):
                primeFactors.append(n)
                terminate = True
            else:
                terminate = True
        if(n%testDivisor==0and(not(terminate))):
            primeFactors.append(testDivisor)
            remainder = n%testDivisor
            n /= testDivisor
            if(remainder!=0):
                testDivisor+=1
            while(n%testDivisor==0 and (not(terminate))):
                n /= testDivisor
        testDivisor+=1
    # Find largest prime factor in primeFactors.
    for pf in primeFactors:
        if(pf>max):
            max=pf
    return max
print (problemThree())
