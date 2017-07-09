#include "p96.hpp"
/*I used the "Back-Track" method for solving the sudoku puzzles.  See wikipedia
 * for illustrations and animations for how the algorithm works.  Also look at
 * the notes in "solve_sudoku" for more details */

namespace p96
{
  /*--- Main Function --------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  void p96()
  {
    number puzzle[9][9];

    std::ifstream infile;
    infile.open("../problems/p96/p096_sudoku.txt");
    std::istream_iterator<char> isi(infile);  // need this for advancing
                                              // iterator up one position, see
                                              // comments in
                                              // "read_next_puzzle()"
    int summation = 0;
    for (int c = 0; c != 50; c++)
    {
      read_next_puzzle(puzzle, infile);  // load next puzz
      solve_sudoku(puzzle);              // solve puzz
      for (int j = 0; j != 3; j++)  // needed for answering projectEuler.net
        summation += puzzle[0][j].contents * std::pow(10, 3 - j - 1);
      // example for how previous line works:
      //  483 = 4*10^2 + 8*10^1 + 3*10^0
    }
    cout << summation << endl;  // feed to projectEuler.net

    infile.close();
  }

  /*--- Display Puzzle -------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  void display_puzzle(number A[][9])
  {
    for (int i = 0; i < 9; i++)
    {
      for (int j = 0; j < 9; j++)
        cout << std::setw(2) << A[i][j].contents;
      cout << endl;
    }
  }

  /*--- Navigation Functions -------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  coor get_coordinates(int in)
  {  // Each number in sudoku puzzle is indexed from 0 to 80.  This function
     // will take an index and return a ordered pair as the (i,j) coordinates of
     // the number in the sudoku puzzle
    unsigned int row = in / 9;
    unsigned int col = in % 9;
    return coor(row, col);
  }

  unsigned int get_sudoku_index(coor ip)
  {  // this function does the inverse of get_coordinates
    return ip.first * 9 + ip.second;
  }

  unsigned int mod_floor(unsigned int n, unsigned int d)
  {  // for finding group
    // [0,2] -> 0; [3,5] -> 3; [6,8] -> 6
    while (n % d != 0)
      n--;
    return n;
  }

  /*--- Load Puzzle Function -------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  void read_next_puzzle(number A[][9], std::istream& infile)
  {
    std::istream_iterator<char> isi(infile);  // If file is already being read,
                                              // this causes isi to increment by
                                              // 1.  How to avoid this?
    for (int i = 0; i != 5; ++i)  // Grid XX header, should go 6 times to skip
                                  // over header, but until I figure out the isi
                                  // incrementing problem above, this will need
                                  // to go one less: 5 times.
      isi++;
    coor prev(-1, -1);
    for (int i = 0; i != 81; ++i)
    {  // In actual puzzle grid

      coor coords = get_coordinates(i);
      A[coords.first][coords.second].given =
          false;  // redefine as false for next read

      A[coords.first][coords.second].contents = *isi - '0';
      A[coords.first][coords.second].coordinates = coords;
      if (A[coords.first][coords.second].contents != 0)
        A[coords.first][coords.second].given = true;

      if (A[coords.first][coords.second].contents == 0)
      {
        A[coords.first][coords.second].previous = prev;
        prev = A[coords.first][coords.second].coordinates;
      }
      isi++;
    }
  }

  /*--- Checker Functions ----------------------------------------------------*/
  /*---'n' is the number we're checking for-----------------------------------*/
  bool does_row_have(number A[][9], unsigned int row, unsigned int n)
  {
    for (int j = 0; j != 9; ++j)
      if (A[row][j].contents == n)
        return true;
    return false;
  }

  bool does_col_have(number A[][9], unsigned int col, unsigned int n)
  {
    for (int i = 0; i != 9; ++i)
      if (A[i][col].contents == n)
        return true;
    return false;
  }

  bool does_group_have(number A[][9], coor& ip, unsigned int n)
  {  //'group' is one of the nine 3x3 sub-grids in sudoku puzzle
    int groupRowStart = mod_floor(ip.first, 3);
    int groupColStart = mod_floor(ip.second, 3);
    for (int i = groupRowStart; i != groupRowStart + 3; i++)
      for (int j = groupColStart; j != groupColStart + 3; j++)
        if (A[i][j].contents == n)
          return true;
    return false;
  }
  /*--- Solver Function ------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  void solve_sudoku(number A[][9])
  {  // This implements the "back-track" method of solving sudoku:
    // Fill out cells left to right, row by row with smallest number possible
    // If no number can be put in a cell, go back to previous cell and see if
    // another bigger number could be used instead.  If nothing changes for the
    // former cell, go back another cell and so on until each cell has a number
    int j = 0;
    while (j < 81)
    {
      coor location = get_coordinates(j);
      unsigned int current = A[location.first][location.second].contents;
      // attempt to put a number in cell, starting with smallest possible.
      if (A[location.first][location.second].given == false)
      {
        for (int n = current; n != 10; n++)  // start from n = current, as the
                                             // numbers smaller than current
                                             // have already been tested.
          if (!(does_row_have(A, location.first, n) ||
                does_col_have(A, location.second, n) ||
                does_group_have(A, location, n)))
          {
            A[location.first][location.second].contents = n;
            break;
          }
      }
      j++;  // move on, unless....

      // using 'current', we check to see if the contents changed.  If they
      // didn't, that means we were unable to place  a value in the cell.
      // Hence, we "back-track" to the previous cell
      if (current == A[location.first][location.second].contents &&
          A[location.first][location.second].given == false)
      {  // if there's no change to current entry
        j = get_sudoku_index(A[location.first][location.second].previous);
        A[location.first][location.second].contents = 0;
      }  // then take us back to previous entry
    }
  }
}
