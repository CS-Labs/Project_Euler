#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>

/*Author: Christian Seely*/

/*
 Method to find the primes from 2 to 2,000,000
 using the Sieve of Eratosthenes algorithm and then
 sum them all together.
*/
long long problemTen()
{
  int scope = 2000000;
  // The index in the array represents a natural number.
    // The possible values at each index have the following meaning :
  // 1 = Prime, 0 = Not prime.
  std::vector<int> n(scope, 1);
  int bound = std::sqrt(n.size());
  int j, k;
  for (int i = 2; i < bound; i++)
  {
    if (n[i] == 1)
    {
      j = (i*i);
      k = 1;
      while (j < scope)
      {
        n[j] = 0;
        j = (i*i) + (k*i);
        k += 1;
      }
    }
  }
  long long sum = 0;
  // Sum all the primes. 
  for (int i = 2; i < scope; i++)
  {
    if (n[i]) sum += i;
  }
  return sum;
}


int main()
{
  std::cout << problemTen() << std::endl;
  return 0;
}

