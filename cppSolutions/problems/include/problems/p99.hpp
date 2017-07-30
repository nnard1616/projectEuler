#ifndef P99_HPP
#define P99_HPP
#include <common/common.hpp>
#include <utility>

namespace problems
{
  typedef std::pair<long, long> baseExp;

  int p99();

  template <typename T>
  long double logN(T& base, T& power);

  baseExp* max_power(baseExp* current, baseExp& competitor);
}
#endif  // P99_HPP
