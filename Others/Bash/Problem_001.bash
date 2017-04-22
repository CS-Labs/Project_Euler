#!/bin/bash

sum = 0

for (( c=1; c<1000; c++ ))
do
   if (($c%3==0)) || (($c%5==0))
   then
        ((sum += $c))
   fi
done

echo $sum