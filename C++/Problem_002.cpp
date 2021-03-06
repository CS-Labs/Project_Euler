#include "stdafx.h"
#include <iostream>
#include <numeric>
#include <algorithm>
#include <vector>
/*Author: Christian Seely*/

constexpr size_t problemTwo()
{

  constexpr size_t breakValue = 4000000;
  size_t prev = 0;
  size_t cur = 1;
  size_t sum = 0;

  while(1)
  {
    size_t tmp = cur;
    cur = prev + cur;
    prev = tmp;
    if (cur > breakValue) break;
    if (cur % 2 == 0) sum += cur; // Sum even values. 
  }

  return sum;
}


int main()
{
  std::cout << problemTwo() << std::endl;
  return 0;
}

