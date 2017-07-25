#include "p105.hpp"
// This compeltely recycles old code from p103.  See p103 header for explanation
// of algorithm.  Completes in 0.1 s.
namespace problems
{
  int p105()
  {
    using common::strings_to_ints;
    using common::split;
    std::ifstream infile("../problems/p105/p105_sets.txt");
    string line;
    vector<std::pair<int, int>> sizeSums;  // temporary set of (partition size,
                                           // partition sum) pairs.  Used for
                                           // determining if a potential special
                                           // sum set is legitimate.
    vector<int> temp;

    int summation = 0;

    while (std::getline(infile, line))
    {
      vector<int> set = strings_to_ints(split(line, ','));
      if (is_really_special(set, temp, sizeSums))
        summation += common::sum(set);
      sizeSums = {};
      temp = {};
    }
    return summation;
  }
}
