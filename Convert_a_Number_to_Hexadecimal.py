"""
Question

Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:

Input: num = 26
Output: "1a"

Example 2:

Input: num = -1
Output: "ffffffff"

Constraints:

-231 <= num <= 231 - 1

"""
# Solution

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hex_map = "0123456789abcdef"
        out_hex = ""
        if num==0:
            return '0'
        for _ in range(8):
            out_hex = hex_map[num%16]+out_hex
            num = num//16
            
        return out_hex.lstrip('0')