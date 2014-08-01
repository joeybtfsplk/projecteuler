#!/usr/bin/env python
"""
file: 10.py
date: Thu Jul 31 09:25:11 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of 
      all the primes below two million.
      Ans: 142913828922 on Fri Aug  1 19:15:40 EDT 2014
"""
def prime_list(num):
    """
    From: http://en.wikibooks.org/wiki/Efficient_Prime_Number_Generating_
    Algorithms
    Modified: tls, fixed so entering 10 did not return 11 in the list of primes.
    Return primes up to but not including num.
    """
    num= int(num)
    if num <= 2:
        return []
    tp= [2]    # fills up with primes
    pp= 3        # potential primes
    while pp < num:
        test= True
        sqrtpp= int(pp**0.5)
        for a in tp:
            if a > sqrtpp: # can be no more compoents from here on
                break
            if pp % a == 0:# well, it's divisible by something
                test= False
                break
        if test: 
            tp.append(pp)
        pp += 2
    return tp

def main():
    """
    """
    num= 2000000
    ans= prime_list(num)
    print("Sum of primes from 2 to %d: %d" % (num, sum(ans)))
    print("Found a total of %d primes." % len(ans))
    if len(ans) <= 6:
        print("Primes: %s" % str(ans))
    else:
        print("From %s... to ...%s" % (str(ans[:3]),ans[-3:]))
    return 0

if __name__ == "__main__":
    main()
