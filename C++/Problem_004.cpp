#include "stdafx.h"
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <string>

/*Author: Christian Seely*/


class PalindromicMultipleFactory
{
public:
	PalindromicMultipleFactory(const std::vector<int>& singles) : singles{ singles } { generatePalindromicMultiples(singles); }

	const std::vector<int>& getPalindromicMultiples() const { return palindromicMultiples;  }

private:
	std::vector<int> singles;
	std::vector<int> palindromicMultiples;
	std::vector<std::vector<int>> parings;
	std::vector<int> pair;

	bool isPalindromicMultiple(int mult)
	{
		std::string tmp = std::to_string(mult);
		int len = tmp.length();
		std::string fHalf, sHalf;
		if (len % 2 == 0) 
		{
			fHalf = tmp.substr(0, len / 2);
			sHalf = tmp.substr(len / 2, len);
		}
		else // Odd # of digits -> Ignore middle digit. 
		{
			fHalf = tmp.substr(0, len / 2);
			sHalf = tmp.substr(len / 2 + 1, len);
		}
		std::reverse(sHalf.begin(), sHalf.end()); // Reverse second half before comparing. 
		return (fHalf == sHalf);

	}
	
	// Generate all N choose 2 combinations. 
	void genParings(int offset, int k) {
		if (k == 0)
		{
			parings.push_back(pair);
			return;
		}
		for (int i = offset; i <= singles.size() - k; ++i) 
		{
			pair.push_back(singles[i]);
			genParings(i + 1, k - 1);
			pair.pop_back();
		}
	}



	void generatePalindromicMultiples(const std::vector<int>& singles)
	{
		genParings(0,2); // n choose 2; 
		for (auto& pair : parings)
		{
			if (isPalindromicMultiple(pair[0] * pair[1])) palindromicMultiples.push_back(pair[0] * pair[1]);
		}
	}
};



int problemFour()
{
	std::vector<int> singles(900); 
	std::iota(singles.begin(), singles.end(), 100); // 100 to 999.
	PalindromicMultipleFactory pmFactory{ singles };
	std::vector<int> palindromicMultiples = pmFactory.getPalindromicMultiples();
	auto max =  std::max_element(palindromicMultiples.begin(), palindromicMultiples.end());
	return *max; // Get value by dereferencing iterator. 
}


int main()
{
	std::cout << problemFour() << std::endl;
	
	return 0;
}

