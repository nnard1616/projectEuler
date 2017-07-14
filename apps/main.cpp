#include "problems/p102/p102.hpp"
#include "common/common.hpp"

int main()
{
  cout << std::fixed;
  int start_s = std::clock();

  cout << p102::p102() << endl;

  int stop_s = std::clock();
  cout << "time: " << (stop_s - start_s) / double(CLOCKS_PER_SEC) << endl;
  return 0;
}
