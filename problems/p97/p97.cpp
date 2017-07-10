#include "p97.hpp"

namespace p97
{
  /*--- Main Function --------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  void p97()
  {
    long prod = 1;
    for (int i = 0; i != 7830457; i++)
    {
      prod *= 2;
      if (prod >= std::pow(10, 10))
        prod -= std::pow(10, 10);
    }
    prod *= 28433;
    prod += 1;
    std::ostringstream ss;
    ss << std::fixed << prod;
    string num = ss.str();

    for (auto it = num.end() - 10; it != num.end(); it++)
      cout << *it;

    cout << endl;
  }
}
