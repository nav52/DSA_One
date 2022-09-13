"""
Question

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true

"""
# Solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return int(str(abs(x))[::-1])== x