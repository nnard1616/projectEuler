#include "common.hpp"

namespace common
{
  /*--- Container Functions  -------------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  //  template <typename ForwardIterator>
  //  void print_container(ForwardIterator first, ForwardIterator last)
  //  {
  //    while (first != last)
  //      cout << *first++ << ' ';
  //    cout << endl;
  //  }

  //  template <typename Container>
  //  void print_container(Container in)
  //  {
  //    print_conainer(in.begin(), in.end());
  //  }

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

  //  template <typename IntType>
  //  std::vector<IntType> range(IntType start, IntType stop, IntType step)
  //  {
  //    if (step == IntType(0))
  //    {
  //      throw std::invalid_argument("step for range must be non-zero");
  //    }

  //    std::vector<IntType> result;
  //    IntType i = start;
  //    while ((step > 0) ? (i < stop) : (i > stop))
  //    {
  //      result.push_back(i);
  //      i += step;
  //    }

  //    return result;
  //  }

  //  template <typename IntType>
  //  std::vector<IntType> range(IntType start, IntType stop)
  //  {
  //    return range(start, stop, IntType(1));
  //  }

  //  template <typename IntType>
  //  std::vector<IntType> range(IntType stop)
  //  {
  //    return range(IntType(0), stop, IntType(1));
  //  }


  /*--- Math Functions  ------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  template <typename Numerical>
  long double logN(Numerical& base, Numerical& power)
  {
    return (std::log10(power) / std::log10(base));
  }

  template <typename ForwardIterator>
  auto sum(ForwardIterator first, ForwardIterator last)
  {
    int s = 0;
    while (first != last)
      s += *first++;
    return s;
  }

  template <typename NumericalContainer>
  auto sum(NumericalContainer in)
  {
    return sum(in.begin(), in.end());
  }

  template <typename Integral>
  bool is_prime(Integral n)
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
    for (Integral i = 2; i * i <= n; ++i)
      if (n % i == 0)
        return false;
    return true;
  }

  template <typename Integral>
  vector<Integral> prime_factors(Integral n)
  {
    vector<Integral> primeFactors;
    for (Integral i = 2; i * i <= n; ++i)
      while (n % i == 0)
      {
        primeFactors.push_back(i);
        n /= i;
        if (is_prime(n))
          primeFactors.push_back(n);
      }
    return primeFactors;
  }

  template <typename Integral>
  vector<Integral> divisors(Integral n)
  {
    vector<Integral> d = {1, n};
    for (Integral i = 2; i * i <= n; ++i)
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
}
