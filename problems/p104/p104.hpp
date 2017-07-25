#ifndef P104_HPP
#define P104_HPP
#include "common/common.hpp"
#define BLOCKMAX 1000000000000000000        // 10^18
#define GOLDENRATIO (1 + std::sqrt(5)) / 2  // for best solution.
#define SPACEHOLDER 1000000000              // 10^9, for best solution.

namespace problems
{
  int p104();


  /*--- Best Solution -- 0.4 sec  --------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  bool is_front_pandigital(long long n);
  bool is_end_pandigital(long long n);
  int optimal_solution();


  /*--- First Attempt -- 24 sec  ---------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  // I have a lot to learn about operator overloading and class/struct
  // private/public member interactions...

  int first_try();

  struct big_number
  {
    vector<long long> blocks;

    big_number() { blocks = {0}; }
    long long& operator[](unsigned int i) { return blocks[i]; }
    const long long& operator[](unsigned int i) const { return blocks[i]; }
    big_number& operator=(const big_number& other)
    {
      std::copy(other.blocks.begin(), other.blocks.end(), this->blocks.begin());
      return *this;
    }

    big_number operator+(big_number& rhs)
    {
      big_number result;
      result.blocks = {0};
      while (this->blocks.size() > rhs.blocks.size())
        rhs.blocks.push_back(0);
      while (this->blocks.size() < rhs.blocks.size())
        this->blocks.push_back(0);
      while (result.blocks.size() < rhs.blocks.size())
        result.blocks.push_back(0);
      // clang-format off
      unsigned int maxI = result.blocks.size();
      for (unsigned int i = 0; i != maxI; ++i)
      {
        result[i] += (blocks[i] + rhs[i]);
        if (result[i] > BLOCKMAX) //did we reach block's max value it can hold?
        {//yes, we need to carry a 1
          result[i] -= BLOCKMAX; //remove first digit
          if (i == result.blocks.size() - 1) //are we at end of blocks?
            result.blocks.push_back(1); //yes, make new block with 1
          else //no, add 1 to next already existing block
            result[i + 1] += 1;
        }//no, move on to next block
      }
      // clang-format on
      return result;
    }

    template <typename ForwardIterator>
    string concatenate_integers(ForwardIterator first, ForwardIterator last)
    {
      string cat = "";
      string s = std::to_string(*first);
      cat += s;
      first++;

      while (first != last)
      {
        s = std::to_string(*first);
        for (unsigned long i = 0; i != 18 - s.size(); ++i)
          cat += "0";  // leading zeroes
        cat += s;
        first++;
      }

      return cat;
    }

    void print()
    {
      cout << concatenate_integers(blocks.rbegin(), blocks.rend()) << endl;
    }

    bool is_end_pandigital()
    {
      string number = concatenate_integers(blocks.begin(), blocks.begin() + 1);
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

    bool is_front_pandigital()
    {
      string number =
          concatenate_integers(blocks.rbegin(), blocks.rbegin() + 2);
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
  };
}

#endif  // P104_HPP
