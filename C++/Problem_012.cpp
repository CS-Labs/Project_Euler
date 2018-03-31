#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>

/*Author: Christian Seely*/

long getNumFactors(int t_n)
{
  long nFactors = 0;
  double bound = std::sqrt(t_n) + 1;
  for (int i = 1; i < bound; i++)
  {
    if (t_n%i == 0) nFactors += 1;
  }
  return (nFactors * 2);
}


long problemTwelve()
{
  int i = 2;
  int sum;
  while (1)
  {
    sum = i * (i + 1) / 2; // Obtain triangle number.
    if (getNumFactors(sum) > 500) return sum;
    i++;
  }

}

int main()
{
  std::cout << problemTwelve() << std::endl;
  return 0;
}

