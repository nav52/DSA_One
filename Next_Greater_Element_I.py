"""
Question

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
"""
#Solution
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums2:
            return None
        
        # Create a hashmap to store the next greater element of each of numbers in nums2
        # Have a stack to store the numbers which can be popped to find the greater element of a num        
        nge_map = {}
        stack = []
        next_greater_element = []
        
        stack.append(nums2[0])
        
        # Loop through nums2 and check if the num is greater than the last element of stack.
        # If yes, then the next greater element of the last element in stack is the number.
        # Same holds good for next stack element as well as long as number is greater and stack is not empty.
        for num in nums2:
            while stack and num > stack[-1]:
                nge_map[stack.pop()] = num
            stack.append(num)
        
        # If there are elements in stack, this means that they don't have a next greater element
        # their values are defaulted to -1
        for num in stack:
            nge_map[num] = -1
            
        # Loop through nums1 and check for next greater element from the hashmap
        for num in nums1:
            next_greater_element.append(nge_map[num])
        
        return next_greater_element
        