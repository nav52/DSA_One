"""
Question

Given an integer num, return a string of its base 7 representation.

Example 1:

Input: num = 100
Output: "202"

Example 2:

Input: num = -7
Output: "-10"

Constraints:

-107 <= num <= 107
"""
#Solution

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # set the positivity flag, initialize the base_seven variable
        p=1
        base_seven = ""
        if num ==0:
            return "0"
        if num<0:
            p=-1
            num = num*p
        while num>0:
            base_seven += str(num%7)
            num = num//7
        
        return str(int(base_seven[::-1])*p)
