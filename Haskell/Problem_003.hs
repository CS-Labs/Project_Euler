-- Author: Christian Seely

primeFactors :: Integer -> [Integer]
primeFactors = factorize 2
  where 
    factorize a n
        | n == 1 = []
        | a * a > n = [n]
        | rem == 0 = a : factorize a div
        | otherwise = factorize (a + 1) n
        where
            (div, rem) = divMod n a

problemThree :: Integer
problemThree = last $ primeFactors 600851475143

main = print $ problemThree