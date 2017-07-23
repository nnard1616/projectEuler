#ifndef P103_HPP
#define P103_HPP
#include <utility>
#include <map>
#include "common/common.hpp"


namespace p103
{
  int p103();

  /*--- Comparator Functions  ------------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  bool is_bigger(std::pair<int, int> i, std::pair<int, int> j);

  bool setCompare(vector<int> i, vector<int> j);


  /*--- (Poor) Algorithm Functions -- 43 seconds -----------------------------*/
  /*--------------------------------------------------------------------------*/

  void product(int n,
               vector<int>& nums,
               vector<int>& temp,
               vector<vector<int>>& prods);

  bool is_really_special(vector<int>& set,
                         vector<int>& temp,
                         vector<std::pair<int, int>>& sizeSums);

  bool partitions(int n,
                  int r,
                  const vector<int>& N,
                  vector<int>& indices,
                  vector<std::pair<int, int>>& sizeSum);


  // Algorithm in a nutshell:
  // Creates all deltas away from base point, which was determined from the
  // erroneous algorithm provided for p103, assuming largest delta to be +/- 4
  // units away from base coordinate. These deltas were applied to the base
  // point, the resulting set of numbers/coordinates were then sorted by
  // increasing sum value. These subsets were one by one partitioned into all
  // subsets.  These subsets were sorted by decreasing sum value.  If a
  // subset size occurred before a larger subset size was finished, the entire
  // set was classified as *not* special.  See example below:

  //   Special:        \   Not Special:
  //   (Size, Sum)     \   (Size, Sum)
  //   (7 , 250)       \   (7 , 250)
  //   (6 , 230)       \   (6 , 230)
  //   (6 , 228)       \   (6 , 228)
  //   (6 , 225)       \   (6 , 225)
  //   (6 , 220)       \   (6 , 220)
  //   (6 , 215)       \   (*5* , 215) <-- ILLEGAL, NOT SPECIAL SET!
  //   (6 , 210)       \   (6 , 210)
  //   (6 , 205)       \   (6 , 205)
  //   (5 , 170)       \   (6 , 170)
  //   (5 , 165)       \   (5 , 165)

  // Since the sets were sorted by increaseing sum value, the first set to be
  // classified as a special sum set was declared the minimal/smallest special
  // sum set, answer p103.  A concatenated string representing the set is
  // printed.
}

#endif  // P103_HPP
