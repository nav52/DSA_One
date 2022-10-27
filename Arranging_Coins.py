"""
Question

You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:

$
$ $
$ $ -
    
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:

$
$ $
$ $ $
$ $ - -

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:

1 <= n <= 231 - 1
"""
#Solution

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # for k rows, we need k(k+1)/2 coins.
        # We can do a binary search to find the max k
        # where k(k+1)/2 <= n
        
        left, right = 0,n
        while left <= right:
            k = (left+right)//2
            curr = k*(k+1)//2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
        
