"""
Question

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""
# Solution

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Initialise a dictionary and add the numbers to it by traversing nums
        # If the num is already in the dict, return True else False
        temp_hash = {}
        for num in nums:
            if num in temp_hash:
                return True
            temp_hash[num] = True
        return False