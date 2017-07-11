#include "p98.hpp"

namespace p98
{
  /*--- Main Function --------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  long p98()
  {
    std::ifstream infile("../problems/p98/p098_words.txt");
    std::map<string, vector<string>> wordAnagrams = load_word_anagrams(infile);
    infile.close();

    // Get largest possible anagram number from longest word in 'wordAnagrams'
    double maxNum = 0;
    for (auto it = wordAnagrams.begin(); it != wordAnagrams.end(); ++it)
      maxNum = std::max(maxNum, pow(10, it->first.size()));

    // Generate vector of square numbers up to 'maxNum'
    vector<long> squares;
    for (long i = 0; pow(i, 2) < maxNum; i++)
      squares.push_back(pow(i, 2));

    // Compare squares to anagramic words
    for (auto rit = squares.rbegin(); rit != squares.rend(); ++rit)
      for (auto it = wordAnagrams.begin(); it != wordAnagrams.end(); ++it)
        if (std::to_string(*rit).size() == it->first.size())  // same length
          if (have_equal_unique_char_num(*rit, it->first))
            if (is_a_match(*rit, it->second[0]))  // see function def below
              if (is_a_square_anagram(*rit, it->second))
                return *rit;  // answer to projectEuler problem has been found

    return 0;  // answer not found
  }

  /*--- Load Function --------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  std::map<string, vector<string>> load_word_anagrams(std::istream& infile)
  {
    string word;                                   // getline parser
    std::map<string, vector<string>> nonAnagrams;  // contains anagrams
    std::map<string, vector<string>> anagrams;     // subset of nonAnagrams

    while (std::getline(infile, word, ','))
    {
      string subword = word.substr(1, word.length() - 2);  // Gets rid of " "
      if (subword.length() > 3)  // I guess answer will be more than 3 letters
      {
        string letters = subword;  // gonna alphabetize word's letters, map key
        std::sort(letters.begin(), letters.end());  // alphabetized

        // generate anagrams' map values
        if (nonAnagrams[letters].size() > 0)
        {  // we have a anagram pair/set
          nonAnagrams[letters].push_back(subword);
          anagrams[letters] = nonAnagrams[letters];
        }
        else  // first word of this letters type, may or may not be anagram set
          nonAnagrams[letters].push_back(subword);
      }
    }

    // anagrams map example:
    // Key: "OPST" -> Value: ["STOP", "POST", "SPOT"]
    // NOTE: "OPST" is only anagram set with more than 2 words
    return anagrams;
  }

  /*--- Matcher Functions ----------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  bool have_equal_unique_char_num(long& n, const string& letters)
  {  // counts unique characters in 'n' and 'letters'
     // returns true if same number of uniques, false otherwise

    string alphaUniques;
    for (auto it = letters.begin(); it != letters.end(); ++it)
      if (alphaUniques.find(*it) == string::npos)
        alphaUniques.push_back(*it);

    string sn = std::to_string(n);
    string digitUniques;
    for (auto it = sn.begin(); it != sn.end(); ++it)
      if (digitUniques.find(*it) == string::npos)
        digitUniques.push_back(*it);

    return alphaUniques.size() == digitUniques.size();
  }

  bool is_a_match(long& n, string& word)
  {  // Match: n and word have identical char lengths and orders

    std::map<int, char> dtoa;  // digit to alpha
    string sn = std::to_string(n);
    for (auto it = sn.begin(); it != sn.end(); ++it)
      // going over digits in 'n' to map them to a alpha in word
      dtoa[*it] = word[sn.find(*it)];

    string transcription;  // word from number
    for (auto it = sn.begin(); it != sn.end(); ++it)
      transcription.push_back(dtoa[*it]);

    return transcription == word;
  }

  bool is_a_square_anagram(long& n, vector<string>& words)
  {
    std::map<char, int> atod;  // alpha to digit
    string sn = std::to_string(n);

    bool winner = false;     // no chicken dinner
    long transcription = 0;  // number from word

    for (int w = 0; w != 2; ++w)
    {  // First iteration checks if first word creates anagramic square that
       // transcribes to the second word in the string vector, words.
       //
       // Second iteration does the inverse, so I need for the 'x' index below.
       //
       // when w = 0, x =  1 and likewise when w = 1, x = 0

      for (auto it = words[w].begin(); it != words[w].end(); ++it)
        // going over letters in the word to map them to a digit in 'sn'
        atod[*it] = sn[words[w].find(*it)] - '0';  // char -'0' yields digit

      transcription = 0;    // reset
      int x = (w + 1) % 2;  // index of other word in the string vector, words
      for (long i = words[x].size() - 1; i != -1; --i)
        transcription += atod[words[x][words[x].size() - i - 1]] * pow(10, i);

      // The above for loop creates a new number, 'transcription', generated
      // from the 'x' word from 'words' via the map made from the 'w' word.
      // It's hard to describe how it computes 'transcription', but here's a
      // brief and simple example demonstrating what it's doing:
      //    483 = 4*10^2 + 8*10^1 + 3*10^0

      // The boolean below first checks that 'transcription' is a square number,
      // and then checks that they have the same number of digits.  Without the
      // second test, bugged answers occur due to leading 0's popping up in
      // 'transcription':
      // ex) 4501 has an anagram of 0145, but that is interpreted as 145.
      if ((floor(pow(transcription, 0.5)) == pow(transcription, 0.5)) &&
          (ceil(log10(transcription)) == ceil(log10(n))))
        winner = true;  // winner winner chicken dinner
    }

    return winner;
  }
}
