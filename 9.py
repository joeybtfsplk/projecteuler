#!/usr/bin/env python
"""
file: 9.py
date: Thu Jul 31 04:49:48 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: A Pythagorean triplet is a set of three natural numbers, a < b < c, for 
      which, a^2 + b^2 = c^2.  For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.  
      There exists exactly one Pythagorean triplet for which a + b + c = 1000.
      Find the product a*b*c.
      Ans: 31875000 on Thu Jul 31 08:28:42 EDT 2014
"""

def main():
    """
    Experimented and found out the answer was after 200, so started there.
    """
    for i in range(200,1001):
        for j in range(200,1001):
            for k in range(200,1001):
                if k > j:
                    if j > i:
                        sums= (i+j+k==1000)
                        prods= (i**2+j**2)==k**2
                        if sums and prods:
                            print i,j,k,i+j+k,i**2+j**2,k**2
                            print i*j*k
                            return 1
    return 0

if __name__ == "__main__":
    main()
