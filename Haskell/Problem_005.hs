-- Author: Christian Seely

problemFive :: Integer
problemFive = foldr lcm 1 [1..21]

main = print $ problemFive