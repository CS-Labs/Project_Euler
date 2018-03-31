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
std::tuple<bool, int> euclidsFormulaHelper(int t_i, int t_j)
{
  int a = (t_i*t_i) - (t_j*t_j);
  int b = 2 * t_i*t_j;
  int c = (t_i*t_i) + (t_j*t_j);
  if (a + b + c == 1000) return {true, a*b*c};
  else return {false, 0};
}

int problemNine()
{
  for (int i = 0; i < 1000; i++)
  {
    for (int j = 0; j < 1000; j++)
    {
      if (i > j)
      {
        auto [e, ans] = euclidsFormulaHelper(i, j);
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
