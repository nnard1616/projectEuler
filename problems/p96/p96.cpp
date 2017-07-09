#include "p96.hpp"

namespace p96
{
  void p96()
  {
    number puzzle[9][9];
    puzzle[0][0].contents = 8;

    std::ifstream infile;
    infile.open("../problems/p96/p096_sudoku.txt");
    std::istream_iterator<char> isi(infile);  // need this for advancing
                                              // iterator up one position, see
                                              // comments in
                                              // "read_next_puzzle()"
    read_next_puzzle(puzzle, infile);
    display_puzzle(puzzle);
    cout << endl;
    // START HERE
    // Able to read in puzzles, now need to implement solving algorithm.

    infile.close();
  }

  void display_puzzle(number A[][9])
  {
    for (int i = 0; i < 9; i++)
    {
      for (int j = 0; j < 9; j++)
        cout << std::setw(2) << A[i][j].contents;
      cout << endl;
    }
  }

  std::pair<unsigned int, unsigned int> get_coordinates(int in)
  {  // Each number in sudoku puzzle is indexed from 0 to 80.  This function
     // will take an index and return a ordered pair as the (i,j) coordinates of
     // the number in the sudoku puzzle
    unsigned int row = in / 9;
    unsigned int col = in % 9;
    return std::pair<unsigned int, unsigned int>(row, col);
  }

  unsigned int get_sudoku_index(std::pair<unsigned int, unsigned int> ip)
  {  // this function does the inverse of get_coordinates
    return ip.first * 9 + ip.second;
  }

  void read_next_puzzle(number A[][9], std::istream& infile)
  {
    std::istream_iterator<char> isi(infile);  // If file is already being read,
                                              // this causes isi to increment by
                                              // 1.  How to avoid this?
    for (int i = 0; i != 5; ++i)  // Grid XX header, should go 6 times, but
                                  // until I figure out the isi incrementing
                                  // problem above, this will need to go one
                                  // less, 5 times.
      isi++;

    for (int i = 0; i != 81; ++i)
    {  // In actual puzzle grid
      std::pair<unsigned int, unsigned int> coords = get_coordinates(i);
      A[coords.first][coords.second].contents = *isi - '0';
      A[coords.first][coords.second].coordinates = coords;
      isi++;
    }
  }
}
