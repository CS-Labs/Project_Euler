-- Author: Christian Seely

reverseInteger :: Integer -> Integer
reverseInteger = read . reverse . show

isPalindromicMultiple :: Integer -> Bool
isPalindromicMultiple x = x == reverseInteger x

problemFour :: Integer
problemFour = maximum $ filter isPalindromicMultiple [x*y | x <- [100..999], y <- [100..999]]

main = print $ problemFour