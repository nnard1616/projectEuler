#include <problems/p104.hpp>

namespace problems
{
  int p104() { return optimal_solution(); }
  /*--- Best Solution -- 0.4 sec  --------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  // This uses modulo and the golden ratio to track the bookend digits only.

  bool is_end_pandigital(long long n)
  {
    string number = std::to_string(n);
    auto digits = common::range(1, 10);
    for (auto rit = number.rbegin(); rit < number.rbegin() + 9; ++rit)
    {
      auto loc = std::find(digits.begin(), digits.end(), *rit - '0');
      if (loc == digits.end())  // If digit not found in digits...
        return false;           // then not pandigital.
      digits.erase(loc);
    }

    return true;  // pandigital end
  }

  bool is_front_pandigital(long long n)
  {
    string number = std::to_string(n);

    auto digits = common::range(1, 10);
    for (auto it = number.begin(); it < number.begin() + 9; ++it)
    {
      auto loc = std::find(digits.begin(), digits.end(), *it - '0');
      if (loc == digits.end())  // If digit not found in digits...
        return false;           // then not pandigital.
      digits.erase(loc);
    }

    return true;  // pandigital front
  }

  int optimal_solution()
  {
    long long front[500000];
    long long end[500000];
    front[0] = 0;
    front[1] = 1;
    front[83] = 99194853094755497;
    end[0] = 0;
    end[1] = 1;

    int k = 2;
    while (k < 500000)
    {
      if (k > 83)
      {
        front[k] = front[k - 1] * GOLDENRATIO;
        if (front[k] > BLOCKMAX)
          front[k] /= 10000;
      }
      end[k] = (end[k - 2] + end[k - 1]) % SPACEHOLDER;

      if (is_front_pandigital(front[k]) && is_end_pandigital(end[k]))
        return k;
      k++;
    }
    return 0;
  }


  /*--- First Attempt -- 24 sec ----------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  // This calculates ALL of the fib numbers and their full set of digits.

  int first_try()
  {
    vector<big_number> fib;
    big_number zero;
    big_number one;
    one.blocks[0] = 1;
    fib.push_back(zero);
    fib.push_back(one);

    int k = 2;
    while (k)
    {
      fib.push_back(fib[k - 2] + fib[k - 1]);
      if (fib[k].is_front_pandigital() && fib[k].is_end_pandigital())
        return k;
      k++;
    }
  }
}
