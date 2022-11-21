"""
Question

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""
#Solution

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Two pointer approach
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # check and compare by removing right element and then left element 
                return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]
        
        return True