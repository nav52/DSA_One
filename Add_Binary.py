"""
Question

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
#Solution

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # int(a,2) --> Converts binary a to integer base 10.
        # bin() converts an interger to binary and the result is "0b<bin_nim>"
        # Strip the result from 2nd index on to get the binary number
        total=bin(int(a,2)+int(b,2))[2:]
        return total