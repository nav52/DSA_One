"""
Question

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

"""
# Solution

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """                 
        n = len(nums)        
        lastNonZero = 0      
        for i in range(n):
            if(nums[i] != 0 ):
                nums[lastNonZero] = nums[i]
                lastNonZero += 1 
        for zeroIndex in range(lastNonZero,n):
            nums[zeroIndex] = 0      