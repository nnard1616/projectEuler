#include <problems/p103.hpp>
#include <problems/p105.hpp>
#include <problems/p106.hpp>

void swap(int& a, int& b)
{
  int tmp = a;
  a = b;
  b = tmp;
}


int main()
{
  cout << std::fixed;
  int start_s = std::clock();

  char a[5] = {'a', 'b', 'c', 'd', 'e'};
  char b[5] = {'a', 'b', 'c', 'd', 'e'};
  if (a == b)
  {
    cout << true << endl;
  }
  //  cout << common::is_prime(45615316601) << endl;
  //  cout << problems::p106() << endl;
  //  string line = "20,31,38,39,40,42,45";
  //  vector<int> ints = common::strings_to_ints(common::split(line, ','));

  //  vector<std::pair<int, int>> sizeSums;  // temporary set of (partition
  //  size,
  //                                         // partition sum) pairs.  Used for
  //                                         // determining if a potential
  //                                         special
  //                                         // sum set is legitimate.
  //  vector<int> temp;

  //  common::print_container(ints);
  //  if (problems::is_really_special(ints, temp, sizeSums))
  //    cout << "HELL YES" << endl;
  //  sizeSums = {};
  //  temp = {};

  int stop_s = std::clock();
  cout << "time: " << (stop_s - start_s) / double(CLOCKS_PER_SEC) << endl;
  return 0;
}
