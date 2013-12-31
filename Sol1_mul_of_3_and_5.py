#!/usr/bin/env python

"""
Solution to Project Euler Question 1

Multiples of 3 and 5
--------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.
"""

def run():
    """Main Function"""
    sum = 0
    for each_num in range(3, 1000):
        if each_num % 3 == 0 or each_num % 5 == 0:
            sum = sum + each_num
    print "Sum of all 3 and 5 multiples is %d" % sum
    
if __name__ == '__main__':
    run()
