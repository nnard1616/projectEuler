#ifndef P96_HPP
#define P96_HPP
#include "common/common.hpp"
#include <utility>

namespace p96
{
  void p96();
  struct number
  {
    unsigned int contents = 0;
    std::pair<unsigned int, unsigned int> coordinates;
  };
  void display_puzzle(number A[][9]);
  std::pair<unsigned int, unsigned int> get_coordinates(int in);
  unsigned int get_sudoku_index(std::pair<unsigned int, unsigned int> ip);
  void read_next_puzzle(number A[][9], std::istream& infile);
}
#endif  // P96_HPP
