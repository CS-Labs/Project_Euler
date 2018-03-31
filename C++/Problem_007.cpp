#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <math.h>

/*Author: Christian Seely*/

bool isPrime(int t_n)
{
  int div = 2;
  while (div <= std::sqrt(t_n))
  {
    if (t_n%div == 0) return false;
    div += 1;
  }
  return true;
}

int problemSeven()
{
  int nPrimes = 0;
  int i = 2;
  while (nPrimes < 10001)
  {
    if (isPrime(i)) nPrimes += 1;
    i += 1;
  }
  return (i - 1);
}


int main()
{
  std::cout << problemSeven() << std::endl;
  return 0;
}

