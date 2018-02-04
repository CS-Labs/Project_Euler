#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <tuple>

/*Author: Christian Seely*/


/*
 Method to find the Pythagorean Triple such that
 a+b+c = 1000. This method uses Euclid's formula
 for increased speed. Euclid's formula works by
 providing two numbers in this case i, and j such
 that i>j and generates a unique Pythagorean Triple.
 This version of Euclid's formula does not make use
 of the constant k so all possible combinations of
 i and j | i>j only encompass a subset of the total
 solution set of Pythagorean Triples. In this case the
 answer we were looking for was contained in the subset.
*/
std::tuple<bool,int> euclidsFormulaHelper(int i, int j)
{
  int a = (i*i) - (j*j);
  int b = 2 * i*j;
  int c = (i*i) + (j*j);
  if (a + b + c == 1000) return std::make_tuple(true, a*b*c);
  else return std::make_tuple(false, 0);
}

int problemNine()
{
  int ans;
  bool e; 
  for (int i = 0; i < 1000; i++)
  {
    for (int j = 0; j < 1000; j++)
    {
      if (i > j)
      {
        std::tie(e, ans) = euclidsFormulaHelper(i, j);
        if (e) return ans;
      }
    }
  }
}


int main()
{
  std::cout << problemNine() << std::endl;
  return 0;
}

