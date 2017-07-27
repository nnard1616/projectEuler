#include "p106.hpp"

namespace problems
{
  int p106()
  {
    using common::sum;
    using common::mean;

    vector<int> nums = {20, 31, 38, 39, 40, 42, 45};
    //      vector<int> nums = {3,5,6,7};
    //    auto nums = common::range(7);
    int n = nums.size();
    vector<int> temp;
    vector<vector<int>> subsets;
    double setAverage;
    if (n % 2 == 0)
      setAverage = (nums[n / 2] + nums[n / 2 - 1]) / 2.0;
    else
      setAverage = nums[n / 2];


    for (int r = n; r >= n / 2.0; --r)
      generate_subsets(n, r, nums, temp, subsets);

    int c = 0;
    for (unsigned int i = 0; i != subsets.size(); ++i)
      for (unsigned int j = i + 1; j != subsets.size(); ++j)
        if (subsets[i].size() == subsets[j].size())
          if (subsets[i].size() > 1)
            if (is_disjoint(subsets[i], subsets[j]))
            {
              common::print_container(subsets[i]);
              std::sort(subsets[i].begin(), subsets[i].end());
              std::sort(subsets[j].begin(), subsets[j].end());
              if (needs_check(subsets[i], subsets[j]))
              {
                //                common::print_container(subsets[i]);
                //                common::print_container(subsets[j]);
                //                cout << endl;
                c += 1;
              }
            }


    return c;
  }

  void generate_subsets(int n,
                        int r,
                        const vector<int>& N,
                        vector<int>& indices,
                        vector<vector<int>>& subsets)
  {
    if (r == 0)
    {
      //      std::sort(indices.begin(), indices.end());
      //      common::print_container(indices);
      subsets.push_back(indices);

      if (indices.size() != N.size() / 2)
      {
        vector<int> complement;
        for (auto it = N.begin(); it != N.end(); ++it)
          if (std::count(indices.begin(), indices.end(), *it) == 0)
            complement.push_back(*it);
        if (complement.size() > 0)
        {
          //          std::sort(complement.begin(), complement.end());
          //          common::print_container(complement);
          subsets.push_back(complement);
        }
      }

      return;
    }

    for (int i = n; i != r - 1; --i)
    {
      indices.push_back(N[i - 1]);
      generate_subsets(i - 1, r - 1, N, indices, subsets);
      indices.pop_back();
    }
  }

  bool is_disjoint(vector<int>& a, vector<int>& b)
  {
    for (auto iit = a.begin(); iit != a.end(); ++iit)
      for (auto jit = b.begin(); jit != b.end(); ++jit)
        if (*iit == *jit)
          return false;
    return true;
  }

  bool needs_check(vector<int>& a, vector<int>& b)
  {
    float biggerCount = 0;
    for (unsigned int i = 0; i != a.size(); ++i)
      if (a[i] > b[i])
        biggerCount += 1;
    return (std::abs(biggerCount - a.size() / 2.0) <= 0.5);
  }
}
