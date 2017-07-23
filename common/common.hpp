#ifndef COMMON_HPP
#define COMMON_HPP
#include <iostream>
#include <iomanip>
#include <fstream>
#include <istream>
#include <vector>
#include <string>
//#include <iterator>
#include <cmath>
//#include <ctime>
#include <sstream>
//#include <map>
//#include <list>
#include <algorithm>
//#include <math.h>
//#include <set>

using std::vector;
using std::string;
using std::cout;
using std::endl;


namespace common
{
  /*--- Container Functions  -------------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  //  template <typename ForwardIterator>
  //  void print_container(ForwardIterator first, ForwardIterator last);

  //  template <typename Container>
  //  void print_container(Container in);

  template <typename ForwardIterator>
  void print_container(ForwardIterator first, ForwardIterator last)
  {
    while (first != last)
      cout << *first++ << ' ';
    cout << endl;
  }

  template <typename Container>
  void print_container(Container in)
  {
    print_container(in.begin(), in.end());
  }

  vector<string> split(const string& s, char delim);


  /*--- Pythonic Range Functions  --------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  //  template <typename IntType>
  //  std::vector<IntType> range(IntType start, IntType stop, IntType step);

  //  template <typename IntType>
  //  std::vector<IntType> range(IntType start, IntType stop);

  //  template <typename IntType>
  //  std::vector<IntType> range(IntType stop);

  template <typename IntType>
  std::vector<IntType> range(IntType start, IntType stop, IntType step)
  {
    if (step == IntType(0))
    {
      throw std::invalid_argument("step for range must be non-zero");
    }

    std::vector<IntType> result;
    IntType i = start;
    while ((step > 0) ? (i < stop) : (i > stop))
    {
      result.push_back(i);
      i += step;
    }

    return result;
  }

  template <typename IntType>
  std::vector<IntType> range(IntType start, IntType stop)
  {
    return range(start, stop, IntType(1));
  }

  template <typename IntType>
  std::vector<IntType> range(IntType stop)
  {
    return range(IntType(0), stop, IntType(1));
  }


  /*--- Math Functions  ------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  template <typename Numerical>
  long double logN(Numerical& base, Numerical& power);

  template <typename ForwardIterator>
  auto sum(ForwardIterator first, ForwardIterator last);

  template <typename NumericalContainer>
  auto sum(NumericalContainer in);

  template <typename Integral>
  bool is_prime(Integral n);

  template <typename Integral>
  vector<Integral> prime_factors(Integral n);

  template <typename Integral>
  vector<Integral> divisors(Integral n);
}
#endif  // COMMON_HPP
