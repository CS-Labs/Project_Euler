#include "stdafx.h"
#include <iostream>
#include <vector>
/*Author: Christian Seely*/

constexpr size_t problemThree()
{
  size_t max = 0;
  long long n = 600851475143;
  size_t div = 2;
  size_t remainder = 0;
  // Go through every prime factor of the number n.
  // While going through each of the prime factors
  // if a prime factor > max, max = prime factor
  while (1)
  {
    if ((div*div) > n)
    {
      if (n != 1 && n > max) max = n;
      break;
    }
    if (n%div == 0)
    {
      if (div > max) max = div;
      n /= div;
      if (remainder != 0) ++div;
      while (n%div == 0) n /= div;
    }
    ++div;
  }

  return max;
}


int main()
{
  std::cout << problemThree() << std::endl;
  return 0;
}