#include "stdafx.h"
#include <iostream>
#include <vector>
/*Author: Christian Seely*/

long problemThree()
{
	long max = 0;
	long long n = 600851475143;
	std::vector<long> primeFactors;
	long div = 2;
	bool terminate = false;
	long remainder = 0;
	//Fill primeFactors with prime factors of n. 
	while (!terminate)
	{
		if ((div*div) > n)
		{
			if (n != 1)
			{
				primeFactors.push_back(n);
				terminate = true;
			}
			else
			{
				terminate = true;
			}
		}
		if (n%div == 0 && !terminate)
		{
			primeFactors.push_back(div);
			n /= div;
			if (remainder != 0)++div;
			while (n%div == 0 && !terminate) n /= div;
		}
		++div;
	}
	//Find largest prime factor in prime factors.
	for (long pf : primeFactors)
	{
		if (pf > max) max = pf;
	}

	return max;
}


int main()
{
	std::cout << problemThree() << std::endl;
	return 0;
}

