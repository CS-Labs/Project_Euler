#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <math.h>
#include <execution>

/*Author: Christian Seely*/

int problemFive()
{
  std::vector<int> range(20);
  std::iota(range.begin(), range.end(), 1);
  // Execution method: parallel, start, end, initial acc, custom reduction lambda. 
  // Note, warnings for experimental method usage may need to be suppressed.  (SDL checks for visual studio).
  return std::reduce(std::execution::par, range.begin(), range.end(), 1, [](int a, int b) {return a / std::gcd(a, b)*b;});
}


int main()
{
  std::cout << problemFive() << std::endl;
  return 0;
}

