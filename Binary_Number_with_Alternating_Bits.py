"""
Question

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.

Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.

Constraints:

1 <= n <= 231 - 1
"""
#Solution

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # If the bits of a number n are alternating,
            # Right shifting n by 1 bit and then & with n will result in 0.
            # Right shifting n by 2 bits and then | with n should result in the number n itself.
        return (n & (n>>1) == 0) & (n | (n>>2) == n)