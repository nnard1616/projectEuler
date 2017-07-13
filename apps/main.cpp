#include "problems/p100/p100.hpp"
#include "common/common.hpp"

int main()
{
  cout << std::fixed;
  int start_s = std::clock();

  cout << p100::p100() << endl;

  int stop_s = std::clock();
  cout << "time: " << (stop_s - start_s) / double(CLOCKS_PER_SEC) << endl;
  return 0;
}
