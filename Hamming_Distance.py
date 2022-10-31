"""
Question

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them. 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:

Input: x = 3, y = 1
Output: 1

Constraints:

0 <= x, y <= 231 - 1
"""
#Solution

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # XOR will give 1's for the change amonth the 2 inputs
        # count the number of 1s to get the hamming distance
        res = x^y
        ham_dist = bin(res).count('1')
        return ham_dist
