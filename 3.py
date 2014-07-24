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
    """
    Make test_factor equal to the lowest prime (2).
    While the square of the test_factor is < than the number:
        while the number mod test_factor equals 0:
            divide the number by test_factor and use that number
        add one to the test_factor
    Upon exit test_factor equals the largest prime or equals the number
    """
    num = 600851475143 
    test_factor = 2
    while (test_factor * test_factor) < num:
        while num % test_factor == 0:
            num = num / test_factor
        test_factor += 1
    print (num)
    return

if __name__ == "__main__":
    main()
