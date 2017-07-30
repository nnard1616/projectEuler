#include <problems/p103.hpp>

namespace problems
{
  int p103()
  {
    vector<int> set = {22, 33, 39, 42, 44, 45, 46};  // base point
    vector<vector<int>> prods;  // set of sets of deltas from base point
    vector<std::pair<int, int>> sizeSums;  // temporary set of (partition size,
                                           // partition sum) pairs.  Used for
                                           // determining if a potential special
                                           // sum set is legitimate.
    vector<int> temp;  // temp container for populating 'prods' and 'sizeSums'

    auto nums = common::range(-4, 5);  // all possible deltas, guessing largest
                                       // in magnitude delta will be 4

    product(set.size(), nums, temp, prods);
    cout << "Done Making Products of Changes..." << endl;

    cout << prods.size() << endl;
    for (auto it = prods.begin(); it != prods.end(); ++it)
    {
      for (unsigned int i = 0; i != set.size(); ++i)
      {
        (*it)[i] += set[i];
      }
    }  // deltas applied to base point

    cout << "sorting" << endl;
    std::sort(prods.begin(), prods.end(), setCompare);

    cout << "done sorting, searching now..." << endl;
    for (auto it = prods.begin(); it != prods.end(); ++it)
    {
      if (is_really_special(*it, temp, sizeSums))
      {  // Since potentials are sorted, the first legitimate encountered will
         // be the minimum special sum set.
        std::sort(it->begin(), it->end());
        cout << common::concatenate_integers(*it) << endl;
        return 1;
      }
      sizeSums = {};
      temp = {};
    }

    return 0;
  }


  /*--- Comparator Functions  ------------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  bool is_bigger(std::pair<int, int> i, std::pair<int, int> j)
  {
    return (i.second > j.second);
  }

  bool setCompare(vector<int> i, vector<int> j)
  {
    using common::sum;
    return sum(i.begin(), i.end()) < sum(j.begin(), j.end());
  }


  /*--- (Poor) Algorithm Functions -- 43 seconds -----------------------------*/
  /*--------------------------------------------------------------------------*/

  void product(int n,
               vector<int>& nums,
               vector<int>& temp,
               vector<vector<int>>& prods)
  {
    if (n == 0)
    {
      prods.push_back(temp);
      return;
    }

    for (auto it = nums.begin(); it != nums.end(); ++it)
    {
      temp.push_back(*it);
      product(n - 1, nums, temp, prods);
      temp.pop_back();
    }
  }


  bool is_really_special(vector<int>& set,
                         vector<int>& temp,
                         vector<std::pair<int, int>>& sizeSums)
  {
    for (int r = set.size(); r >= set.size() / 2.0; --r)
      if (!(partitions(set.size(), r, set, temp, sizeSums)))
        return false;


    std::sort(sizeSums.begin(), sizeSums.end(), is_bigger);

    int prevSize = set.size();
    int prevSum = 0;
    int dif;
    for (auto it = sizeSums.begin(); it != sizeSums.end(); ++it)
    {
      dif = it->first - prevSize;
      cout << it->first << ',' << it->second << endl;
      if ((dif == 0) || (dif == -1))
      {
        prevSize = it->first;
        if (prevSum != it->second)  // subsets can't equal each other
          prevSum = it->second;
        else
          return false;
      }
      else
      {
        return false;
      }
    }

    return true;
  }


  // only checks bipartitions that make the complete set combined.
  bool partitions(int n,
                  int r,
                  const vector<int>& N,
                  vector<int>& indices,
                  vector<std::pair<int, int>>& sizeSum)
  {
    if (r == 0)
    {
      int selectionSum = 0;
      int nonSelectionSum = 0;
      for (auto it = N.begin(); it != N.end(); ++it)
      {
        if (std::count(indices.begin(), indices.end(),
                       std::find(N.begin(), N.end(), *it) - N.begin()))
          selectionSum += *it;
        else
          nonSelectionSum += *it;
      }

      if (indices.size() > N.size() / 2)
      {
        if (selectionSum > nonSelectionSum)
        {
          sizeSum.push_back({indices.size(), selectionSum});
          sizeSum.push_back({N.size() - indices.size(), nonSelectionSum});

          return true;
        }
        else
          return false;
      }
      if (indices.size() == N.size() / 2)
      {
        if (selectionSum != nonSelectionSum)
        {
          sizeSum.push_back({indices.size(), selectionSum});
          return true;
        }
        else
          return false;
      }
    }

    for (int i = n; i != r - 1; --i)
    {
      indices.push_back(i - 1);
      if (partitions(i - 1, r - 1, N, indices, sizeSum))
        indices.pop_back();
      else
        return false;
    }
    return true;
  }
}
