"""
Question

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
                                    1
                                  1   1
                                1   2   1
                              1   3   3   1
                            1   4   6   4   1

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]
"""
# Solution

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        outer_array = []
        for i in range(rowIndex+1):
            inner_array = []
            for j in range(i+1):               #Each row has i+1 elements
                if j == 0 or j == i:           #First and Last elements of each row is 1
                    inner_array.append(1)
                else:                               
                    inner_array.append(outer_array[i-1][j-1]+outer_array[i-1][j])    #Adding Previous row's current and previous elements
            outer_array.append(inner_array)
        return outer_array[rowIndex]