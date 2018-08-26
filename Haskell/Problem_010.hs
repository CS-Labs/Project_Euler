-- Author: Christian Seely

-- Note, the prime generator was derived from the paper: https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf

-- TODO: Improve speed. 

primeGen :: [Integer]
primeGen = 2 : rest
  where rest = [c | c <- [3..], all ((/=) 0 . mod c) $ takeWhile (\p -> p*p <= c) primeGen]

problemTen :: Integer
problemTen = sum $ takeWhile (<= 2000000) primeGen

main = print $ problemTen