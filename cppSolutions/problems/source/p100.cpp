#include <problems/p100.hpp>

// I actually had to cheat on this one.  Using the "Crappy Function" I was able
// to determine several blue disc values, 'a', that satisfied the given
// restrictions in p100 for a>0.  Searching for this sequence: 15,85, 493, 2871
// on OEIS yielded the following recursive function for generating 'a' values:
// a(n) = 6a(n-1)-a(n-2)-2 with a(0) = 1 and a(1) = 3.  Using this recursive
// function and the closed function relating 'a' and 'n' (total discs), I was
// able to come up with the answer very quickly.  My "crappy function" was
// going much too slow, not sure how to improve it... :(
namespace problems
{  // It can be shown that a = sqrt((n^2-n+0.5)/2) + 0.5, where a = number
  //  of blue discs and n = total discs.  All that's left is to iterate
  // from n = 10^12 and go until an n that satisifies the above equation is
  // found.
  // To get the above formula, realize that P(BB) = 50% implies:
  // (a/n)*(a-1)/(n-1) = 1/2
  // Next, group a's and n's on opposite sides, complete the square on the a's
  // side to solve for a in terms of n, yielding the above equation. (do the
  // opposite to get equation for n in terms of a).
  long long p100() { return generate_blues(1, 3); }  // Main Function
  long double magic_equation(long double n)
  {
    return std::sqrt((n * n - n + 0.5) / 2) + 0.5;
  }

  long double magic_equation_inverse(long double a)
  {
    return std::sqrt(2 * a * a - 2 * a + 0.25) + 0.5;
  }

  long double generate_blues(long double a0, long double a1)
  {
    if (magic_equation_inverse(a1) > 1000000000000)
      return a1;
    return generate_blues(a1, 6 * a1 - a0 - 2);
  }

  /*--- Crappy Function ------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  bool is_it_fifty(long long n, long long a)
  {  // Finds prime factors of probability's numerator and denominator generated
     // from 'a' and 'n', according to the given equation in p100.  Since it
     // should equal 50%, the denominator and numerator should contain the same
     // prime factors, except denominator will have an extra '2'.  This function
     // checks to see if the numerator and denominator have all same primes
     // except for a factor of 2 in denominator.
    vector<long long> numerator;
    vector<long long> denominator;

    vector<long long> aPrimes = common::prime_factors(a);  // a primes
    for (auto it = aPrimes.begin(); it != aPrimes.end(); ++it)
      numerator.push_back(*it);
    vector<long long> aPrimesM1 = common::prime_factors(a - 1);  // a-1 primes
    for (auto it = aPrimesM1.begin(); it != aPrimesM1.end(); ++it)
      numerator.push_back(*it);
    std::sort(numerator.begin(), numerator.end());

    // I REALLY SHOULD BE USING STD::COPY!!!  XD
    vector<long long> nPrimes = common::prime_factors(n);  // n primes
    for (auto it = nPrimes.begin(); it != nPrimes.end(); ++it)
      denominator.push_back(*it);
    vector<long long> nPrimesM1 = common::prime_factors(n - 1);  // n-1 primes
    for (auto it = nPrimesM1.begin(); it != nPrimesM1.end(); ++it)
      denominator.push_back(*it);
    std::sort(denominator.begin(), denominator.end());

    int numSize = numerator.size();
    int denSize = denominator.size();
    if (numSize + 1 == denSize)
    {
      for (int i = numSize - 1; i >= 0; --i)
        if (numerator[i] == denominator[i + 1])
          denominator.pop_back();
      if (denominator.size() == 1 && denominator[0] == 2)
        return true;  // satisfies p100
    }
    return false;  // does not satisfy p100
  }
}
