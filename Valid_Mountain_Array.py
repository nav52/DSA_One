"""
Question

Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""
#Solution

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Array less than 3 elements is not a valid Mountain Array
        if len(arr) < 3:
            return False

        # If the first 2 elements are not in increasing order, its not a valid Mountain Array
        if arr[0:2] != sorted(list(set(arr[0:2]))):
            return False
        
        indexi = -1
        #Loop from element 2 with comparison to find the peak 
        for i in range(1, len(arr) -1):
            if arr[i+1] < arr [i]:
                indexi = i
                break
            elif arr[i+1] == arr[i]:         # There cannot be 2 peaks
                return False
        # If no peak is found, return False
        if indexi == -1:
            return False
        
        #check if the array after the peak is strictly decreasing
        if arr[indexi:][::-1] == sorted(list(set(arr[indexi:]))):
            return True
        
        return False