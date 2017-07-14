#ifndef P101_HPP
#define P101_HPP
#include "common/common.hpp"
#include <armadillo>
using namespace arma;
namespace p101
{
  long long p101();
  void rref(long double A[][11]);
  void swap_rows(long double A[][11], int row1, int row2);
  void display_matrix(long double A[][11]);
  void divide_rows(long double A[][11], int row, long double lead);
  void sub_multiply_row(long double A[][11], int r, int i, long double lead);
  long double un(int n);
  long long OP(double long A[][11], long long n);

  long double larma();
  long double OP(const vec& coefs, long double n);

  long lagrange(int n);
}
#endif  // P101_HPP
