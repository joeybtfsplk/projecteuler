#!/usr/bin/env python
"""
file: 4.py
date: Thu Jul 24 20:26:24 EDT 2014
from: Project Euler: http://projecteuler.net
auth: tls
purp: A palindromic number reads the same both ways. The largest palindrome 
      made from the product of two 2-digit numbers is 9009 = 91 x 99. Find
      the largest palindrome made from the product of two 3-digit numbers.
      Ans: 906609 on Fri Jul 25 09:01:44 EDT 2014
"""

def palindrome_check(num):
    """
    Convert number to a string. Compare string's digits, left-most digit to
    right-most digit for equality. If they all match break out of for loop
    and return True else return False.
    """
    num= str(num)
    len_num= len(num)
    for i in range(len_num/2):
       if num[i] == num[len_num-i-1]:
            ans= True
       else:
            ans= False
            break
    return ans

def main():
    """
    Check numbers starting at 999 down to 890 (since I found one before 999*890.)
    """
    for l in range(999,890,-1):
        for r in range(999,890,-1):
            num= l*r
            ans= palindrome_check(num)
            if ans:
                print l,r,num
                return
            print l,r,num
    print "No palindrome found."
    return

if __name__ == "__main__":
    main()
