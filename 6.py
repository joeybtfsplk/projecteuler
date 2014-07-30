#!/usr/bin/env python
"""
file: 6.py
date: Wed Jul 30 16:03:05 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: The sum of the squares of the first ten natural numbers is
      1^2 + 2^2 + ... + 10^2 = 385.
      The square of the sum of the first ten natural numbers is,
      (1 + 2 + ... + 10)^2 = 55^2 = 3025.
      Hence the difference between the sum of the squares of the first ten 
      natural numbers and the square of the sum is 3025 - 385 = 2640.  
      Find the difference between the sum of the squares of the first one 
      hundred natural numbers and the square of the sum.
      Ans: 25164150 on Wed Jul 30 16:13:05 EDT 2014
"""

def primes(n): # save for now
    divisors = [ d for d in range(2,n//2+1) if n % d == 0 ]
    return [ d for d in divisors if \
             all( d % od != 0 for od in divisors if od != d ) ]

def sum_squares(num):
    sum= 0
    for i in range(1,num+1):
        sum += i * i
    return sum

def square_sums(num):
    sum= 0
    for i in range(1,num+1):
        sum += i
    return sum * sum

def main():
    """
    """
    num= 10
    diff= square_sums(num) - sum_squares(num)
    print diff
    num= 100
    diff= square_sums(num) - sum_squares(num)
    print diff
    return 0

if __name__ == "__main__":
    main()
