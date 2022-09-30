"""
Question

Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k. 

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""
# Solution

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(nums)):
            # If the number is not in hash, add it
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            # if the number is in hash, see if the current index 
            # and the value of the number in hash is less than k
            # else add it again to hash to rewrite the value to current index
            elif nums[i] in hashMap:
                if abs(i-hashMap[nums[i]]) <= k:
                    return True
                else:
                    hashMap[nums[i]]=i
        return False