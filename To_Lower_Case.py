"""
Question

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:

Input: s = "Hello"
Output: "hello"

Example 2:

Input: s = "here"
Output: "here"

Example 3:

Input: s = "LOVELY"
Output: "lovely"

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
"""
#Solution

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach other than s.lower()
        # chr(65) == ord('A')
        # ASCII A-Z ==> 65-90. Lowercase starts from 97
        result = ""
        
        for letter in s:
            if 90>=ord(letter)>=65:
                result += chr(ord(letter)-ord('A')+ord('a'))
            else:
                result += letter
        return result
