"""
Question

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 
A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:

Input: num = 7
Output: false

Constraints:
1 <= num <= 108

"""
#Solution

from math import floor, sqrt

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        # Edge case
        if num<=1:
            return False
        
        divisor_sum = 1
        for i in range(2, int(floor(sqrt(num)))+1):
            if num%i == 0:
                if i*i == num:
                    # square root of num should only be addded once
                    divisor_sum += i
                else:
                    # add quotient and the divisor
                    divisor_sum += i+num//i
        return divisor_sum == num
            