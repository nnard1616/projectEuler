#include "p101.hpp"


namespace p101
{
  /*--- Homemade RREF Matrix Method-------------------------------------------*/
  /*--------------------------------------------------------------------------*/

  long long p101()
  {
    long double m[10][11] = {{0}};
    long double TIMS = 1;

    for (int x = 2; x != 11; ++x)
    {
      for (int i = 0; i != x; ++i)
      {
        m[i][10] = un(i + 1);
        for (int j = 10 - x; j != 10; ++j)
          m[i][j] = pow(i + 1, j - (10 - x));
      }
      rref(m);
      TIMS += OP(m, x + 1);
    }

    return TIMS;
  }

  void rref(long double A[][11])
  {
    int lead = 0;
    int rowCount = 10;
    int colCount = 11;

    for (int r = 0; r != rowCount; ++r)
    {
      if (colCount <= lead)
        return;
      int i = r;
      while (A[i][lead] == 0)
      {
        i++;
        if (rowCount == i)
        {
          i = r;
          lead++;
          if (colCount == lead)
            return;
        }
      }
      swap_rows(A, i, r);
      if (A[r][lead] != 0)
        divide_rows(A, r, A[r][lead]);
      for (int i = 0; i != rowCount; ++i)
        if (i != r)
          sub_multiply_row(A, r, i, A[i][lead]);
      lead++;
    }
  }

  void display_matrix(long double A[][11])
  {
    for (int i = 0; i != 10; ++i)
    {
      for (int j = 0; j != 11; ++j)
        cout << A[i][j] << ' ';
      cout << endl;
    }
  }

  void swap_rows(long double A[][11], int row1, int row2)
  {
    for (int i = 0; i != 11; ++i)
      std::swap(A[row1][i], A[row2][i]);
  }

  void divide_rows(long double A[][11], int row, long double lead)
  {
    for (int j = 0; j != 11; ++j)
      A[row][j] /= lead;
  }

  void sub_multiply_row(long double A[][11], int r, int i, long double lead)
  {
    for (int j = 0; j != 11; ++j)
      A[i][j] -= lead * A[r][j];
  }

  /*--- Polynomial & Approximation Functions ---------------------------------*/
  /*--------------------------------------------------------------------------*/

  long double un(int n)
  {
    return 1 - n + n * n - pow(n, 3) + pow(n, 4) - pow(n, 5) + pow(n, 6) -
           pow(n, 7) + pow(n, 8) - pow(n, 9) + pow(n, 10);
  }

  long long OP(double long A[][11], long long n)  // approximation
  {
    long long summation = 0;
    for (int i = 0; i != 10; ++i)
      summation += A[i][10] * pow(n, i);
    return summation;
  }

  /*--- Linear Algebra Method ------------------------------------------------*/
  /*--- Using Armadillo Library ----------------------------------------------*/

  long double larma()
  {
    long double TIMS = 1;
    long double size = 2;
    mat m(size, size);
    vec v(size);

    while (size != 11)
    {
      for (int i = 0; i != size; ++i)
      {
        v(i) = un(i + 1);
        for (int j = 0; j != size; ++j)
          m(i, j) = pow(i + 1, j);
      }
      TIMS += OP(solve(m, v), size + 1);
      size++;
      m.set_size(size, size);
      v.set_size(size);
    }
    return TIMS;
  }

  long double OP(const vec& coefs, long double n)  // larma approximation
  {
    long double summation = 0;
    for (unsigned long long i = 0; i != coefs.size(); ++i)
      summation += coefs(i) * pow(n, i);
    return summation;
  }

  /*--- Lagrange Method -- From Internet -------------------------------------*/
  /*----BEST METHOD!----------------------------------------------------------*/

  long lagrange(int n)
  {
    long result = 0;
    for (long i = 1; i <= n; ++i)
    {
      long temp1 = 1;
      long temp2 = 1;
      for (long j = 1; j <= n; j++)
      {
        if (i == j)
          continue;
        else
        {
          temp1 *= n + 1 - j;
          temp2 *= i - j;
        }
      }
      result += temp1 * un(i) / temp2;
    }
    return result;
  }
}
