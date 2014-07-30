#!/usr/bin/env python
"""
file: 5.py
date: Fri Jul 25 09:53:39 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: 2520 is the smallest number that can be divided by each of the numbers 
      from 1 to 10 without any remainder. What is the smallest positive number 
      that is evenly divisible by all of the numbers from 1 to 20?
      Ans: 232792560 on Wed Jul 30 10:33:40 EDT 2014
"""

def primes(n):
    divisors = [ d for d in range(2,n//2+1) if n % d == 0 ]
    return [ d for d in divisors if \
             all( d % od != 0 for od in divisors if od != d ) ]

def main():
    """
    For now just do the raw math.
    """
    print 2*2*2*2*3*3*5*7*11*13*17*19
    return 0
    for i in range(1,101):
        print i,primes(i)
    return 0

if __name__ == "__main__":
    main()
"""
2 = 2
3 = 3
4 = 2*2
5 = 5
6 = 2*3
7 = 7
8 = 2*2*2
9 = 3*3
10 = 2*5
...for up to 20
11=11
12=2*2*3
13=13
14=2*7
15=3*5
16=2*2*2*2
17=17
18=2*3*3
19=19
20=2*2*5

The LCM of all those must have as many factors of
each prime that appears in any factorization
2 appears at most 3 times as a factor of 8
3 appears at most 2 times as a factor of 9
5 appears at most 1 time as a factor if 5 and 10
7 appears at most 1 time as a factor of 7
...for up to 20
2 for 4
3 for 2
5 for 1
7 for 1
11 for 1
13 for 1
17 for 1
19 for 1

So the LCM has
3 factors of 2, 2 factors of 3, and 1 facor each of 5 and 7
LCM = 2*2*2*3*3*5*7 = 2520 
So for up to 20...
2*2*2*2*3*3*5*7*11*13*17*19= 232792560
"""
