#!/usr/bin/env python
"""
file: 1.py
date: Thu Jul 24 08:48:51 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: If we list all the natural numbers below 10 that are multiples of 3 or 5, 
      we get 3, 5, 6 and 9. The sum of these multiples is 23.  Find the sum of 
      all the multiples of 3 or 5 below 1000.
      Ans: 233168 was correct on Thu Jul 24 09:22:46 EDT 2014
"""
def main():
    return sum([i for i in range(1,1000) if (i % 3 == 0) or (i % 5 == 0)])

if __name__ == "__main__":
    print main()
