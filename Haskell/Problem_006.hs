-- Author: Christian Seely

problemSix :: Integer
problemSix = let sr = sum r
                 r = [1..100]
             in sr * sr - (foldr ((+) . (\x -> x*x)) 0 r)

main = print $ problemSix