"""
Question

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

"""
# Solution

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        
        left, right = 0,0
        result = []
        while left<len(nums1) and right<len(nums2):
            if nums1[left] < nums2[right]:
                left+=1
            elif nums2[right] < nums1[left]:
                right+=1
            else:
                result.append(nums1[left])
                left+=1
                right+=1
        return result