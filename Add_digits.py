"""
Question

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

"""
# Solution

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        outNum = 0
        while num>0:
            outNum += num%10
            num = num//10
            
            if num == 0 and outNum>9:
                num = outNum
                outNum = 0
        
        return outNum

# Solution using the math way.
"""
    Any number  n = d0 + d1*10 + d2*100 + ..+dk*100..0
                n = d0 + d1*(9*1+1) + d2*(9*11+1)+....+dk*(9*111..11+1)
                n = (d0+d1+d2+...+dk) + 9*(d1*1 + d2*11 +...+ dk*111...11)
    Taking mod 9  on both sides
                n mod 9 = (d0 + d1 + d2 +...+ dk) mod 9
    if n = 0, output = 0
    if n = 9k, output = 9
    if n != 9k, output = n mod 9
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num%9 == 0:
            return 9
        return num%9