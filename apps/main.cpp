#include "problems/p103/p103.hpp"
#include "common/common.hpp"

int main()
{
  cout << std::fixed;
  int start_s = std::clock();
  auto nums = common::range(10);

  common::print_container(nums);

  int stop_s = std::clock();
  cout << "time: " << (stop_s - start_s) / double(CLOCKS_PER_SEC) << endl;
  return 0;
}
