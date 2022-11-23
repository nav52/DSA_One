"""
Question

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
#Solution

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # right_most_index - left_most_index+1 is the answer 
        # To do this, we need to find the most frequent element first.
        freq = {}
        left = {}
        right = {}
        
        for i,x in enumerate(nums):
            if x not in freq:
                freq[x] = 1
                left[x] = i
                right[x] = i
            else:
                freq[x] += 1
                right[x] = i
        
        lowSpan = len(nums)
        maxFreq = max(freq.values())
        
        for i in set(nums):
            if freq[i] == maxFreq:
                span = right[i]-left[i]+1
                if span < lowSpan:
                    lowSpan = span
        return lowSpan
            