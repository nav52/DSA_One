"""
Question

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""
# Solution

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Dynamic programming
        # One and Two represent the n and n-1 stair and no. of steps needed to reach nth step from n and n-1
        # It forms a fibonacci sequence.
        one, two = 1,1
        for i in range(n-1):
            temp_one = one
            one = one+two
            two = temp_one
        return one