"""
Question

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

"""
# Solution

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The thought process has 2 simple parts:
            # the XOR of a number with itself = 0 (so the XOR sum of all the numbers occuring twice would be 0)
            # the XOR of a number with 0 = the number itself (so the resultant XOR sum would be the number occuring only once)
        xor_sum=0
        for num in nums:
            xor_sum^=num
        return xor_sum