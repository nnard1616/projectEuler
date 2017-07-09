#ifndef P96_HPP
#define P96_HPP
#include "common/common.hpp"
#include <utility>

namespace p96
{
  void p96();
  struct number
  {
    unsigned int contents;
    std::pair<unsigned int, unsigned int> coordinates;
  };
}
#endif  // P96_HPP
