-- Author: Christian Seely

-- Note, the prime generator was derived from the paper: https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf

primeGen :: [Integer]
primeGen = 2 : rest
  where rest = [c | c <- [3..], all ((/=) 0 . mod c) $ takeWhile (\p -> p*p <= c) primeGen]

nthPrime :: Int -> Integer
nthPrime n = primeGen !! n

problemSeven :: Integer
problemSeven = nthPrime 10000

main = print $ problemSeven