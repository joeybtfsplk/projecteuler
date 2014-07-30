#!/usr/bin/env python
"""
file: 6.py
date: Wed Jul 30 16:03:05 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
      see that the 6th prime is 13.  What is the 10,001st prime number?
      Ans: 104743 on Wed Jul 30 19:41:31 EDT 2014
"""
def primes(n):
    m = (n-1) // 2
    b = [True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
            if len(ps) == 10001:
                return ps
        i+=1; p+=2
    return ps

def main():
    """
    """
    prime_list= primes(2000000)
    print prime_list[-5:]
    print len(prime_list)
    return 0

if __name__ == "__main__":
    main()
