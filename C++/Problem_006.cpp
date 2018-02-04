#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <math.h>

/*Author: Christian Seely*/


long sumOfSquares(int n)
{
  std::vector<int> range(n);
  std::iota(range.begin(), range.end(), 0);
  for (auto &v : range) v *= v;
  return std::accumulate(range.begin(), range.end(), 0);
}

long squareOfSum(int n)
{
  std::vector<int> range(n);
  std::iota(range.begin(), range.end(), 0);
  return std::pow(std::accumulate(range.begin(), range.end(),0),2);
}


long problemSix()
{
  return squareOfSum(101) - sumOfSquares(101);
}


int main()
{
  std::cout << problemSix() << std::endl;
  return 0;
}

