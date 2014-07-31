#!/usr/bin/env python
"""
file: 10.py
date: Thu Jul 31 09:25:11 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of 
      all the primes below two million.
      Ans: 
      The sum of all primes from 2 to 1,999,993 is 142,913,828,922
"""

def primes(n):
    """
    Return list of prime factors of n.
    If list == [] n is a prime.
    """
    divisors = [ d for d in xrange(2,n//2+1) if n % d == 0 ]
    return [ d for d in divisors if \
             all( d % od != 0 for od in divisors if od != d ) ]

def xprime_sieve(num):
    summed= 2 + 3 + 5 + 7
    prime_list= [2,3,5,7]
    for i in xrange(8,num):
        if i % 2== 0 or i % 3== 0 or i % 5== 0 or i % 7== 0:
            next
        else:
            ans= primes(i)
            if len(ans) == 0:
                summed += i
                prime_list.append(i)
                #print i
    print prime_list
    return summed

def prime_sieve(num):
    """
    try this one out
    """
    summed= 0
    prime_list= [2]
    for i in xrange(3,num,2):
        for p in prime_list:
            if i % p == 0:
                next
        else:
            ans= primes(i)
            if len(ans) == 0:
                prime_list.append(i)
                summed += i
                last_prime= i
                #print i
    print("num= %d, last prime: %d" % (num,last_prime))
    print prime_list
    return summed

def main():
    """
    """
    num= 10
    num= 2000000
    ans= prime_sieve(num)
    print("Sum: %d" % ans)
    return 0

if __name__ == "__main__":
    main()
