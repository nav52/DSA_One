"""
Question

You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
    which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:

Input: nums = [1,1]
Output: [1,2]

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
"""
#Solution

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = 1+hashmap.get(num, 0)
        missing = 1
        for num in range(1, len(nums)+1):
            if num in hashmap:
                if hashmap[num] == 2:
                    dup = num
            else:
                missing = num
                
        return [dup, missing]