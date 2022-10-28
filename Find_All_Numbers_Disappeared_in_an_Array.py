"""
Question

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums. 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
"""
#Solution

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Traverse the array and change the sign at indexes of present element
        for num in nums:
            index = abs(num)-1
            nums[index] = -1*abs(nums[index])
        missed_nums =[]
        # Iterate through nums and get the index of positive values
        # if say num[4] is positive, then number 5 is not in nums
        for i,num in enumerate(nums):
            if num>0:
                missed_nums.append(i+1)
        return missed_nums