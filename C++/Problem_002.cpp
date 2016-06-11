#include "stdafx.h"
#include <iostream>
/*Author: Christian Seely*/
int main()
{
	int i = 1;
	int j = 2;
	int k = 0;
	int temp = 0;
	int sum = j;
	while (true)
	{
		k = i + j;
		if (k>4000000)break;
		if (k % 2 == 0)sum += k;
		temp = j;
		j = k;
		i = temp;
	}
	std::cout << sum;
    return 0;
}

