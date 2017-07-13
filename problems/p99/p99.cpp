#include "p99.hpp"

namespace p99
{
  /*--- Main Function --------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  int p99()
  {
    // load base/exponent pairs
    std::ifstream infile("../problems/p99/p099_base_exp.txt");
    vector<baseExp> powers;
    char comma;
    long base;
    long exp;
    while (!(infile.eof()))
    {
      infile >> base >> comma >> exp;
      powers.push_back(baseExp(base, exp));
    }
    infile.close();

    baseExp* maxPower;
    maxPower = &powers[0];
    for (auto it = powers.begin(); it != powers.end(); ++it)
      maxPower = max_power(maxPower, *it);

    return maxPower - &powers[0] + 1;  // Return Line number that the
                                       // base/exponent pair appears on.
  }

  /*--- Helper Functions -----------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  template <typename T>
  long double logN(T& base, T& power)
  {
    return (std::log10(power) / std::log10(base));
  }

  baseExp* max_power(baseExp* current, baseExp& competitor)
  {
    if (competitor.second * logN(current->first, competitor.first) >
        current->second)
      return &competitor;
    else
      return current;
  }
}
