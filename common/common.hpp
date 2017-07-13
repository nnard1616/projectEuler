#ifndef COMMON_HPP
#define COMMON_HPP
#include <iostream>
#include <iomanip>
#include <fstream>
#include <istream>
#include <vector>
#include <string>
#include <iterator>
#include <cmath>
#include <ctime>
#include <sstream>
#include <map>
#include <list>
#include <algorithm>
#include <math.h>

using std::vector;
using std::string;
using std::cout;
using std::endl;
using std::list;

namespace common
{
  template <typename T>
  long double logN(T& base, T& power);

  bool is_prime(long long n);
  vector<long long> prime_factors(long long n);

  template <typename T>
  void print(T begin, T end)
  {
    for (auto it = begin; it != end; ++it)
      cout << *it << ' ';
    cout << endl;
  }
  template <typename T>
  void print(T in)
  {
    for (auto it = in.begin(); it != in.end(); ++it)
      cout << *it << ' ';
    cout << endl;
  }
  vector<long long> divisors(long long n);
}
#endif  // COMMON_HPP
