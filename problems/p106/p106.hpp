#ifndef P106_HPP
#define P106_HPP
#include "../p103/p103.hpp"

namespace problems
{
  int p106();

  void generate_subsets(int n,
                        int r,
                        const vector<int>& N,
                        vector<int>& indices,
                        vector<vector<int>>& subsets);
  bool is_disjoint(vector<int>& a, vector<int>& b);

  bool needs_check(vector<int>& a, vector<int>& b);
}

#endif  // P106_HPP
