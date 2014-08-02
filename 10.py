#!/usr/bin/env python
"""
file: 10.py
date: Thu Jul 31 09:25:11 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of 
      all the primes below two million.
      Ans: 142913828922 on Fri Aug  1 22:34:07 EDT 2014
"""
def prime_list(num):
    """
    From: http://en.wikibooks.org/wiki/Efficient_Prime_Number_Generating_
    Algorithms
    Return primes up to but not including num.
    Acts goofy below 20.
    """
    from math  import sqrt
    pp=2
    ep=[pp]
    pp+=1
    tp=[pp]
    ss=[2]
    #lim=raw_input("\nGenerate prime numbers up to what number? : ")
    lim= int(num)
    while pp<int(lim):
        pp+=ss[0]
        test=True
        sqrtpp=sqrt(pp)
        for a in tp:
            if a>sqrtpp: break
            if pp%a==0:
               test=False
               break
        if test: tp.append(pp)
    ep.reverse()
    [tp.insert(0,a) for a in ep]
    return tp

def main():
    """
    """
    num= 2000000
    ans= prime_list(num)
    print("Sum of primes found between 2 and %d: %d" % (num, sum(ans)))
    print("Found a total of %d primes." % len(ans))
    if len(ans) <= 6:
        print("Primes: %s" % str(ans))
    else:
        print("From %s... to ...%s" % (str(ans[:3]),ans[-3:]))
    return 0

if __name__ == "__main__":
    main()
