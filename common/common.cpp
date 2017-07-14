#include "common.hpp"

namespace common
{
  template <typename T>
  long double logN(T& base, T& power)
  {
    return (std::log10(power) / std::log10(base));
  }

  bool is_prime(long long n)
  {
    if (n < 1)
    {
      cout << "WARNING: n < 1 passed to is_prime!" << endl;
      return false;
    }
    if (n == 1)
      return false;
    if (n == 2)
      return true;
    if (n == 3)
      return true;
    for (long long i = 2; i * i <= n; ++i)
      if (n % i == 0)
        return false;
    return true;
  }

  vector<long long> prime_factors(long long n)
  {
    vector<long long> primeFactors;
    for (long long i = 2; i * i <= n; ++i)
      while (n % i == 0)
      {
        primeFactors.push_back(i);
        n /= i;
        if (is_prime(n))
          primeFactors.push_back(n);
      }
    return primeFactors;
  }

  vector<long long> divisors(long long n)
  {
    vector<long long> d = {1, n};
    for (long long i = 2; i * i <= n; ++i)
    {
      if (n % i == 0)
      {
        d.push_back(i);
        d.push_back(n / i);
      }
    }
    std::sort(d.begin(), d.end());
    return d;
  }

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
}
