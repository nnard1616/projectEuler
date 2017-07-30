#ifndef P96_HPP
#define P96_HPP
#include <common/common.hpp>
#include <utility>
#include <iterator>

namespace problems
{
  typedef std::pair<unsigned int, unsigned int> coor;
  void p96();  // main

  struct number
  {
    unsigned int contents = 0;
    bool given = false;
    coor coordinates;
    coor previous;
  };  // container for single number space in puzzle

  void display_puzzle(number A[][9]);  // show puzzle

  // Navigation functions
  coor get_coordinates(int in);
  unsigned int get_sudoku_index(coor ip);  // inverse of get_coordinates
  unsigned int mod_floor(unsigned int n, unsigned int d);  // for finding group

  void read_next_puzzle(number A[][9], std::istream& infile);  // Load puzzle

  // checker functions
  bool does_row_have(number A[][9], unsigned int row, unsigned int n);
  bool does_col_have(number A[][9], unsigned int col, unsigned int n);
  bool does_group_have(number A[][9], coor& ip, unsigned int n);

  // Solver function
  void solve_sudoku(number A[][9]);
}
#endif  // P96_HPP
