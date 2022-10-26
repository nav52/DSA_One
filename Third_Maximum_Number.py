"""
Question

Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
#Solution

class Solution(object):
    def thirdMax_using_set(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return max(nums)
        else:
            return sorted((set(nums)))[-3]

    # without using set and sorted
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        oneMax = nums[0]
        secMax = float('-inf')
        thirdMax = float('-inf')
        
        if len(nums)<3:
                return max(nums)
        
        for i in range(1, len(nums)):
            if nums[i]>oneMax:
                thirdMax = secMax
                secMax = oneMax
                oneMax = nums[i]
            elif nums[i]>secMax and nums[i]<oneMax:
                thirdMax = secMax
                secMax = nums[i]
            elif nums[i]>thirdMax and nums[i]<secMax:
                thirdMax = nums[i]
                
        return thirdMax if thirdMax != float('-inf') else oneMax

