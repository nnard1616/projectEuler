#include "problems/p98/p98.hpp"

int main()
{
  int start_s = std::clock();

  p98::p98();

  int stop_s = std::clock();
  cout << "time: " << (stop_s - start_s) / double(CLOCKS_PER_SEC) << endl;
  return 0;
}
