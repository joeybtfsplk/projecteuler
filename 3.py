#!/usr/bin/env python
"""
file: 3.py
date: Thu Jul 24 13:07:22 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: The prime factors of 13195 are 5, 7, 13 and 29. What is the largest 
      prime factor of the number 600851475143?
      Ans: 6857 on Thu Jul 24 13:11:42 EDT 2014
"""

def main():
    n = 600851475143 
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i += 1
    print (n)
    return

if __name__ == "__main__":
    main()
