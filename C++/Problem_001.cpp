#include "stdafx.h"
#include <iostream>
#include <numeric>
#include <algorithm>
#include <vector>
/*Author: Christian Seely*/

int problemOne()
{
  std::vector<int> v(1000);
  std::iota(v.begin(), v.end(), 0);
  v.erase(std::remove_if(v.begin(), v.end(), [](const int& i) {return !(i % 3 == 0 || i % 5 == 0);}), v.end());
  return std::accumulate(v.begin(), v.end(), 0);
}

int main()
{
  std::cout << problemOne() << std::endl;
  return 0;
}

