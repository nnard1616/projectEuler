#include <common/common.hpp>

namespace common
{
  /*--- Container Functions  -------------------------------------------------*/
  /*--------------------------------------------------------------------------*/


  /*--- String Functions  ----------------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  vector<string> split(const string& s, char delim)
  {
    std::stringstream ss;
    ss.str(s);

    string item;
    vector<string> items;

    while (std::getline(ss, item, delim))
      items.push_back(item);  // populate items
    return items;
  }


  vector<int> strings_to_ints(vector<string> in)
  {
    vector<int> ints;
    for (auto it = in.begin(); it != in.end(); ++it)
      ints.push_back(std::stoi(*it));
    return ints;
  }


  /*--- Pythonic Range Functions  --------------------------------------------*/
  /*--------------------------------------------------------------------------*/


  /*--- Math Functions  ------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
}
