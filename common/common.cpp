#include "common.hpp"

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


  /*--- Pythonic Range Functions  --------------------------------------------*/
  /*--------------------------------------------------------------------------*/


  /*--- Math Functions  ------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
}
