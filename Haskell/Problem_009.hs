-- Author: Christian Seely

-- Pythagorean triple generation speed increased by using Euclid's formula. 
problemNine :: Integer
problemNine = head $ [a*b*c | i <- [0..999], j <- [0..999], let (a,b,c) = (i*i-j*j, 2*i*j, i*i+j*j), i > j && a+b+c == 1000]

main = print $ problemNine