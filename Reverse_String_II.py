"""
Question

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
"""
#Solution

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # check for every 2k string blocks.
        # if the curr_index+block(k) is within the length of string
        #   reverse the k block and append the rest
        # if curr_index+vlock(k) exceeds or equals the string length
        #   just reverse the k block/rest of chars.
        for i in range(0, len(s), 2*k):
            if (i+k)<len(s):
                s = s[0:i]+s[i:i+k][::-1]+s[i+k:]
            else:
                s = s[0:i]+s[i:i+k][::-1]
        return s