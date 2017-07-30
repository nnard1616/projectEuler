#ifndef P98_HPP
#define P98_HPP
#include <common/common.hpp>
#include <map>

namespace problems
{
  using std::floor;
  using std::ceil;
  using std::pow;
  using std::log10;
  long p98();
  std::map<string, vector<string>> load_word_anagrams(std::istream& infile);

  bool have_equal_unique_char_num(long& n, const string& letters);
  bool is_a_match(long& n, string& word);
  bool is_a_square_anagram(long& n, vector<string>& words);
}
#endif  // P98_HPP
