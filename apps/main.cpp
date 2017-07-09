#include "problems/p96/p96.hpp"

int main()
{
  p96::p96();  // this prints "1" when return_one() below is present.  A linker
               // error appears when return_one() is removed below
  return_one();
  return 0;
}
