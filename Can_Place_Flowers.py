"""
Question

You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
#Solution

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            # check if the current plot is empty
            if flowerbed[i] == 0:
                # check if the left and right plots are empty
                empty_left_plot = (i==0) or (flowerbed[i-1]==0)
                empty_right_plot = (i == len(flowerbed)-1) or (flowerbed[i+1]==0)
                
                if empty_left_plot and empty_right_plot:
                    flowerbed[i]=1
                    count += 1
                    if count >= n:
                        return True
        return count >= n