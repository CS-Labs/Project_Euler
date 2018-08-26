-- Author: Christian Seely

import Data.List 

fibGen :: Integer -> Integer -> [Integer]
fibGen a b = a:fibGen b (a+b)

problemTwo :: Integer
problemTwo = sum $ filter even $ takeWhile (<=4000000) $ fibGen 0 1

main = print $ problemTwo