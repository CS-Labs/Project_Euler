#include "stdafx.h"
#include <iostream>
#include <numeric>
#include <iterator>
#include <valarray>

/*Author: Christian Seely*/


// Determine if an integer is palindromic by reversing the
// integers digits and comparing it to the original. 
bool isPalindromicMultiple(int t_mult) {
  int forward = t_mult;
  int reverse = 0;
  while (t_mult > 0) {
    int currDigit = t_mult % 10;
    t_mult /= 10;
    reverse = reverse * 10 + currDigit;
  }
  return forward == reverse;
}

int problemFour()
{
  std::valarray<int> singles(900); 
  int max = 0;
  std::iota(std::begin(singles), std::end(singles), 100); // All valid 3 digit numbers, 100-999.
  // Iterate through each of the valid three digit numbers and multiple the scalar value to the 
  // vector range 100-999 to get a strip of permutations were the values are multiplied together. 
  // Next for all non palindromic multiples in the strip we set the value to zero. Next we get
  // the max value of the strip or the max palindromic multiple and if it is greater than our 
  // overall max then our overall max is updated. This is continued on for every strip. 
  for (auto &val : singles) 
  {
    auto stripMax = (singles*val).apply([](int v) {return isPalindromicMultiple(v) ? v : 0;}).max();
    if (stripMax > max) max = stripMax;
  }
  return max;
}


int main()
{
  std::cout << problemFour() << std::endl;
  
  return 0;
}
