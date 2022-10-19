"""
Question

Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true

Example 2:

Input: num = 14
Output: false

Constraints:

1 <= num <= 2^31 - 1

"""
# Solution

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Binary search
        # For a perfect square, the actual number will be <= half of perfect square number
        if num == 1: 
            return True
        low = 0
        high = num//2
        while low<=high:
            mid = (low+high)//2
            square = mid*mid
            if square == num:
                return True
            elif square < num:
                low = mid+1
            else:
                high = mid-1
                
        return False