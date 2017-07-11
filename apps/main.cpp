#include "problems/p98/p98.hpp"

int main()
{
  int start_s = std::clock();

  cout << p98::p98() << endl;

  //  vector<int> stuff;
  //  stuff.push_back(3);
  //  stuff.push_back(4);
  //  stuff.push_back(5);
  //  stuff.push_back(6);

  //  for (auto it = stuff.begin(); it != stuff.end(); ++it)
  //    cout << it[3] << endl;
  int stop_s = std::clock();
  cout << "time: " << (stop_s - start_s) / double(CLOCKS_PER_SEC) << endl;
  return 0;
}
